import random

"""
good password :
param1: contain alphanumeric 
param2: contain special symbol 
param3: minimum length 8 - 12 character 
"""

ganntt_password = " "
for i in range(15):
    randnumber = random.randint(33,123)
    ganntt_password += chr(randnumber)

print(ganntt_password)