import os
welcome = "Nmap scanner"
x = welcome.center(155, "-")
print(x)
IP = input("Target IP: ")
target = (f"Scanning {IP}")
target_ip = target.center(155, "-")
print(target_ip)
scan_type = int(input("Select your mode of scannning\n1) Quick Scan\n2) Passive Scan\n3) Aggressive scan\n"))
if scan_type == 1:
  os.system(f"sudo nmap -sV -sC -A -T4 {IP} -oN nmap_results.txt")
elif scan_type == 2:
  os.system(f"sudo nmap -sV -sV -A -T1 {IP} -oN nmap_results.txt")
else:
  os.system(f"sudo nmap -sV -sC -A -T4 -p- {IP} -oN nmap_results.txt")
