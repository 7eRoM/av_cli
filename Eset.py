...

exit_code = 0
try:
	result = check_output('"C:\\Program Files\\ESET\\ESET Security\\ecls.exe" /base-dir="C:\\Program Files\\ESET\\ESET Security\\Modules" /heur /files C:\\Users\\user\\Desktop\\file.rar', stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
	result = e.output
	exit_code = e.returncode
	pass

result = result.decode("ascii","ignore")
malwareName = "Clean"
 
if (exit_code == 0):
	malwareName = "Clean"
elif (exit_code == 10 or exit_code >= 100):
	malwareName = "Unable"
elif (exit_code == 1 or exit_code == 50):
	malwareNamePattern = re.search(r'", threat="(.*?)"', result)
	malwareName = malwareNamePattern.group(1)

malwareName = "ESET:" + malwareName		 

...
