from __future__ import print_function
import sys
import CreatingDictionary
import QueryProcessing
import re
import os
import glob

# storage file name
lst_file_name=set([])
boolean_operator = ['and','or','not','(', ')', '']

def create_doc_list():
    lst_file_name=CreatingDictionary.create_library()
    return lst_file_name

# intialize list to storage boolean value for each sub-query
def intialization_value_storage(sub_query):
    sub_query=[]
    return sub_query

# boolean processing
def check_exist(sub_query):
    doc_list = create_doc_list()
    itl = intialization_value_storage(sub_query)
    for item2 in doc_list:
         if item2 in QueryProcessing.simple_handling(sub_query):
            itl.append(1)
         else:
            itl.append(0)
    return itl

# create boolean table
def create_table(query):
    query = str(query).replace('(', '( ')
    query = query.replace(')', ' )')
    _query = query.split(" ")
    print('Doc ID:', end='\t\t     ')
    doc_list = create_doc_list()
    for idx, item in enumerate(doc_list):
        print(idx, end=' ')
    print('\n')
    for item in _query:
        if item in boolean_operator:
            continue
        print(item, end='')
        for i in range(21 - len(item)):
            print('-', end='')
        # print(QueryProcessing.simple_handling(item))
        for item2 in check_exist(item):
            print(item2, end=' ')
        print('\n')
