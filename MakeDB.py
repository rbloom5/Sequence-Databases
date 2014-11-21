#!/usr/bin/env python
import os

def MakeDB(database):

	databaseString = "makeblastdb -in " + database + " -dbtype 'prot' "
	os.system(databaseString)


MakeDB("/Users/Ryan/PythonProjects/Databases/uniprot_sprot.fasta")