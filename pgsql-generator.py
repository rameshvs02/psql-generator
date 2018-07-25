 #===================================================
 #    Created by Ramesh Sivaraman, Percona LLC      #
 #===================================================
import getopt
import sys
import os
import random
import createsql

def usage():
	print("Usage: [ options ]")
	print ("  pgsql-generator.py --lines=1000 --outfile=pgsql.sql")
	print ("")
	print("Options:")
	print("  -l, --lines=<number>      Specify number of lines to generate")
	print("  -o, --outfile=<filename>  Specify SQL output file name")
	print("  -v, --version             print version number")
	print("  -h, --help                print usage info")

try:
    opts, args = getopt.getopt(sys.argv[1:],"l:o:vh",["lines=","outfile=","version","help"])
except getopt.GetoptError as err:
    print('ERROR:', err)
    print("")
    usage()
    sys.exit(2)
lines = ""
outfile = ""

if len(sys.argv) == 1:
	usage()
	sys.exit()

for opt, arg in opts:
    if opt in ("-v","--version"):
        print ('1.0')
        sys.exit()
    elif opt in ("-h","--help"):
        usage()
        sys.exit()
    elif opt in ("-l", "--lines"):
        lines = int(arg)
    elif opt in ("-o", "--outfile"):
        outfile = arg

if lines == "":
	LINE_COUNT = 100
else:
	LINE_COUNT = lines

OUTFILE = "/tmp/" + outfile
#for num in range(LINE_COUNT):
 #   print(num)

columncount = int(15*LINE_COUNT/100)
tblcount = int(15*LINE_COUNT/100)
createsql.OutFile(OUTFILE)
createsql.CreateTable(tblcount, columncount)
createsql.DropTable(tblcount)
sys.stdout = sys.__stdout__
print("DONE! Generated " + OUTFILE)
