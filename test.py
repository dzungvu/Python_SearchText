listTest=("firstElement", "secondElement", "thirdElement")
setTest = set(["firstimeLoop", "secondtimeLoop", "thirdtimeLoop","firstimeLoop", "secondtimeLoop", "thirdtimeLoop"])
setTest2 = set(["firstimeLoop", "secondtimeLoop", "thirdtimeLoop","firstimeLoop", "secondtimeLoop", "thirdtimeLoop"])
print (listTest)
# dictionary = {"key":listTest,"key2": listTest}
dictionary = {"firstKey":setTest, "secondKey":setTest2}

for run in dictionary.keys():
    (dictionary[run].add("fourthimeLoop"))

dictionary["firstKey"].add("fiveTime")
newDic = 'haventCreate'
if (newDic in dictionary.keys()):
    dictionary[newDic].add("addElement")
else:
    dictionary[newDic]=set(["addElement"])

dictionary[newDic].add("addElement2")

stopWords=['a','an','and','are','as','at','be','by','for'
           ,'from','has','he','in','is','it','its','of',
           'on','that','the','to','was','were','will','with']
print(stopWords)
stopWords.pop(2);
print(stopWords)
# for run in dictionary.keys():
#     print(run, dictionary[run])
# dictionary ={"string":set(["string value"])}
# dictionary["table"]=set(["table value"])
# dictionary["table"].add("new table value")
# dictionary["table"].add("new table value")
# print (dictionary["table"])

