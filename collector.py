#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import settings
from functions import *

def collectxx(xxtype,time,args):
	verbose(args,xxtype+"--"+str(time))
	verbose(args,settings.options[xxtype]["B"])
	#print(settings.options[xxtype]["A"])
	#print(time)
	if(os.path.exists(settings.options[xxtype]["A"])):

		s=[];
		for x in range(time):
			next_date = datetime.datetime.now() - datetime.timedelta(minutes=x)
			
			
			verbose(args,"Date:"+str(x)+"-"+next_date.strftime(settings.options[xxtype]["B"]))
			s.append(next_date.strftime(settings.options[xxtype]["B"]))

		#print('\|'.join(s))
		cmd="grep -i \""+'\|'.join(s)+"\" "+settings.options[xxtype]["A"]
		if "M1" in settings.options[xxtype]:
			cmd=cmd+" | grep \""+settings.options[xxtype]["M1"]+"\""
		
		if "M2" in settings.options[xxtype]:
			cmd=cmd+" | grep \""+settings.options[xxtype]["M2"]+"\""	
			
		if xxtype == "mat":
			cmd=cmd+ " | grep \"" +args.find + "\""
		
		
		cmd=cmd+" | wc -l"	
		verbose(args,"command")
		verbose(args,cmd)
		#print(cmd)
		logstr("cmd:"+str(cmd))
		os.system(cmd)
	else:
		print("File Not Foud")
		logstr("File Not Foud")
		logstr("Type:"+str(xxtype)+",Time:"+str(time))
		logstr("Args:"+str(args))
		
	return False
