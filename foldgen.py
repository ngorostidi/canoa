from datetime import datetime
import sys

in1 = str(sys.argv[1])

today = datetime.now()

#filename = today.strftime('%Y-%m-%d-%H.%M')+'-'+in1 
filename = in1
print(filename)
