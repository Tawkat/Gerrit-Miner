from Utilities.Log_Progessbar import show_progress


class Request_Table:
    def __init__(self,db):
        self.db=db

    def requestAttr(self,req):
        '''print("request_id,project_id, gerrit_id,gerrit_key,change_id owner, subject, status, project,branch,topic,starred,"
              " last_updated_on, sort_key, owner_name,owner_email,created,insertions, deletions")

        print(req['request_id'],req['project_id'],req['gerrit_id'],req['gerrit_key'],req['change_id'],req['owner'],
              req['subject'],req['status'],req['project'],req['branch'],req['topic'],req['starred'],
              req['last_update_on'],req['sort_key'],req['owner_name'],req['owner_email'],req['created'],
              req['insertions'],req['deletions'])'''

        self.db.saveReviewRequestList(req['request_id'],req['project_id'],req['gerrit_id'],req['gerrit_key'],
                                    req['change_id'],req['owner'],req['subject'],req['status'],req['project'],
                                    req['branch'],req['topic'],req['starred'],req['last_update_on'],req['sort_key'],
                                    req['owner_name'],req['owner_email'],req['created'],req['insertions'],req['deletions'])



    def printRequestList(self,reqList):
        self.reqList=reqList
        for i,req in enumerate(self.reqList,1):
            show_progress("Inserting Request Table", i, len(self.reqList))
            self.requestAttr(req)


    def prepRequest(self,changeDetailList):
        #print(self.changeDetailList)
        reqList=[]
        print('Preparing Request Table...')
        for changeDetail in changeDetailList:
            req = {}
            try:
                req['request_id'] = changeDetail['request_id']
            except:
                req['request_id'] = None
            try:
                req['project_id'] = changeDetail['projectDetail']['id']
            except:
                req['mergeable'] = None
            try:
                req['gerrit_id'] = changeDetail['_number']
            except:
                req['gerrit_id'] = None
            try:
                req['gerrit_key'] = changeDetail['id']
            except:
                req['gerrit_key'] = None
            try:
                req['change_id'] = changeDetail['change_id']
            except:
                req['change_id'] = None
            try:
                req['owner'] = changeDetail['owner']['_account_id']
            except:
                req['owner'] = None
            try:
                req['subject'] = changeDetail['subject']
            except:
                req['subject'] = None
            try:
                req['status'] = changeDetail['subject']
            except:
                req['status'] = None
            try:
                req['project'] = changeDetail['project']
            except:
                req['project'] = None
            try:
                req['branch'] = changeDetail['branch']
            except:
                req['branch'] = None
            try:
                req['topic'] = changeDetail['topic']
            except:
                req['topic'] = None

            req['starred'] = None

            try:
                req['last_update_on'] = changeDetail['updated']
            except:
                req['last_update_on'] = None

            req['sort_key'] = None

            try:
                req['owner_name'] = changeDetail['owner']['name']
            except:
                req['owner_name'] = None

            try:
                req['owner_email'] = changeDetail['owner']['email']
            except:
                req['owner_email'] = None

            try:
                req['created'] = changeDetail['created']
            except:
                req['created'] = None

            try:
                req['insertions'] = changeDetail['insertions']
            except:
                req['insertions'] = None

            try:
                req['deletions'] = changeDetail['deletions']
            except:
                req['deletions'] = None

            try:
                req['mergeable'] = changeDetail['mergeable']
            except:
                req['mergeable'] = None

            try:
                req['current_patch_id'] = changeDetail['current_revision']
            except:
                req['current_patch_id'] = None

            try:
                req['number_patches'] = len(changeDetail['revisions'])
            except:
                req['number_patches'] = None

            reqList.append(req)



        self.printRequestList(reqList)





