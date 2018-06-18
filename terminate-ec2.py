import boto3
import requests
import json


def get_instance_id():
    try:
        response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
        instance_id = response.text
        response = json.loads(requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document').text)
        region = response['region']
        print("Instance info: " + instance_id + " region: " + region)
        return instance_id, region
    except Exception, exc:
        return None, None


def is_running_on_aws():
    instance_id, region = get_instance_id()

    if not instance_id:
        return False

    return True


def get_autoscale_group_name_by_instance_id(instance_id, region):
    client = boto3.client('autoscaling', region)
    try:
        response = client.describe_auto_scaling_instances(
            InstanceIds=[instance_id],
            MaxRecords=1)

        autoscale_group_name = response['AutoScalingInstances'][0]['AutoScalingGroupName']
        return autoscale_group_name
    except Exception, exc:
        print(exc)
        return None


def detach_ec2_from_autoscale(instance_id, autoscale_group_name, region):
    client = boto3.client('autoscaling', region)
    try:
        client.detach_instances(
            InstanceIds=[
                instance_id,
            ],
            AutoScalingGroupName=autoscale_group_name,
            ShouldDecrementDesiredCapacity=True
        )
    except Exception, exc:
        print(exc)


def terminate_self_ec2_instance(instance_id, region):
    ec2 = boto3.resource('ec2', region)
    ec2.instances.filter(InstanceIds=[instance_id]).terminate()


def terminate_instance_from_autoscale():
    try:
        instance_id, region = get_instance_id()

        if not instance_id:
            raise Exception("Opps.. not running on aws")

        autoscale_group_name = get_autoscale_group_name_by_instance_id(instance_id, region)

        if not autoscale_group_name:
            raise Exception("Cannot get auto scale group")

        detach_ec2_from_autoscale(instance_id, autoscale_group_name, region)
        terminate_self_ec2_instance(instance_id, region)
    except Exception, e:
        return e
