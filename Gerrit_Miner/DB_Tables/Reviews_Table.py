from Utilities.Log_Progessbar import show_progress


class Reviews_Table:
    def __init__(self,db):
        self.db=db
        self.reviewsList=[]

    def reviewAttr(self,review):
        '''print("request_id,people_id,verified,reviewed,build")
        print(review['request_id'],review['people_id'],review['verified'],
              review['reviewed'],review['build'])'''
        self.db.Reviews(review['request_id'],review['people_id'],review['verified'],
              review['reviewed'],review['build'])

    def printReviewsList(self):
        for i,review in enumerate(self.reviewsList,1):
            show_progress("Inserting Reviews Table", i, len(self.reviewsList))
            self.reviewAttr(review)


    def prepReviews(self,reviewerList):
        print('Preparing Reviews Table...')
        for reviews in reviewerList:
                for r in reviews:
                    #print(r)
                    review={}

                    try:
                        review['request_id'] = r['request_id']
                    except:
                        review['request_id']=None

                    try:
                        review['people_id'] = r['_account_id']
                    except:
                        review['request_id']=None

                    try:
                        review['verified'] = r['approvals']['Verified']
                    except:
                        review['verified']=None

                    try:
                        review['reviewed'] = r['approvals']['Code-Review']
                    except:
                        review['reviewed']=None

                    try:
                        review['build'] = r['approvals']['Build-Status']
                    except:
                        review['build'] = None

                    self.reviewsList.append(review)


        self.printReviewsList()






