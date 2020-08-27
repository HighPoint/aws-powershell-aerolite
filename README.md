# Aerolite on AWS

Run Microsoft Powershell commands on AWS Windows EC2 instances easily. 

Aerolite retries any failed PowerShell commands and logs all issues to CloudWatch. It runs agent-free.

![Aerolite Step Functions Graph](/images/aerolite_graph.png?raw=true)

# Requirements

Aerolite is agent-free, because it accesses the AWS System Manager installed along with your EC2. The System Manager uses port 443 to communicate with Windows EC2 Instances. Port 443 must be open. 

The EC2 also must have an IAM role that allows the AWS System Manager to communicate with it. A role, SSMRoleForInstancesQuickSetup, is included in the YAML Cloudformation template. SSMRoleForInstancesQuickSetup uses the AWS policy, AmazonSSMManagedInstanceCore. If you are creating an EC2 after running the Cloudformation template, select: 

![SSMRoleForInstancesQuickSetup](/images/ScreenShot.png?raw=true)

Otherwise, add the IAM role to the EC2 instance.

# How to Use

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
  
