#!/usr/bin/env python

from Bio import SeqIO
import gzip

def Unzip(database, directory = "~/sprot/", outfile = None):

	#if no outfile name given, names the outfile the same as the zipped file, minus the .gz
	if outfile == None:
		outfile = database[0:len(database)-3]

	outfile = directory + outfile

	with gzip.open(database, 'rb') as dataTemp:
		with open(outfile, 'w+') as outHandle:
			SeqIO.write(dataTemp, outHandle, "fasta")


Unzip('databases/uniprot_sprot.fasta.gz')
#add stuff about file names and locations (os.filename...)