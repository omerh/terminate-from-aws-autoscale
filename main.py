from ec2terminate import terminate


def main():
    try:
        #code here
    except Exception, e:
        print("Fatal: {}".format(e))
        terminate.terminate_instance_from_autoscale()


if __name__ == "__main__":
    main()
