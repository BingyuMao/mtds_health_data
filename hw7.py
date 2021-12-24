import requests

def medline(drug):
    '''Method to get drug name and url from MedlinePlus webpage
       Input: drug name as a string
       Output: a string contains the drug name and the url to get it in MedlinPlus
    '''
    #Handle exceptions may occur
    if type(drug) != str:
        print('Drug name must be a string!')
    
    #Get RXCUI by drug name for MedlinePlus search use
    try:
        rx_endpoint = 'https://rxnav.nlm.nih.gov/REST/rxclass'
        rx_resource = '/class/byDrugName.json'
        para = {'drugName' : drug, 'relaSource' : 'ATC'}
        rx = requests.get(rx_endpoint + rx_resource, params=para)
    except:
        print('An error occurs when getting RxCUI code of the drug.')
        
    #Load the json data for processing    
    rxcui = rx.json()
    #Choose the right RxCUI code for the drug    
    for items in range(len(rxcui['rxclassDrugInfoList']['rxclassDrugInfo'])):
        if rxcui['rxclassDrugInfoList']['rxclassDrugInfo'][items]['minConcept']['name'] == drug.lower():
            rx_code = rxcui['rxclassDrugInfoList']['rxclassDrugInfo'][items]['minConcept']['rxcui']
    
    #Get MdelinePlus URL using RxCUI code
    try:
        base_url = 'https://connect.medlineplus.gov/service'
        #Parameter information: the first is request using RxCUI code, the second is the actual code
        #and the last request MedlinPlus to give data back as a JSON.
        #Information get from https://medlineplus.gov/connect/service.html
        param = {'mainSearchCriteria.v.cs' : '2.16.840.1.113883.6.88', 'mainSearchCriteria.v.c' : rx_code, 'knowledgeResponseType' : 'application/json'}
        #To avoid InsecureRequestWarning or any other warnings in the output
        requests.packages.urllib3.disable_warnings()
        r = requests.get(base_url, params = param, verify = False)
    except:
        print('An error occurs when request from MedlinePlus.')
    
    #Load data as a dictionary
    data = r.json()
    #Get the URL of the drug
    href = data['feed']['entry'][0]['link'][0]['href']#a string contains the url
    hreflist = href.split('?') #only need the part before "?"
    output = drug + ' - ' + hreflist[0] #define the output
    
    return output

print(medline('Metformin'))
print(medline('Aspirin'))
print(medline('Escitalopram'))