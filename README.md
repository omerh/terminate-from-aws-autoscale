# terminate-from-aws-autoscale
Python lib for terminating AWS Instance from an autoscaling group

Import lib and call `terminate_instance_from_autoscale()`

Instance need to have a role attached with the folling policy

```json
{
	"Version": "2012-10-17",
	"Statement": [{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"ec2:TerminateInstances",
				"autoscaling:DetachInstances"
			],
			"Resource": [
				"arn:aws:ec2:*:*:instance/*",
				"arn:aws:autoscaling:*:*:autoScalingGroup:*:autoScalingGroupName/*"
			]
		},
		{
			"Sid": "VisualEditor1",
			"Effect": "Allow",
			"Action": [
				"autoscaling:DescribeAutoScalingInstances",
				"ec2:DescribeInstances"
			],
			"Resource": "*"
		}
	]
}
```
