...

try:
	result = check_output('"C:\\Program Files (x86)\\AVG\\Av\\avgscana.exe" /A /H /SCAN="C:\\Users\\user\\Desktop\\file.exe"', shell=True,stderr=subprocess.STDOUT).decode()
except subprocess.CalledProcessError as e:
	result = e.output
	pass

malwareName = "Clean"	
malwareNamePattern = re.search(r'[a-zA-Z]:\\(((?![<>:\"/\\|?*]).)+((?<![ .])\\)?)*', result.decode('utf-8'))
if malwareNamePattern is None:
	malwareName = "Clean"
else:
	malwareName = ' '.join(malwareNamePattern.group(1).split(' ')[1:])

malwareName = "AVG:" + malwareName		

...
