...

output = subprocess.Popen(["/usr/local/bin/fpscan","/home/user/Desktop/file.exe","-r","-v","0"], stdout=subprocess.PIPE)
result = output.communicate()[0]

malwareName = "Clean"
if result == "":
		 malwareName = "Clean"
else:            
	malwareName = result.split(' ')[2]

malwareName = "F-PROT:" + malwareName		  	

...
