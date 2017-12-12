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

from datetime import datetime

# Extract the claims text
def getClaimsAndClasses(inFile, w1):

	e = xml.etree.ElementTree.parse(inFile).getroot()

	# Open the input file
	f = open(inFile, 'r')
	soup = BeautifulSoup(f, 'xml')
	if soup:
		# Publication reference
		pub_ref = soup.find('publication-reference') 
		if pub_ref:# and cs and cs is not '':
			# Document number
			publication = pub_ref.find_all('doc-number')
			for pub_num in publication:
				doc_num = pub_num.text.encode("utf-8")
				# Remove all special charecters
				doc_num = re.sub('[^A-Za-z0-9]+', '', doc_num)
				w1.write(doc_num)
				w1.write(",")
			# Date
			pub_date = pub_ref.find_all('date')
			for pub_day in pub_date:
				pd = pub_day.text.encode("utf-8")
				# Remove all special charecters
				pd = re.sub('[^A-Za-z0-9]+', '', pd)
				pd = datetime.strptime(pd, '%Y%m%d').strftime('%m/%d/%Y')
				w1.write(pd)
				w1.write(",")

		# Application reference
		appl_ref = soup.find('application-reference') 
		if appl_ref:# and cs and cs is not '':
			# Document number
			application = appl_ref.find_all('doc-number')
			for app_num in application:
				doc_num = app_num.text.encode("utf-8")
				# Remove all special charecters
				doc_num = re.sub('[^A-Za-z0-9]+', '', doc_num)
				w1.write(doc_num)
				w1.write(",")
			# Date
			app_date = appl_ref.find_all('date')
			for app_day in app_date:
				ad = app_day.text.encode("utf-8")
				# Remove all special charecters
				ad = re.sub('[^A-Za-z0-9]+', '', ad)
				ad = datetime.strptime(ad, '%Y%m%d').strftime('%m/%d/%Y')
				w1.write(ad)
				w1.write(",")

		# Claims text
		claim_sec = soup.find('claim')
		if claim_sec:# and cs and cs is not '':
			claims = soup.find_all('claim-text')

			w1.write("\"") ;
			for claim in claims:
				claim_txt = claim.text.encode("utf-8")
				claim_txt = re.sub('[\n\r]+', '', claim_txt)
				w1.write(claim_txt)
			w1.write("\"") ;
			w1.write(",")

		# Prior art
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

	#print fil

	# Open output file
	if ( i == 0 ):
		split = fil.split('/')
		inF = split[len(split) - 1]
		split = inF.split('.') 
		inF = split[0]
		w1 = open(sys.path[0]+'/scrape/'+inF+'_xml.csv', 'w')
		w1.write("publication_no,publication_date,application_no,application_date,claims_txt,prior_art\n") ;

	getClaimsAndClasses(fil, w1)

	if i % 500 == 0:
		print('finished', i)

	if (i == len(files)-1 ):
		w1.close()

	if (i == 100000):
		sys.exit(0) ;

	i += 1
