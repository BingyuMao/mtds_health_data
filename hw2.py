import os
try:
    folder = os.walk('./medline/')#walk thtough the folder
except IOError:
    print("This folder not exist!")
    
#create a list for all the text files
folderlist = []
for root, dirs, files in folder:
    for filename in files:
        if 'txt' in filename: #only use the text files
            folderlist.append(filename)


def freq(f):

    ''' 
    The function counts the number of word in a file and frequency of every word
    Input: a string contains all the elements in the file
    Output: a dictionary with words for keys and frequency for values   
    '''
    
    #Count number of words
    for char in '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~':
        f = f.replace(char,'~')  #replace special characters to '~'
    for num in '1234567890':
        f = f.replace(num,'~')   #replace numbers to '~'
    words = []
    for string in f.split():
        if '~' not in string:
            words.append(string)  #remain words not include '~'

    #count the number each word occurs and put them in a dictionary
    countf = {}
    for word in words:
        word = word.lower() 
        word = ''.join(word.split())
        #let the word be key and its frequency be value
        countf[word] = countf.get(word, 0) + 1 
    return countf


def top3(count):

    ''' 
    The function counts the top 3 frequenct words in a file
    Input: a dictionary with words for keys and frequency for values
    Output: a dictionary with the top 3 frequenct words in the file
    '''

    count = freq(f)

    #make the dictionary a list for sort
    freqc = list(count.items()) 
    freqc.sort(key=lambda letter:letter[1],reverse=True)

    #create a new dictionary for the top 3 words
    tops = {}
    for top in range(len(freqc)-1):
        #ensure the frequency number will not be the same
        if freqc[top][1] > freqc[top+1][1] and len(tops) < 3: 
            tops[freqc[top][0]] = freqc[top][1]
    return tops

#factorial part --add all the 3 words and their frequency in a list
top3s = []
for file in folderlist:
    f = open('./medline/'+ file).read()
    count = freq(f)
    tops = top3(count)
    top3s = top3s + list(tops.items())


#combine the repeated words and add their frequency
foldertop = {}
for word in top3s:
    if not word[0] in foldertop:
        foldertop[word[0]] = word[1]
    else:
        foldertop[word[0]] = foldertop[word[0]] + word[1]
#make the dictionary a list for sort
sfdl = list(foldertop.items())
sfdl.sort(key=lambda letter:letter[1],reverse=True)

#create a new dictionary for the top 3 words
top3 = {}
for top in range(len(sfdl)-1):
    #ensure the frequency number will not be the same
    if sfdl[top][1] > sfdl[top+1][1] and len(top3) < 3: 
        top3[sfdl[top][0]] = sfdl[top][1]
print(f'Top 3 words and their frequency for the entire folder: {top3}')