from Utilities.Log_Progessbar import show_progress


class RequestDetail_Table:
    def __init__(self,db):
        self.db=db

    def requestDetailAttr(self,rDetail):
        '''print("'requestDetail_id,project_id,gerrit_id,gerrit_key,owner,subject,status,project,branch,topic,starred,"
              "last_update_on,sort_key,owner_name,owner_email,created,insertions,deletions")
        print(rDetail['request_id'],rDetail['gerrit_id'],rDetail['project'],rDetail['branch'],rDetail['topic'],
              rDetail['change_id'],rDetail['subject'],rDetail['status'],rDetail['created'],rDetail['last_update_on'],
              rDetail['insertions'],rDetail['deletions'],rDetail['sort_key'],rDetail['mergeable'],
              rDetail['owner'],rDetail['number_patches'],rDetail['current_patch_id'])'''

        self.db.saveDetailsRequest ( rDetail['request_id'],rDetail['gerrit_id'],rDetail['project'],rDetail['branch'],
                                     rDetail['topic'],rDetail['change_id'],rDetail['subject'],rDetail['status'],
                                     rDetail['created'],rDetail['last_update_on'],rDetail['insertions'],
                                     rDetail['deletions'],rDetail['sort_key'],rDetail['mergeable'],
                                     rDetail['owner'],rDetail['number_patches'],rDetail['current_patch_id'])



    def printRequestDetailList(self,reqList):
        self.reqList=reqList
        for i,rDetail in enumerate(self.reqList,1):
            show_progress("Inserting Request Detail Table", i, len(self.reqList))
            self.requestDetailAttr(rDetail)


    def prepRequestDetail(self,changeDetailList):
        #print(self.changeDetailList)
        reqList=[]
        print('Preparing Request Detail Table...')
        for changeDetail in changeDetailList:
            rDetail = {}
            try:
                rDetail['request_id'] = changeDetail['request_id']
            except:
                rDetail['request_id'] = None
            try:
                rDetail['project_id'] = changeDetail['projectDetail']['id']
            except:
                rDetail['mergeable'] = None
            try:
                rDetail['gerrit_id'] = changeDetail['_number']
            except:
                rDetail['gerrit_id'] = None
            try:
                rDetail['gerrit_key'] = changeDetail['id']
            except:
                rDetail['gerrit_key'] = None
            try:
                rDetail['change_id'] = changeDetail['change_id']
            except:
                rDetail['change_id'] = None
            try:
                rDetail['owner'] = changeDetail['owner']['_account_id']
            except:
                rDetail['owner'] = None
            try:
                rDetail['subject'] = changeDetail['subject']
            except:
                rDetail['subject'] = None
            try:
                rDetail['status'] = changeDetail['subject']
            except:
                rDetail['status'] = None
            try:
                rDetail['project'] = changeDetail['project']
            except:
                rDetail['project'] = None
            try:
                rDetail['branch'] = changeDetail['branch']
            except:
                rDetail['branch'] = None
            try:
                rDetail['topic'] = changeDetail['topic']
            except:
                rDetail['topic'] = None

            rDetail['starred'] = None

            try:
                rDetail['last_update_on'] = changeDetail['updated']
            except:
                rDetail['last_update_on'] = None

            rDetail['sort_key'] = None

            try:
                rDetail['owner_name'] = changeDetail['owner']['name']
            except:
                rDetail['owner_name'] = None

            try:
                rDetail['owner_email'] = changeDetail['owner']['email']
            except:
                rDetail['owner_email'] = None

            try:
                rDetail['created'] = changeDetail['created']
            except:
                rDetail['created'] = None

            try:
                rDetail['insertions'] = changeDetail['insertions']
            except:
                rDetail['insertions'] = None

            try:
                rDetail['deletions'] = changeDetail['deletions']
            except:
                rDetail['deletions'] = None

            try:
                rDetail['mergeable'] = changeDetail['mergeable']
            except:
                rDetail['mergeable'] = None

            try:
                rDetail['current_patch_id'] = changeDetail['current_revision']
            except:
                rDetail['current_patch_id'] = None

            try:
                rDetail['number_patches'] = len(changeDetail['revisions'])
            except:
                rDetail['number_patches'] = None

            reqList.append(rDetail)



        self.printRequestDetailList(reqList)





