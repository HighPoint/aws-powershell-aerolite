# Aerolite on AWS

Easily run Microsoft Powershell commands on AWS Windows EC2 instances. 

Aerolite retries any failed PowerShell commands, logs all issues to CloudWatch and runs agent-free. It uses the native AWS Step Functions, Lambda, and System Manager to send, listen, and react to PowerShell commands. Below is the AWS Step Function Graph, showing how Aerolite works.


![Aerolite Step Functions Graph](/images/aerolite_graph.png?raw=true)


First, Aerolite opens a text file in an S3 bucket. It removes the comments, creating a list of commands. Next, Aerolite executes each PowerShell command individually. It waits for confirmation that the command successfully executed or failed. If the command failed, it will retry the command up to three times. Aerolite then logs all issues to a CloudWatch Log. If the command requires an Windows restart, Aerolite will wait for the EC2 to be available for PowerShell commands. 

Easily add Aerolite to your Cloudformation stacks.

# Requirements

- **The EC2 IAM role must include the AmazonSSMManagedInstanceCore policy**

The Windows EC2 must have an IAM role that allows the AWS System Manager to communicate with it. A role, SSMInstancesQuickSetupRole, is included in the YAML Cloudformation template. SSMInstancesQuickSetupRole uses the AWS policy, AmazonSSMManagedInstanceCore. If you are creating an EC2 manually after running the Cloudformation template, select: 

![SSMRoleForInstancesQuickSetup](/images/IAMRoleShot.png?raw=true)

Otherwise, add the IAM role to the EC2 instance.

- **Port 443 must be open**

Aerolite is agent-free, because it accesses the AWS System Manager installed along with your EC2. The System Manager uses port 443 to communicate with Windows EC2 Instances. The EC2 Security Group must open port 443, the standard port for HTTPS traffic. If you are creating an EC2 manually, select:

![Security Group Port 443](/images/SecurityGroupShot.png?raw=true)

If you use Remote Desktop Protocol, RDP Port 3389 should also be opened to your IP address or addresses.

# How to Use

[![Aerolite Launch Stack](/images/Aerolite-Launch-Stack.png?raw=true)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=AeroliteStack&templateURL=https://yappytest1234.s3.amazonaws.com/AWSPowerShellAerolite.yaml)

1) Click the "Aerolite Launch Stack" button above.

This will bring you to either the Cloudformation UI or the AWS console if you are not signed in. Sign in, if you are not already. From the Cloudformation UI, click "Next" at the bottom of the screen. Repeat clicking "Next" on the two following pages. You will reach a page with this towards the bottom:

![CloudFormation Shot](/images/CloudFormationShot.png)

Checkmark the three "I acknowledgement" statements and select "Create Stack." This will start building the CloudFormation stack.

2) Select or create a Windows EC2 to work with. Copy the EC2 Id.

3) Add the SSMInstancesQuickSetupRole to the EC2's IAM. The Requirements section of this Readme shows how to do this.

4) Open the HTTPS port 443 in the EC2's Security Group.

5) Navigate to the Step Functions. "Aerolite-PowerShell" should appear as an option under "State Machines." Select the "Aerolite-PowerShell" blue hyperlink. You will reach the page below:

![Step Function Shot](/images/StepFunctionShot.png)

Select the "Start Execution" button.




# Samples

```
SampleCommands.txt
```

A demo which will: 

- Change the Time Zone to Eastern Standard Time
- Rename the computer to "WS2019-01"
- Restart the computer
- Install Remote Server Admin Tools for Active Directory
- Restart the computer (again)
- Create a directory "c:\installer"
- Copy Firefox Installer to the directory
- Install Firefox
- Clean up

```
SampleUpdate.txt
```

A demo which will:

- Download all pending updates
- Install NuGet
- Install PSWindowsUpdate
- Install all pending updates
- Restart the computer

# AWS Step Functions and AWS Lambda Python Files

The Step Function file is included inline in the YAML Cloudformation template.

```
  AWSPowerShellAerolite.json
```

The AWS Lambda files are included inline in the YAML Cloudformation template.

```   
 isWindowsMachineAvailable.py
 parsePowerShellFile.py
 runWindowsPowerShell.py
```
  
They are include here for reference.

# Questions

Any questions or suggestions, just add an "Issues" submission to this repository. Thanks.

#

Happy Coding!
  
