import boto3

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
response = client.describe_instances()
# print(response)
# print(response['Reservations'][0]['Instances'][0]['PrivateDnsName'])

def create_instance():
    instances = ec2.create_instances(
        ImageId="ami-0c4e4b4eb2e11d1d4",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )
    print(instances)

def stop_instance():
    response = client.terminate_instances(
        InstanceIds=[
            'i-09164d12bab6b7cb1',
        ],
    )
    print(response)

def get_instance_ids():
    results = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            results.append(instance['InstanceId'])
    return results

# create_instance()
# stop_instance()
print(get_instance_ids())