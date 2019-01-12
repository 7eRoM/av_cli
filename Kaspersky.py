...

try:
	result = check_output('"C:\\Program Files (x86)\\Kaspersky Lab\\Kaspersky Internet Security 18.0.0\\avp.com" SCAN -i0 C:\\Users\\test\\Desktop\\file.exe', shell=True, stderr=subprocess.STDOUT).decode()
except subprocess.CalledProcessError as e:
	result = e.output
	result = result.decode("utf-8")
	pass

result = re.sub("Progress\s[0-9]{1,2}%...\r","", result)        
malwareName = "Clean"	        
i=1
matchedList = re.findall(r'[\d]{4}-[\d]{2}-[\d]{2}\s+\d{2}(:\d{2}){2}\s+(.*)' , result)        
while i < len(matchedList):            
	if (("ok" in matchedList[i][1]) or ("starting" in matchedList[i][1]) or ("running" in matchedList[i][1]) or ("skipped" in matchedList[i][1]) or ("password protected" in matchedList[i][1]) or ("corrupted" in matchedList[i][1])):                                
		i=i+1
		continue            
	elif "completed" in matchedList[i][1]:                                
		i=i+1
		break
	else:        
		malwareName = matchedList[i][1].split('\t')[2]                
		break
	
malwareName = "Kaspersky:" + malwareName		 

...