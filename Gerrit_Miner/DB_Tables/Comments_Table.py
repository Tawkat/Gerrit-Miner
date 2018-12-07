from Utilities.Log_Progessbar import show_progress


class Comment_Table:
    def __init__(self,db):
        self.db=db

    def commentAttr(self,com):
        '''print("request_id,message_id,patchset_id,author,created,message,sentiment_score")
        print(com['request_id'],com['message_id'],com['patchset_id'],com['author'],com['created'],
              com['message'],com['sentiment_score'])'''

        self.db.ReviewComments(com['request_id'],com['message_id'],com['patchset_id'],com['author'],com['created'],
              com['message'])

    def printCommentList(self,comList):
        self.comList=comList
        for i,com in enumerate(self.comList,1):
            show_progress("Inserting Review Comment Table",i,len(self.comList))
            self.commentAttr(com)


    def prepComment(self,changeDetailList):
        #print(self.changeDetailList)
        comList=[]
        print('Preparing Review Comments Table...')
        for changeDetail in changeDetailList:
            if "messages" not in changeDetail.keys():
                continue
            for messages in changeDetail['messages']:
                com = {}

                try:
                    com['request_id'] = changeDetail['request_id']
                except:
                    com['request_id'] = None

                try:
                    com['message_id'] = messages['id']
                except:
                    com['message_id'] = None

                try:
                    com['author'] = messages['author']['_account_id']
                except:
                    com['author'] = None

                try:
                    com['created'] = messages['date']
                except:
                    com['message_id'] = None

                try:
                    com['message'] = messages['message']
                except:
                    com['message'] = None

                com['sentiment_score'] = None

                try:
                    com['patchset_id'] = messages['_revision_number']
                except:
                    com['patchset_id'] = None

                comList.append(com)


        self.printCommentList(comList)





