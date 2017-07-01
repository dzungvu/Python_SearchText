import glob
import os
import re
from nltk.stem import *
from _hashlib import new


def doDict():
    # Create file
    # Save the result of search process
    result_file = open('result\\result_file.txt', 'w')
    #save all words in all file
    dictionary_file = open('dictionary\\dictionary_file.txt', 'w')
    # save worlds and document name includes them
    processed_dictionary_file = open('dictionary\\processed_dictionary_file.txt', 'w')
    # open the resource folder
    os.chdir("res")

    term={}
    posting_list={}
    stemmer = PorterStemmer();


    i = 0;
    # create dictionary type dictionary to storage words and documents include on each file
    dictionary={}

    for file in glob.glob("*.txt"):
        f = open(file,'r')
        term.clear()
        posting_list.clear()
        line_number = 0

        print("Now, I'm reading file " + f.name)
        result_file.writelines ("Line\tPosition\t\t\tFileName\n")

        while True:
            documentName = set()
            line = f.readline().lower()
            if (line == ""):
                print("Done!\n-------------------------------")
                f.close()
                break

            else:
                if (line == "\n"):
                    continue;
                listWords = []
                listWords = re.split('\W+', line)
                for idx, val in enumerate(listWords):
                    val=stemmer.stem(val)
                    if (val in term.keys()):
                        term[val]+=1;
                    else:
                        term[val]=1;

                    if (val in dictionary.keys()):
                        dictionary[val].add(f.name)

                    else:
                        dictionary[val]=set([f.name])

                line_number+=1
        posting_list[f.name] = term
        input_line=str(f.name) + ' ' + str(posting_list[f.name])
        input_line = input_line.replace('{', '')
        input_line = input_line.replace('}', '')
        input_line = input_line.replace(':', '')
        input_line = input_line.replace('\'', '')
        input_line = input_line.replace(',', '')
        input_line = re.sub(r'  [0-9]+','',input_line)
        input_line = re.sub(r'\'\':+\s+[0-9]+', '', input_line)
        dictionary_file.write(input_line+'\n')
        # dictionary_file.write(str(f.name) + ' ' + str(posting_list[f.name]) + '\n')
        f.close()

    stopWords=('a','an','and','are','as','at','be','by','for'
           ,'from','has','he','in','is','it','its','of',
           'on','that','the','to','was','were','will','with')
    for stopword in stopWords:
        if(stopword in dictionary.keys()):
            del dictionary[stopword]

    for run in dictionary.keys():
        input_line=str(dictionary[run])
        input_line = input_line.replace('{', '')
        input_line = input_line.replace('}', '')
        input_line = input_line.replace('\'', '')
        input_line = input_line.replace(',', '')
        processed_dictionary_file.write(run + ' ' + input_line + '\n');
    result_file.close()
    dictionary_file.close()
    processed_dictionary_file.close()
    return dictionary

def create_library():
    library = set([])
    for file in glob.glob("*.txt"):
        f = open(file,'r')
        library.add(f.name)
    return library

