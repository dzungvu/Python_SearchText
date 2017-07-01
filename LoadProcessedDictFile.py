def LoadDictFile(link):
    f = open(link, 'r')
    dicRam = {'':set([])}
    while True:
        line = f.readline()
        if (line == ''):
            print('Load dictionary successful')
            break
        else:
            ram = line.split('{')
            ram[1].replace('}', '')
            ram[1].split(',')

