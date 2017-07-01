

'''
rules:
1. Order sort of operator will be implemented from left to right if Don't have any prioritize
2. Objects inside parentheses will be implemented first and then combine to the result before execute them
'''

import CreatingDictionary
# create read_dict as a dictionary with read_dict.keys() is vocabularies and read_dict.val is documents have that key
read_dict = CreatingDictionary.doDict()

# variable contains all the name of documents
library = CreatingDictionary.create_library()

# initialize set of documents, which is result of simple query like A and/or/not B
result=set()

# stemmer (standardize vocabularies)
from nltk.stem import *
# initialize stemmer
stemmer=PorterStemmer();


# to make the query easy to split
def rewrite_query(query):
    _new_query = str(query).replace(')', ' )')
    _new_query = _new_query.replace('(', '( ')
    return _new_query

'''
left_operand is the word in the left of query
ex: A and B --> left_operand is A
The same with right_operand
'''

'''
main idea: check the existence of left and right operand
and for each situation, choose the reasonable way to return result
'''
# operate processing
def andToken(left_operand, right_operand):
    if (left_operand in read_dict.keys()) and right_operand in read_dict.keys():
        result = read_dict[left_operand] & read_dict[right_operand]
    else:
        result = set('')
    return result

def orToken(left_operand, right_operand):
    if (left_operand in read_dict.keys()) and (right_operand in read_dict.keys()):
        result = read_dict[left_operand] | read_dict[right_operand]
    elif (left_operand in read_dict.keys()):
        result = read_dict[left_operand]
    elif right_operand in read_dict.keys():
        result = read_dict[right_operand]
    else:
        result = set('')
    return result
def notToken(right_operand, all_operand):
    if right_operand in read_dict.keys():
        result = set(all_operand - read_dict[right_operand])
    else:
        result = all_operand
    return result

# def builtSentence(list_word):
#     new_built = ''
#     for item in list_word:
#         new_built = new_built + str(item) + ' '

# When simple_handling is processing, if it hit word likes '(', this function will be implemented
'''
main idea:
query: A and B or (D and (E or F) or G)
       return: (D and (E or F) or G)
'''
def getListInBracket(idx, listwords):
    sub_list = []
    weCount = 0
    for werun in range(idx, len(listwords)):
        if (listwords[werun] == "("): weCount+=1
        if (listwords[werun] == ")"):weCount-=1
        sub_list.append(listwords[werun])
        if (weCount == 0):
            return sub_list



def simple_handling(simple_query):
    #try:
        # split query into list
        list_words = simple_query.split()
        # stemmer each word in list
        list_words=[stemmer.stem(item) for item in list_words]
        # if list_word have only one element --> search for key A
        if (((len(list_words))==1)):
            if (list_words[0] in read_dict.keys()):
                final_result = read_dict[list_words[0]]

            else:
                final_result = set('')
        # if list_word have 2 elements --> not 'something' --> search for 'something' and invert the result
        elif ((len(list_words)) == 2 and (list_words[0] == 'not')):
            final_result = notToken(list_words[1], library)


        # if list_word have more than 2 elements --> check for the 1st element
        # main idea: to start a query, - A and B...
        #                              - not A and B...
        else:
            if (list_words[0] == 'not'):   #if start query is 'not'
                if(list_words[1] in read_dict.keys()):
                    result=notToken(read_dict[list_words[1]], library)
                else:
                    result=set('')
                list_words[0]=list_words[0]+list_words[1]
                del list_words[1]
                read_dict[list_words[0]]=result
            # else: for each couple of index and value in list_word:
            for idx, word in enumerate(list_words):
                if (word == 'or'):
                    if (list_words[idx + 1] == '('):        # if list_word[idx] = or and after or is '(' --> A, or, (B...)
                        sub_list = []                       # include word inside bracket
                        sub_list = getListInBracket(idx + 1, list_words)    # get all things inside bracket --> (B...)
                        sub_list.remove(sub_list[0])                        # }remove bracket in sub_list   -->  B...
                        sub_list.remove(sub_list[len(sub_list) - 1])        # }
                        sub_list_string = ' '.join(sub_list)                # --> 'B...'
                        sub_result = simple_handling(sub_list_string)       #
                        list_words_string = ' '.join(list_words)            # 'A or (B...)'
                        list_words_string = list_words_string.replace(sub_list_string, '')# delete sub_list in list_word
                        list_words = list_words_string.split()              # --> A, or, ()
                        if (idx + 2 < len(list_words)):
                            list_words.remove(list_words[idx + 2])          # --> A, or, (
                        list_words[idx + 1] = ''.join(sub_list)             # --> A, or, srt(sub_list)
                        read_dict[list_words[idx + 1]] = sub_result;        # add str(sub_list) as a new word into dictionary with value = simplehandling(sub_list)
                        result = orToken(list_words[idx - 1], list_words[idx + 1]) # or
                        list_words[idx + 1] = list_words[idx - 1] + list_words[idx + 1] # --> A, or, str(A+sub_list)
                        read_dict[list_words[idx + 1]] = result             # add str(A+sub_list) as a new word into dictionary with value=result of or token
                        simple_query = ' '.join(list_words)
                        return simple_handling(simple_query)


                    elif (list_words[idx + 1] == 'not'):
                        if (list_words[idx + 2] in read_dict.keys()):
                            result = notToken(list_words[idx + 2], library)
                        else:
                            result = library

                        list_words[idx + 1] = list_words[idx + 1]+list_words[idx + 2]
                        read_dict[list_words[idx + 1]]=result
                        final_result = orToken(list_words[idx - 1], list_words[idx + 1])
                        del list_words[idx + 2]
                        read_dict[list_words[idx + 1]]=final_result

                    else:
                        final_result = orToken(list_words[idx-1], list_words[idx+1])

                        list_words[idx + 1] = list_words[idx - 1] + list_words[idx + 1]
                        read_dict[list_words[idx + 1]] = final_result

                elif (word=='and'):
                    if (list_words[idx + 1] == '('):
                        sub_list=[]
                        sub_list = getListInBracket(idx + 1, list_words)
                        sub_list.remove(sub_list[0])
                        sub_list.remove(sub_list[len(sub_list) - 1])
                        sub_list_string = ' '.join(sub_list)
                        sub_result=set()
                        sub_result = simple_handling(sub_list_string)
                        list_words_string = ' '.join(list_words)
                        list_words_string=list_words_string.replace(sub_list_string, '')
                        list_words = list_words_string.split()
                        if (idx+2 < len(list_words)):
                            list_words.remove(list_words[idx + 2])
                        list_words[idx + 1] = ''.join(sub_list)
                        read_dict[list_words[idx + 1]] = sub_result;
                        result = andToken(list_words[idx - 1], list_words[idx + 1])
                        list_words[idx + 1] = list_words[idx - 1] + list_words[idx + 1]
                        read_dict[list_words[idx + 1]] = result
                        simple_query = ' '.join(list_words)
                        return simple_handling(simple_query)

                    elif (list_words[idx + 1] == 'not'):
                        if (list_words[idx + 2] in read_dict.keys()):
                            result = notToken(list_words[idx + 2], library)
                        else:
                            result = library

                        list_words[idx + 1] = list_words[idx + 1]+list_words[idx + 2]
                        read_dict[list_words[idx + 1]]=result
                        final_result = andToken(list_words[idx - 1], list_words[idx+1])
                        del list_words[idx + 2]
                        read_dict[list_words[idx + 1]]=final_result
                    else:
                        final_result = andToken(list_words[idx-1], list_words[idx+1])

                        list_words[idx + 1] = list_words[idx - 1] + list_words[idx + 1]
                        read_dict[list_words[idx + 1]] = (final_result);


        return final_result
    #except Exception:
        #pass


