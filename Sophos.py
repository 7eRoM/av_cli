...

output = subprocess.Popen(["/opt/COMODO/cmdscan","-s","/home/user/Desktop/file.exe","-v"], stdout=subprocess.PIPE)
result = output.communicate()[0]

malwareName = "Clean"
if "---> Not Virus".encode() in result:
		 malwareName = "Clean"
else:        
		 malwareNamePattern = re.search(r'---\> Found Virus, Malware Name is (.*)', result.decode('utf-8'))
		 malwareName = malwareNamePattern.group(1)

malwareName = "Sophos:" + malwareName		 	

...
