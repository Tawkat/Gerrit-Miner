from Utilities.Log_Progessbar import show_progress


class PatchDetail_Table:
    def __init__(self,db):
        self.db=db

    def patchDetailAttr(self,pDetail):
        '''print("request_id,patchset_id,file_name,change_type,insertions,deletions")
        print(pDetail['request_id'], pDetail['patchset_id'], pDetail['file_name'],
                             pDetail['change_type'],pDetail['inserted'], pDetail['deleted'])'''

        self.db.patchDetails(pDetail['request_id'], pDetail['patchset_id'], pDetail['file_name'],
                             pDetail['change_type'],pDetail['inserted'], pDetail['deleted'])

    def printPatchDetailList(self,pDetailList):
        self.pDetailList=pDetailList
        for i,pDetail in enumerate(self.pDetailList,1):
            show_progress("Inserting Patch Detail Table", i, len(self.pDetailList))
            self.patchDetailAttr(pDetail)


    def prepPatchDetail(self,changeDetailList):
        #print(self.changeDetailList)
        pDetailList=[]
        print('Preparing Patch Detail Table...')
        for changeDetail in changeDetailList:
            try:
                for r in changeDetail['revisions'].keys():
                    try:
                        for f in changeDetail['revisions'][r]['files'].keys():
                            pDetail = {}

                            try:
                                pDetail['request_id'] = changeDetail['request_id']
                            except:
                                pDetail['request_id'] = None

                            try:
                                pDetail['patchset_id'] = changeDetail['revisions'][r]['_number']
                            except:
                                pDetail['patchset_id'] = None

                            try:
                                pDetail['file_name'] = f
                            except:
                                pDetail['file_name'] = None

                            try:
                                pDetail['change_type'] = changeDetail['revisions'][r]['files'][f]['status']
                            except:
                                pDetail['change_type'] = 'M'

                            try:
                                pDetail['inserted'] = changeDetail['revisions'][r]['files'][f]['lines_inserted']
                            except:
                                pDetail['inserted'] = None

                            try:
                                pDetail['deleted'] = changeDetail['revisions'][r]['files'][f]['lines_deleted']
                            except:
                                pDetail['deleted'] = None

                            pDetailList.append(pDetail)

                    except:
                        continue

            except:
                continue


        self.printPatchDetailList(pDetailList)
