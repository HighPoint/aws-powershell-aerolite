# Aerolite on AWS

Call Microsoft Powershell commands on AWS Windows EC2 instances easily. This uses the 

# Requirements

AWS System Manager uses port 443 to communicate with the Windows EC2 Instance. This port must be open. P

# How to Use

# Samples

A file
```
SampleCommands.txt
```

is include in as demo. This file will

- Change the Time Zone to Eastern Standard Time
- Rename the Computer to "WS2019-01"
- Restart the Computer
- Install Remote Server Admin Tools for Active Directory
- Restart the Computer (again)
- Create a directory "c:\installer"
- Copy Firefox Installer to the directory
- Install Firefox
- Clean up

# Python Files

The Python Files

```   
 isWindowsMachineAvailable.py
 parsePowerShellFile.py
 runWindowsPowerShell.py
```
  
are included inline in the yaml Cloudformation template. They are include here for reference.


Happy Coding!
  
