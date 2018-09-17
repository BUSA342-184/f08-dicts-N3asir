'''
 Reads through the e-mail file from the text,
 mbox-short.txt, finds all of the lines that start with 
 From: and To; Use  dictonaries to count the following:

usernames in the From: field
hosts in the From: field
usernames in the To: field
hosts in the To: field
 '''

import sys
import csv
usernamesFrom = dict()#Making dictionaries
hostsFrom = dict()
usernamesTo = dict()
hostsTo = dict()
num = 0#counts occurences
username = ' '
source = ' '
text = open('mbox-short.txt','r')

file_lines = text.readlines()# stores file contents in a list for multi-iteration
lines = list(file_lines)

for line in lines:
    if line.startswith('From:'):  
        num = 0      
        values = line.split('@')
        username = values[0].split()[1]#before the  '@'
        for line in lines:
            if line.startswith('From:') and username in line:
                num += 1
                usernamesFrom[username] = num

for line in lines:
    if line.startswith('From:'):  
        num = 0      
        values = line.split('@')
        source = values[1].split()[0]#after the '@'            
        for line in lines:
            if line.startswith('From:') and source in line:
                num += 1
                hostsFrom[source] = num

for line in lines:
    if line.startswith('To:'):  
        num = 0      
        values = line.split('@')
        username = values[0].split()[1]
        for line in lines:
            if line.startswith('To:') and username in line:
                num += 1
                usernamesTo[username] = num
for line in lines:
    if line.startswith('To:'):  
        num = 0      
        values = line.split('@')
        source = values[1].split()[0]
        for line in lines:
            if line.startswith('To:') and source in line:
                num += 1
                hostsTo[source] = num

cw = csv.writer(sys.stdout)
#prints each dictionary is a csv ordered format
print('--- FROM USER ---')
cw.writerows(sorted(usernamesFrom.items()))

print('\n--- FROM HOST ---')
cw.writerows(sorted(hostsFrom.items()))

print('\n--- TO USER ---')
cw.writerows(sorted(usernamesTo.items()))

print('\n--- TO HOST ---')
cw.writerows(sorted(hostsTo.items()))
'''
python fromto.py

'''











