# Process File:LBYL

import os

p = 'C:\sumit\Python_Learning/datafile1.dat'

try:
    
    print("File Exist")

except ValueError as e:
    print(e, file=sys.stderr)

finally:
    print("program didn't run")
