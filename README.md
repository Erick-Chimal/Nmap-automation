<h1>Automating Nmap Scanning with Python</h1>

[YouTube Demonstration](https://youtu.be/aUhnVI5CLY0)

<h2>Description</h2>
The goal of this script is to make life easier for anyone performing regular nmap scans by automating the process. This script can be added to the .bashrc_aliases file, so that all the user needs to do is type 'nmap', and the scan will be executed, with the output automatically saved to a file.
<br />

<h2>Language Used</h2>

- <b>Python</b> 

<h2>Environments Used</h2>

- <b>Windows 10</b> 
- <b>Proxmox/Pimox</b>
- <b>kali linux</b>

<h2>Security Concerns:</h2>

<b>In this script, the Operating System (OS) is being imported to allow commands to be executed. If a malicious actor were to discover this script on your local machine, they could use it to gain root access and elevate their privileges, thereby potentially allowing them access to sensitive information or resources. It is therefore critical that one takes the necessary precautions to protect against such malicious actors.<br/>

<br/>

<h2>Mitigation</h2>
<b>So how do we mitigate? Well, we have two options. The first is to use the nmap module, which comes with its own functions and does not spawn a "shell" session like the OS module. While this method is more time consuming and may require the user to read a help page to understand the syntax, it can be more effective in defending against malicious actors. The second option is to change the file modifications, making it read and executable only. This means that should the machine be compromised, the malicious actor won't be able to elevate priviledges or create persistance by injecting commands in the code.<br/>
<br/>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
-->
