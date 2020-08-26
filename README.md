# Aerolite on AWS

Call Microsoft Powershell commands on AWS Windows EC2 instances easily. This uses the 

# Requirements

AWS System Manager uses port 443 to communicate with the Windows EC2 Instance. This port must be open. P

# How to Use

# Sample Commands

A file:
```
SampleCommands.txt
```

is include in as demo. This file will:

1. Change the Time Zone to Eastern Standard Time
2. Rename the Computer to "WS2019-01"
3. Restart the Computer
4. Install Remote Server Admin Tools for Active Directory
5. Restart the Computer
6. 

# Python Files

The Python Files:

```   
 isWindowsMachineAvailable.py
 parsePowerShellFile.py
 runWindowsPowerShell.py
```
  
are included inline in the yaml Cloudformation template. They are include here for reference.


Happy Coding!
  
