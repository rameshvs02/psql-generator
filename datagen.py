import random
import string
from datetime import datetime, timedelta

datatype = ['int','bigint','char','varchar','date','float','text','time','timestamp']
dformat = ["%B %d, %Y" , "%Y-%m-%d" , "%d/%m/%Y" , "%d/%m/%y" , "%Y-%b-%d" , "%b-%d-%Y" , "%d-%b-%Y" , "%y-%b-%d" , "%b-%d-%y" , "%d-%b-%y" , "%Y%m%d", "%y%m%d" ]
tformat = [ "%T" , "%H:%M" , "%H%M%S" , "%T.%f" , "%T %p" ]

class DataGenerator:
    def __init__(self, dtype):
    	self.dtype = dtype
    def gen_datetime(self,min_year=1900, max_year=datetime.now().year):
        # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()

    def getData(self):
        if self.dtype == "int" or self.dtype == "bigint" or self.dtype == "float" :
            data = ''.join(random.choices(string.digits, k=random.randint(1,20)))
            return data
        elif self.dtype == "char" or self.dtype == "varchar" :
            data = ''.join(random.choices(string.ascii_letters, k=random.randint(1,1024)))
            return data
        elif self.dtype == "text" :
            data = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1,2048)))
            return data
        elif self.dtype == "date" :
            data = self.gen_datetime().strftime(dformat[random.randint(0,11)])
            return data
        elif self.dtype == "time" :
            data = self.gen_datetime().strftime(tformat[random.randint(0,4)])
            return data
        elif self.dtype == "timestamp" :
            data = self.gen_datetime().strftime(dformat[random.randint(0,11)]) + " " + self.gen_datetime().strftime(tformat[random.randint(0,4)])
            return data
        else:
            return "sampledata"
