#!/usr/bin/env python
import os
#look up syntax and methods in os
def MakeDB(FILE):
	#Makes blast compatible database from a file of protein sequences.  
	#Will make a database with the same name in the same folder (can make this more flexible in later versions)

	########Inputs########
	#FILE: the path to the (unzipped) file that you would like to turn into a blast db 

	#####Outputs#####
	#a blast db of the same name in the same folder 
	#therefore the same path used for FILE can be used for subsequent methods such as PSSM

	databaseString = "makeblastdb -in " + FILE + " -dbtype 'prot' "
	os.system(databaseString)

