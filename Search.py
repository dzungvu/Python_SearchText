import QueryProcessing
import BooleanTable
import time
while True:
    # try:
        start = time.time()
        query1=input('Enter the query: ')
        query = QueryProcessing.rewrite_query(query1)
        if(query=='dz'):
            print('--------------------------end--------------------------')
            break
        result=QueryProcessing.simple_handling(query)
        if (len(result)==0):
            print('No file is matched')
        else:
            print(result)
            print('We found '+str(len(result)) + ' file(s)')
        BooleanTable.create_table(query)
        end = time.time()
        # print('Time execute: ', end='')
        print('Time execute: ' + str(end - start))
    # except Exception:
    #     print('Query is refused')
# youtube and facebook
# stay and husband and you
# gruse and think
# stay and husband and you and life and you
# stay and (husband and (you and life) and you)
# yes and general and bags
# stay and (husband and you and life) and you
# ((you and i) or not he)
# still and live or we and (girl or not boy and (link or sing) and never)