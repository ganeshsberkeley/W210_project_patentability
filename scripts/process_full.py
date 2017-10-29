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


def getClaimsAndClasses(inFile):

	e = xml.etree.ElementTree.parse(inFile).getroot()

	split = inFile.split('/')
	inF = split[len(split) - 1]

	f = open(inFile, 'r')
	soup = BeautifulSoup(f, 'xml')
	if soup:
		section = soup.find('section')

		if section:# and cs and cs is not '':
			section = section.text
			if section == 'H' or section == 'G':
				claims = soup.find_all('claim-text')


				w1 = open(sys.path[0]+'/claims-full/'+inF+'_.txt', 'w')

				for claim in claims:
					w1.write(claim.text.encode("utf-8"))
				w1.close()

def getPriorAndClasses(inFile):

	e = xml.etree.ElementTree.parse(inFile).getroot()

	split = inFile.split('/')
	inF = split[len(split) - 1]

	f = open(inFile, 'r')
	soup = BeautifulSoup(f, 'xml')
	if soup:
		reference = soup.find('publication-reference')


		if reference:# and cs and cs is not '':
			priorart = reference.find_all('doc-number')
			w1 = open(sys.path[0]+'/priorart/'+inF+'_.txt', 'w')
			for ref_num in priorart:
				w1.write(ref_num.text.encode("utf-8"))
				w1.write(" ")
			w1.close()


files = glob.glob(sys.path[0]+"/xml-split/*.xml")

i = 0
for fil in files:
	split = fil.split('/')
	last = split[len(split) - 1]
#	getClaimsAndClasses(fil)

	getPriorAndClasses(fil)

	if i % 500 == 0:
		print('finished', i)
	i += 1
