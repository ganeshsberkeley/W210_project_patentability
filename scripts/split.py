import glob
import sys

def splitXML(infile):

    with open(infile, "r") as r:
        infile = infile.split('/')[-1:]
        i = -1
        while True:
            i = i + 1
            if i%500 == 0:
                print('patent: '+str(i))
            if (i == 0):
                line = r.readline()
                first = line

            if line == '':
                break

            if line == first:
                with open(sys.path[0]+'/xml-appa/'+infile[0]+'_'+str(i)+'.xml', "w") as w:
                    w.write(line)
                    line = r.readline()
                    while line != first:
                        w.write(line)
                        line = r.readline()
                        if line == '':
                            break
                    w.close()
        r.close()

files = glob.glob(sys.path[0]+"/weekly1/*.xml")
for fil in files:
	splitXML(fil)

# splitXML(sys.path[0]+'/weekly/ipg160216.xml')
    


