import json
import boto3
import time

class RebootException(Exception): pass
class RetryException(Exception): pass
class UnknownException(Exception): pass

def lambda_handler(event, context):

    ec2Id = event['ec2Id']
    psCommand = event['psCommand']

    ssm_client = boto3.client('ssm')

    response = execute_commands_on_windows_instances(ssm_client, [psCommand], [ec2Id], True)

    if("Restart-Computer" in psCommand):

        time.sleep(60)
        raise RebootException("Windows Needs to Restart")

        return "RebootException raised"

    commandId = response['Command']['CommandId']

    for i in range(120):
        time.sleep(5)

        response = ssm_client.get_command_invocation(CommandId=commandId,
            InstanceId=ec2Id)

        status = response['Status']
        print(response)

        if(status == 'Success'):
            if("FullyQualifiedErrorId" in response['StandardErrorContent']):
                raise UnknownException(response['StandardErrorContent'])
                return "Standard Error"
            else:
                return "Success" + " : " + response['StandardOutputContent']
        elif(status == 'Failed' or
             status == 'Terminated' or
             status == 'Canceled'):
            raise RetryException("PowerShell Command Failed, Terminated or Canceled")
            return "Failed"

    raise RetryException("PowerShell Command Timed Out")
    return "RetryException"


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
