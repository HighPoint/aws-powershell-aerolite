import json
import boto3
import time

class NoWindowsResponse(Exception): pass

def lambda_handler(event, context):

    ec2Id = event['ec2Id']

    ssm_client = boto3.client('ssm')

    response = ssm_client.describe_instance_information(
            Filters=[{"Key":"InstanceIds","Values":[ec2Id]}], MaxResults=5)

    PingStatus = response['InstanceInformationList'][0]['PingStatus']

    if(PingStatus != "Online"):
        raise NoWindowsResponse("PingStatus is " + PingStatus)

    response = execute_commands_on_windows_instances(ssm_client, ['Write-Host "MS Windows Reboot"'], [ec2Id], False)

    commandId= response['Command']['CommandId']


    for i in range(12):
        time.sleep(5)

        response = ssm_client.get_command_invocation(CommandId=commandId,
            InstanceId=ec2Id)

        status = response['Status']

        if(status == 'Success'):
            return "Powershell is available on the Windows Machine"
        elif(status == 'Failed' or
             status == 'Terminated' or
             status == 'Canceled'):
            raise NoWindowsResponse("status = " + status)
            return False

    raise NoWindowsResponse("Time out after successful ping.")

    return False


def execute_commands_on_windows_instances(client, commands, instance_ids, cloudWatchOutputEnabled):

    resp = client.send_command(
        DocumentName="AWS-RunPowerShellScript",
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
        CloudWatchOutputConfig = {
            'CloudWatchLogGroupName': 'WindowsEC2response',
            'CloudWatchOutputEnabled': cloudWatchOutputEnabled
        }
    )
    return resp
