# Aerolite on AWS

Run Microsoft Powershell commands on AWS Windows EC2 instances easily. 

Aerolite retries any failed PowerShell commands, logs all issues to CloudWatch and runs agent-free. It uses the native AWS Step Functions, Lambda, and System Manager to send, listen, and react to PowerShell commands. Below is the AWS Step Function Graph, showing how Aerolite works.


![Aerolite Step Functions Graph](/images/aerolite_graph.png?raw=true)


First, Aerolite opens a text file in an S3 bucket. It removes the comments, creating a list of commands. Next, Aerolite executes each PowerShell command individually. It waits for confirmation that the command successfully executed or failed. If the command failed, it will retry the command up to three times. Aerolite then logs all issues to a CloudWatch Log. If the command requires an EC2 restart, Aerolite will wait for the EC2 to be available for PowerShell commands. 

Easily add Aerolite to a Cloudformation stack.

# Requirements

Aerolite is agent-free, because it accesses the AWS System Manager installed along with your EC2. The System Manager uses port 443 to communicate with Windows EC2 Instances. **Port 443 must be open.** 

The EC2 must have an IAM role that allows the AWS System Manager to communicate with it. A role, SSMRoleForInstancesQuickSetup, is included in the YAML Cloudformation template. SSMRoleForInstancesQuickSetup uses the AWS policy, AmazonSSMManagedInstanceCore. If you are creating an EC2 after running the Cloudformation template, select: 

![SSMRoleForInstancesQuickSetup](/images/ScreenShot.png?raw=true)

Otherwise, add the IAM role to the EC2 instance.

# How to Use

[![Aerolite Launch Stack](/images/Aerolite-Launch-Stack.png?raw=true)](https://www.google.com)

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


Happy Coding!
  
