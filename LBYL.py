import os

p = 'datafile1.dat'

try:
    if os.path.exists(p):
        print("File Exist")
except OSError as e:
    print(f"Error: {e}")