from Utilities.Log_Progessbar import show_progress


class People_Table:
    def __init__(self,db):
        self.db=db
        self.peopleDict={}


    def peopleAttr(self,people):
        '''print("gerrit_id,full_name,preferred_email,username,avatar")
        print(people['gerrit_id'],people['full_name'],people['preferred_email'],people['username'],
              people['avatar'])'''
        self.db.saveReviewer(people['gerrit_id'], people['full_name'], people['preferred_email'], people['username'],
              people['avatar'])

    def printpeopleList(self):
        for i,people in enumerate(set(self.peopleDict.keys()),1):
            show_progress("Inserting People Table", i, len(set(self.peopleDict.keys())))
            self.peopleAttr(self.peopleDict[people])


    def prepPeople(self,reviewerList):
        print('Preparing People Table...')
        for peoples in reviewerList:
            for people in peoples:
                #print(people)
                key = people['_account_id']
                #print(key)
                self.peopleDict[key] = {}

                try:
                    self.peopleDict[key]['gerrit_id'] = people['_account_id']
                except:
                    self.peopleDict[key]['gerrit_id'] = None

                try:
                    self.peopleDict[key]['full_name'] = people['name']
                except:
                    self.peopleDict[key]['full_name'] = None

                try:
                    self.peopleDict[key]['preferred_email'] = people['email']
                except:
                    self.peopleDict[key]['preferred_email'] = None

                try:
                    self.peopleDict[key]['username'] = people['username']
                except:
                    self.peopleDict[key]['username'] = None

                try:
                    self.peopleDict[key]['avatar'] = people['avatar'][0]['url']
                except:
                    self.peopleDict[key]['avatar'] = None


        self.printpeopleList()






