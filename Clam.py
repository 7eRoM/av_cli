...

output = subprocess.Popen(["clamscan","-r","/home/user/Desktop/file.exe"], stdout=subprocess.PIPE)
result = output.communicate()[0]
firstLineResult = result.split('\r\n')[0].split(':')[1]

malwareName = "Clean"
if "OK".encode() in result:
		 malwareName = "Clean"
else:        
		 malwareNamePattern = re.search(r' (.*) FOUND', result.decode('utf-8'))
		 malwareName = malwareNamePattern.group(1)

malwareName = "ClamAV:" + malwareName

...
