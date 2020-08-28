# Aerolite on AWS

Easily run Microsoft Powershell commands on AWS Windows EC2 instances. 

Aerolite retries any failed PowerShell commands, logs all issues to CloudWatch and runs agent-free. It uses the native AWS Step Functions, Lambda, and System Manager to send, listen, and react to PowerShell commands. Below is the AWS Step Function Graph, showing how Aerolite works.


![Aerolite Step Functions Graph](/images/aerolite_graph.png?raw=true)


First, Aerolite opens a text file in an S3 bucket. It removes the comments, creating a list of commands. Next, Aerolite executes each PowerShell command individually. It waits for confirmation that the command successfully executed or failed. If the command failed, it will retry the command up to three times. Aerolite then logs all issues to a CloudWatch Log. If the command requires an Windows restart, Aerolite will wait for the EC2 to be available for PowerShell commands. 

Easily add Aerolite to your Cloudformation stacks.

&nbsp;

# Requirements

- **The EC2 IAM role must include the AmazonSSMManagedInstanceCore policy**

The Windows EC2 must have an IAM role that allows the AWS System Manager to communicate with it. A role, SSMInstancesQuickSetupRole, is included in the YAML Cloudformation template. SSMInstancesQuickSetupRole uses the AWS policy, AmazonSSMManagedInstanceCore. If you are creating an EC2 manually after running the Cloudformation template, select: 

![SSMRoleForInstancesQuickSetup](/images/IAMRoleShot.png?raw=true)

&nbsp;

Otherwise, add the IAM role to the EC2 instance.

&nbsp;

- **Port 443 must be open**

Aerolite is agent-free, because it accesses the AWS System Manager installed along with your EC2. The System Manager uses port 443 to communicate with Windows EC2 Instances. The EC2 Security Group must open port 443, the standard port for HTTPS traffic. If you are creating an EC2 manually, select:

![Security Group Port 443](/images/SecurityGroupShot.png?raw=true)

&nbsp;

If you use Remote Desktop Protocol, RDP Port 3389 should also be opened to your IP address or addresses.

&nbsp;

# How to Use

1. Click the "Aerolite Launch Stack" button:
&nbsp;
[![Aerolite Launch Stack](/images/Aerolite-Launch-Stack.png?raw=true)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=AeroliteStack&templateURL=https://yappytest1234.s3.amazonaws.com/AWSPowerShellAerolite.yaml)

&nbsp;

This will bring you to either the Cloudformation UI or the AWS console if you are not signed in. Sign in, if you are not already. From the Cloudformation UI, click "Next" at the bottom of the screen. Repeat clicking "Next" on the two following pages. You will reach a page with this towards the bottom:

![CloudFormation Shot](/images/CloudFormationShot.png?raw=true)

&nbsp;

Checkmark the three "I acknowledgement" statements and select "Create Stack." This will start building the CloudFormation stack.

&nbsp;

2) Select or create a Windows EC2 to work with. Copy the EC2 Instance Id.

&nbsp;

3) Add the SSMInstancesQuickSetupRole to the EC2's IAM. The Requirements section of this Readme shows how to do this.

&nbsp;

4) Open the HTTPS port 443 in the EC2's Security Group.

&nbsp;

5) Navigate to the Step Functions. "Aerolite-PowerShell" should appear as an option under "State Machines." Select the "Aerolite-PowerShell" blue hyperlink. You will reach the page below:

![Step Function Shot](/images/StepFunctionShot.png?raw=true)

&nbsp;

Select the "Start Execution" button.

&nbsp;

6) The following screen will appear:

![Step Function Input Shot](/images/StepFunctionInputShot.png?raw=true)

&nbsp;

Scroll so you can see the Input area and copy and paste following:

```
{
  "Bucket":"Your_Bucket_Name",
  "Key":"Your_Aerolite_PowerShell_File_Name",
  "ec2Id":"Your_EC2_Instance_Id"
}
```

&nbsp;

Replace "Your_Bucket_Name", "Your_Aerolite_PowerShell_File_Name, and "Your_EC2_Instance_Id" with your values. If you don't have a PowerShell to test, try one of the samples below. Now, just press the "Start Execution" button.

&nbsp;

7) Congratulations! The Aerolite Step Function will start executing the PowerShell commands in the S3 file. It's that easy.

&nbsp;

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

&nbsp;

```
SampleUpdate.txt
```

A demo which will:

- Download all pending updates
- Install NuGet
- Install PSWindowsUpdate
- Install all pending updates
- Restart the computer

&nbsp;

# AWS Step Functions and AWS Lambda Python Files

The Step Function file is included inline in the YAML Cloudformation template.

```
  AWSPowerShellAerolite.json
```
&nbsp;

The AWS Lambda files are included inline in the YAML Cloudformation template.

```   
 isWindowsMachineAvailable.py
 parsePowerShellFile.py
 runWindowsPowerShell.py
```
  
They are include here for reference.

&nbsp;

# Questions

Any questions or suggestions, just add an "Issues" submission to this repository. Thanks.

&nbsp;

Happy Coding!
  
