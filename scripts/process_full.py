import xmltodict
import pprint
import string
import glob
import xml.etree.ElementTree
from bs4 import BeautifulSoup
import time
import os, re
import sys

import unicodedata

# Extract the claims text
def getClaimsAndClasses(inFile, w1):

	e = xml.etree.ElementTree.parse(inFile).getroot()


	# Open the input file
	f = open(inFile, 'r')
	soup = BeautifulSoup(f, 'xml')
	if soup:
		pub_no = soup.find('publication-reference') 

		if pub_no:# and cs and cs is not '':
			publication = pub_no.find_all('doc-number')
			for pub_num in publication:
				doc_num = pub_num.text.encode("utf-8")
				# Remove all special charecters
				doc_num = re.sub('[^A-Za-z0-9]+', '', doc_num)
				w1.write(doc_num)
				w1.write(",")
	f.close()

	# Reopen it for claims information
	f = open(inFile, 'r')
	soup = BeautifulSoup(f, 'xml')
	if soup:
		section = soup.find('section')

		if section:# and cs and cs is not '':
			section = section.text
			if section == 'H' or section == 'G':
				claims = soup.find_all('claim-text')

				w1.write("\"") ;
				for claim in claims:
					claim_txt = claim.text.encode("utf-8")
					claim_txt = re.sub('[\n\r]+', '', claim_txt)
					w1.write(claim_txt)
				w1.write("\"") ;
				w1.write(",")
	f.close()

	# Reopen it for priorart information
	f = open(inFile, 'r')
	soup = BeautifulSoup(f, 'xml')
	if soup:
		reference = soup.find('us-references-cited')

		if reference:# and cs and cs is not '':
			priorart = reference.find_all('doc-number')
			for ref_num in priorart:
				pri_info = ref_num.text.encode("utf-8")
				pri_info = re.sub('[^A-Za-z0-9]+', '', pri_info)
				w1.write(pri_info)
				w1.write(" ")

	w1.write("\n")
	f.close()



files = glob.glob(sys.path[0]+"/xml-split/*.xml")

i = 0

for fil in files:
	split = fil.split('/')
	last = split[len(split) - 1]

	# Open output file
	if ( i == 0 ):
		split = fil.split('/')
		inF = split[len(split) - 1]
		split = inF.split('.') 
		inF = split[0]
		w1 = open(sys.path[0]+'/scrape/'+inF+'_xml.csv', 'w')
		w1.write("pub_no,claims_txt,prior_art\n") ;

	getClaimsAndClasses(fil, w1)

	if i % 500 == 0:
		print('finished', i)

	if (i == len(files)-1 ):
		w1.close()

	i += 1
