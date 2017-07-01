import re
# open file dictionary to read
f=open('dictionary\\dictionary_file.txt', 'r')
# read line by line
line=f.readline()
# structure: word:time it appears in doc
term={}
# structure: doc:term
posting_list={}
while line!='':
    list_info=line.split()
    for idx in range(1,len(list_info),2):
        term[list_info[idx]]=int(list_info[idx+1])
    posting_list[list_info[0]]=term
    line=f.readline()
f.close()
print (len(posting_list))
print (len(posting_list['1.txt']))
print (len(posting_list['100.txt']))
print (len(posting_list['45.txt']))
print (len(term))




