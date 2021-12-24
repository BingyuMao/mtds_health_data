import csv
#Read input csv file to a list
data = []
with open('outpatient_sample.csv') as file:
    readfile = csv.DictReader(file)
    for rows in readfile:
        data.append(rows)

def helper(pt,name,count={}):
    '''Helper method to count unique value in the data list
       Input: header of two columns, pt for key and name for value. Value is a set.
       Default count is blank dictionary, but can be a dictionary for more than one times.
       Output: a dictionary.
    '''
    countcopy = count.copy() #set can't be changed so copy it first
    for rows in data:
        if not rows[pt] in countcopy and rows[name] != '': #make sure blank str not add in the set
            countcopy[rows[pt]] = set() #use set to drop duplicate
            countcopy[rows[pt]].add(rows[name])
        elif rows[name] != '':
            countcopy[rows[pt]].add(rows[name])
            
    return countcopy

#Total visits
visit = helper('Patient_ID','Visit_ID')
tv = {}
for key in visit:
    tv[key] = len(visit[key])

#Total unique physicians seen (include primary, operating, and other)
phy = helper('Patient_ID','Primary_Physician')
phy2 = helper('Patient_ID','Operating_Physician',phy)
phy3 = helper('Patient_ID','Other_Physician',phy2)

tp = {}
for key in phy3:
    tp[key] = len(phy3[key])

#Total unique diagnosis
diag = helper('Patient_ID','ICD9_DGNS_CD_1')
diag2 = helper('Patient_ID','ICD9_DGNS_CD_2',diag)
diag3 = helper('Patient_ID','ICD9_DGNS_CD_3',diag2)
diag4 = helper('Patient_ID','ICD9_DGNS_CD_4',diag3)
diag5 = helper('Patient_ID','ICD9_DGNS_CD_5',diag4)
diag6 = helper('Patient_ID','ICD9_DGNS_CD_6',diag5)
diag7 = helper('Patient_ID','ICD9_DGNS_CD_7',diag6)
diag8 = helper('Patient_ID','ICD9_DGNS_CD_8',diag7)
diag9 = helper('Patient_ID','ICD9_DGNS_CD_9',diag8)
diag10 = helper('Patient_ID','ICD9_DGNS_CD_10',diag9)

td = {}
for key in diag10:
    td[key] = len(diag10[key])


def diaghelper(pt,name,count={}):
    '''Helper method for diagnosis, the difference between helper is make the value 
       be list not set, actually prepare for frequency so not drop duplicate.
       Input: header of two columns, pt for key and name for value. Value is a list.
       Default count is blank dictionary, but can be a dictionary for more than one times.
       Output: a dictionary. 
    '''
    for rows in data:
        if not rows[pt] in count and rows[name] != '':
            count[rows[pt]] = []
            count[rows[pt]].append(rows[name])
        elif rows[name] != '':
            count[rows[pt]].append(rows[name])
            
    return count

#Need another result for diagnosis to get frequency
fre = diaghelper('Patient_ID','ICD9_DGNS_CD_1')
fre2 = diaghelper('Patient_ID','ICD9_DGNS_CD_2',fre)
fre3 = diaghelper('Patient_ID','ICD9_DGNS_CD_3',fre2)
fre4 = diaghelper('Patient_ID','ICD9_DGNS_CD_4',fre3)
fre5 = diaghelper('Patient_ID','ICD9_DGNS_CD_5',fre4)
fre6 = diaghelper('Patient_ID','ICD9_DGNS_CD_6',fre5)
fre7 = diaghelper('Patient_ID','ICD9_DGNS_CD_7',fre6)
fre8 = diaghelper('Patient_ID','ICD9_DGNS_CD_8',fre7)
fre9 = diaghelper('Patient_ID','ICD9_DGNS_CD_9',fre8)
fre10 = diaghelper('Patient_ID','ICD9_DGNS_CD_10',fre9)

#Most frequent diagnosis
count = {} #create a dictionary with patient id be key and another dictionary be value
for key in fre10:
    count[key]={} #the value dictionary contains every diagnosis(key) and its frequency(value)
    for subkey in fre10[key]:
        count[key][subkey] = count[key].get(subkey,0) + 1

#Reverse key and value of the value dictionary to prepare for sort 
freq = {}
for key in count:
    freq[key] = {}
    for subkey in count[key]:
        change = count[key][subkey]
        freq[key][change]=count[key].get(change,subkey)

for key in freq:
    freq[key] = list(freq[key].items())
    freq[key].sort(reverse=True)
    freq[key] = freq[key][0][1]

#Create the final reault in a list, prepare for writting in output csv file
fdict = {} #First use dictionary to make sure every patient(key) has correct results(value)
for key in tv:
    fdict[key] = []
    fdict[key].append(tv[key])    
for key in tp:
    fdict[key].append(tp[key])    
for key in td:
    fdict[key].append(td[key])   
for key in freq:
    fdict[key].append(freq[key])

flist = []#Change the dictionary to list for writting
for key in fdict:
    sublist = []
    sublist.append(key)
    for subkey in fdict[key]:
        sublist.append(subkey)
    flist.append(sublist)
#Create a header for output
flist.insert(0,['Patient_ID','Total_Visits','Total_Physicians','Total_Diagnosis','Most_Freq_Diganosis'])
#Create the output file
with open("bmao_hw05.csv","w") as output:
    writer = csv.writer(output)
    writer.writerows(flist)