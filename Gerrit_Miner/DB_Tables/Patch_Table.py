from Utilities.Log_Progessbar import show_progress


class Patch_Table:
    def __init__(self,db):
        self.db=db

    def patchAttr(self,patch):
        '''print("request_id,revision,patchset_number,comment_count,subject,message,checkout,cherrypick,format,pull,author,committer,author_id,created,committed")
        print(patch['request_id'], patch['revision'], patch['patchset_number'],
                             patch['comment_count'],patch['subject'], patch['message'],
                            patch['checkout'], patch['cherrypick'], patch['format'],
                            patch['pull'], patch['author'], patch['committer'],
                        patch['author_id'], patch['created'], patch['committed'])'''

        self.db.patches(patch['request_id'], patch['revision'], patch['patchset_number'],
                             patch['comment_count'],patch['subject'], patch['message'],
                            patch['checkout'], patch['cherrypick'], patch['format'],
                            patch['pull'], patch['author'], patch['committer'],
                        patch['author_id'], patch['created'], patch['committed'])


    def printPatchList(self,patchList):
        self.patchList=patchList
        for i,patch in enumerate(self.patchList,1):
            show_progress("Inserting Patch Table", i, len(self.patchList))
            self.patchAttr(patch)


    def prepPatch(self,changeDetailList,comment_count):
        #print(self.changeDetailList)
        patchList=[]
        print('Preparing Patch Table...')
        for changeDetail in changeDetailList:
            try:
                for r in changeDetail['revisions'].keys():
                    patch={}

                    try:
                        patch['request_id'] = changeDetail['request_id']
                    except:
                        patch['request_id'] = None

                    try:
                        patch['revision'] = r
                    except:
                        patch['revision'] = None

                    try:
                        patch['patchset_number'] = changeDetail['revisions'][r]['_number']
                    except:
                        patch['patchset_number'] = None

                    try:
                        patch['comment_count'] = comment_count[r]
                    except:
                        patch['comment_count'] = None

                    try:
                        patch['subject'] = changeDetail['revisions'][r]['commit']['subject']
                    except:
                        patch['subject'] = None

                    try:
                        patch['message'] = changeDetail['revisions'][r]['commit']['message']
                    except:
                        patch['message'] = None

                    try:
                        patch['checkout'] = changeDetail['revisions'][r]['fetch']['http']['commands']['Checkout']
                    except:
                        patch['checkout'] = None

                    try:
                        patch['cherrypick'] = changeDetail['revisions'][r]['fetch']['http']['commands']['Cherry Pick']
                    except:
                        patch['cherrypick'] = None

                    try:
                        patch['format'] = changeDetail['revisions'][r]['fetch']['http']['commands']['Format Patch']
                    except:
                        patch['format'] = None

                    try:
                        patch['pull'] = changeDetail['revisions'][r]['fetch']['http']['commands']['Pull']
                    except:
                        patch['pull'] = None

                    try:
                        patch['author'] = changeDetail['revisions'][r]['commit']['author']['email']
                    except:
                        patch['author'] = None

                    try:
                        patch['committer'] = changeDetail['revisions'][r]['commit']['committer']['email']
                    except:
                        patch['committer'] = None

                    patch['author_id'] = None

                    try:
                        patch['created'] = changeDetail['revisions'][r]['commit']['author']['date']
                    except:
                        patch['created'] = None

                    try:
                        patch['committed'] = changeDetail['revisions'][r]['commit']['committer']['date']
                    except:
                        patch['committed'] = None

                    patchList.append(patch)

            except:
                continue


        self.printPatchList(patchList)
