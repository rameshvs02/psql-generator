import random
import datagen
import sys

#Datatype List
datatype = ['int','bigint','char','varchar','date','float','text','time','timestamp']
#'bigserial','bit','varbit','boolean','box','bytea','cidr','circle','inet','interval','json','jsonb','line','lseg','macaddr','money','numeric','path','pg_lsn','point','polygon','real','smallint','smallserial','serial','tsquery','tsvector','txid_snapshot','uuid','xml']
#CREATE TABLE extra options list
keytype = ['pk','uk']
#Table name List
tname = ['t1','t2','t3','t4','t5']
#Column name list
cname = ['c1','c2','c3','c4','c5']
#Char count list
charcnt= [1,2,4,16,32,64,126,256,1024]

class OutFile:
    def __init__(self,filename):
        self.filename = filename
        sys.stdout = open(self.filename, "w")


#Class to select CREATE TABLE options
class OptSelection:
    def __init__(self,myextra):
        self.myextra = myextra
    def getMyextra(self):
        if self.myextra == "pk":
            return "PRIMARY KEY"
        elif self.myextra == "uk":
            return "UNIQUE"
        else:
            return ""

class CreateTable:
    def __init__(self, tblcnt, columncnt):
        self.tblcnt = tblcnt
        self.columncnt = columncnt
        for i in range(self.tblcnt):
        	datatypes = ""
        	keycolumn = ""
        	typearray = []
        	tblname = tname[i]
        	getoption = OptSelection(random.choice(keytype))
        	getvalue = getoption.getMyextra()
        	for j in range(self.columncnt):
        		typeval = random.choice(datatype)
        		typearray.append(typeval)
        		if typeval == "char" or typeval == "varchar":
        			typeval = typeval + " (" + format(random.choice(charcnt)) + ")"
        		datatypes += cname[j] + " " + typeval + ", "
        	for k in range(random.randint(1,columncnt)):
        		keycolumn += cname[k] + ","
        	keycolumn = keycolumn[:-1]
        	print("CREATE TABLE IF NOT EXISTS " + tblname + "( " + datatypes + " " + getvalue + " (" +  keycolumn + ") );")
        	for i in range(10):
        		datavalue = ""
        		for typeval in typearray:
        			dvalue = datagen.DataGenerator(typeval)
        			datavalue += "'" + dvalue.getData() + "', "
        		datavalue = datavalue[:-2]
        		print("INSERT INTO "+ tblname + " values (" + datavalue + ");")

class DropTable:
    def __init__(self, tblcnt):
        self.tblcnt = tblcnt
        for i in range(self.tblcnt):
        	tblname = tname[i]
        	print("DROP TABLE IF EXISTS " + tblname + ";")
