import csv

class HWReader(object):

    def __init__(self, data):
        '''
        Define filename to read .csv file
        Read required .csv file, create a list to store data
        '''
        self.data = data
        with open(self.data, newline = "") as file:
            self.data = csv.DictReader(file)
            data = []
            for rows in self.data:
                data.append(rows)
            self.data = data
        

    def get_saps(self, ptID):
        '''
        Founction to get a SAPS-1 score of specific record
        Input: Record ID
        Output: SAPS-1 score
        '''       
        #Handle exceptions when non-string input occurs   
        if type(ptID) != str:
            print("Record ID need to be a string.")

        for rows in self.data:
            if rows["RecordID"] == ptID:
                return rows["SAPS-I"]
        
    def calc_avg(self, head, filter, logic, threshold):
        '''
        Founction to get average
        All of the numbers in the csv file are integers
        '''
        average = 0 
        averageList = []

        #Handle exceptions when non-string input occurs
        if type(head) != str or type(filter) != str or type(logic) != str or type(threshold) != str:
            print("All of the input parameters should be strings.")

        #A helper method to make the loop cleaner
        def InterHelper(i):
            #Handle exceptions when non integer occurs
            try:
                averageList.append(int(i))
            except:
                print("An error occurs.")

        for rows in self.data:
            #Make sure there are no negative integers occur
            if int(rows[head]) >= 0 and int(rows[filter]) >= 0:
                #Define different conditions get from parameter logic
                if logic == "lt" and int(rows[filter]) < int(threshold):
                    InterHelper(rows[head])
                elif logic == "gt" and int(rows[filter]) > int(threshold):
                    InterHelper(rows[head])
                elif logic == "lte" and int(rows[filter]) <= int(threshold):
                    InterHelper(rows[head])
                elif logic == "gte" and int(rows[filter]) >= int(threshold):
                    InterHelper(rows[head])

        average = sum(averageList) / len(averageList)
        return average