...

try:
	result = check_output('"C:\\Program Files\\AVAST Software\\Avast\\ashCmd.exe" C:\\Users\\user\\Desktop\\file.exe /_ --Report', shell=True, stderr=subprocess.STDOUT).decode()
except subprocess.CalledProcessError as e:
	result = e.output
	pass
	
malwareName = "Clean"	        
i=0
while(re.search(r'#\s(-)*'.encode(), result.split('\r\n')[i]) is None):            
	if "OK" in result.split('\r\n')[i]:
		i = i + 1
		continue
	else:
		malwareNamePattern = re.search(r'[a-zA-Z]:\\(((?![<>:\"/\\|?*]).)+((?<![ .])\\)?)*', result.split('\r\n')[i])
		malwareName = ' '.join(malwareNamePattern.group(1).split(' ')[1:])
		break
	
malwareName = "Avast:" + malwareName		

...
