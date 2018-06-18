from setuptools import setup


setup(
    name='ec2terminate',
    packages=[
        'ec2terminate'
    ],
    version='1.0.0',
    description='terminate autoscaling instance from within',
    author='omerh',
    email='omerha@protonmail.com',
    install_requires=[
        'boto3',
        'requests'
    ],
    url='https://github.com/omerh/terminate-from-aws-autoscale.git',
    zip_safe=False
)
