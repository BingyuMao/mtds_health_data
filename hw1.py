#The first function to count words
def wordcount(file):
    try:
        f = open('./medline/'+ file).read()
    except IOError:
        print("This file not exist!")
    
    #Count number of words includes numbers and special characters
    sp = f.split()     #split with space
    allcount = len(sp) #just count words, do not care for numbers and special characters
    print(f"Words include numbers and special characters: {allcount}")
    
    #Count number of words
    for char in '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~':
        f = f.replace(char,'~')  #replace special characters to '~'
    for num in '1234567890':
        f = f.replace(num,'~')   #replace numbers to '~'
    word = []
    for string in f.split():
        if '~' not in string:
            word.append(string)  #remain words not include '~'
    #count English words
    count = len(word) 
    print(f"English words: {count}")
    return word


#The second funcation to count frequency
def freq(file):
    try:
        open('./medline/'+ file).read()
    except IOError:
        print("This file not exist!")
    
    wordlist = wordcount(file) #use the result from last funcation

    #count the number each word occurs and put them in a dictionary
    countf = {}
    for word in wordlist:
        word = word.lower() 
        word = ''.join(word.split())
        #let the word be key and its frequency be value
        countf[word] = countf.get(word, 0) + 1 
    
    freqc = list(countf.items()) #make the dictionary a list
    freqc.sort(key=lambda letter:letter[1],reverse=True) #sort the list reversely
    print(f"The most frequency word is {freqc[0][0]}, its frequency is {freqc[0][1]}")
    return freqc[0]


freq('19771122.txt')
