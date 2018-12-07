
from Gerrit_Extractor.Gerrit_Connection_Setup import Connection_Setup
from Gerrit_Extractor.Gerrit_Queries import Gerrit_Queries

from Utilities.Log_Progessbar import show_progress


class ReviewExtractor:
    def __init__(self, url, username,password):
        self.url = url
        self.username = username
        self.password = password

        self.con=Connection_Setup(url=self.url,username=self.username,password=self.password)
        self.rest=self.con.setConnection()
        print('Gerrit Connection Established Successfully.')

        self.gQ=Gerrit_Queries()


    def getProjectList(self):
        print("Project List Extracting...")
        projectDict = self.rest.get(self.gQ.projectListQuery())
        projectNameList = list(projectDict.keys())
        return projectDict,projectNameList

    def changesPerProject(self, projectName):
        changes = self.rest.get(self.gQ.changeByProjectQuery(projectName))
        return changes
        # print(change)

    def getAllChangeList(self,projectDict):
        changeList=[]
        for i, project in enumerate(list(projectDict.keys()), 1):
            show_progress("Change List Extraction from Project List", i, len(projectDict.keys()))

            changes = self.changesPerProject(project)
            if (len(changes) != 0):
                # print("i: " + str(i))
                for change in changes:
                    if (len(change) != 0):
                        try:
                            # print(projectDict[project])
                            change['projectDetail'] = projectDict[project]
                        except:
                            continue
                        else:
                            changeList.append(change)
        return changeList

    def getChangeDetailList(self,changeList):
        changeDetailList=[]
        for k,change in enumerate(changeList,1):
            show_progress("Change Detail Extraction", k, len(changeList))
            try:
                changeDetail = self.rest.get(self.gQ.changeDetailQuery(change['id']))
            except:
                continue
            else:
                changeDetail['projectDetail'] = change['projectDetail']
                changeDetailList.append(changeDetail)
                for i, change in enumerate(changeDetailList, 1):
                    change['request_id'] = i

        return changeDetailList

    def getTopic(self,changeDetailList):
        for i,change in enumerate(changeDetailList,1):
            show_progress("Topic Extraction", i, len(changeDetailList))
            try:
                topic = self.rest.get(self.gQ.topicQuery(change['id']))
            except:
                print("Exception: Topic Extraction Failed!")
                topic = None
            finally:
                change['topic'] = topic

        return changeDetailList

    def getRevisions(self,changeDetailList):
        for i,change in enumerate(changeDetailList,1):
            show_progress("Revisions Extraction from Change List", i, len(changeDetailList))
            try:

                patchCount = self.rest.get(self.gQ.revisionsQuery(change['id']))

            except:
                print("Exception: Required Parameters Extraction Failed!")
                if 'current_revision' not in patchCount.keys():
                    patchCount['current_revision'] = None
                if 'revisions' not in patchCount.keys():
                    patchCount['revisions'] = None
            finally:
                change['current_revision'] = patchCount['current_revision']
                change['revisions'] = patchCount['revisions']

        return changeDetailList



    def getPatchDetail(self,changeList):
        patchDetail=[]
        for i,change in enumerate(changeList,1):
            show_progress("Required Revisions Extraction from Change List", i, len(changeList))
            try:

                detail = self.rest.get(self.gQ.reqParamsQuery(change['id']))

            except:
                print("Exception: Required Parameters for Patch Detail Extraction Failed!")
                if 'current_revision' not in detail.keys():
                    detail['current_revision'] = None
                if 'revisions' not in detail.keys():
                    detail['revisions'] = None
            finally:
                detail['request_id'] = change['request_id']
                patchDetail.append(detail)

        return patchDetail


    def getReviewerList(self,changeList):
        reviewerList = []
        for i,change in enumerate(changeList,1):
            show_progress("Reviewers Info Extraction from Change List", i, len(changeList))
            try:
                reviewers = self.rest.get(self.gQ.reviewersQuery(change['id']))
            except:
                print("Exception: Reviewers Info Extraction Failed!")
            else:
                if (len(reviewers) != 0):
                    for reviewer in reviewers:
                        reviewer['change_id'] = change['change_id']
                        reviewer['request_id'] = change['request_id']
                    reviewerList.append(reviewers)

        return reviewerList



    def getInlineComment(self,changeList):
        #cnt = 0
        inlineCommentList=[]
        commentCount={}

        for k,cIter in enumerate(changeList,1):
            show_progress("Inline Comment Extraction from Change List", k, len(changeList))
            try:
                change = self.rest.get(self.gQ.revisionsQuery(cIter['id']))
                #print(change)
                for r in change['revisions'].keys():
                    try:
                        patchset = change['revisions'][r]['_number']
                        commentCount[str(r)] = 0

                        try:
                            commentFile = self.rest.get(self.gQ.inlineCommentQuery(cIter['id'],patchset))
                            for file in commentFile.keys():
                                commentList = commentFile[file]

                                for i,comment in enumerate(commentList,1):
                                    #cnt += 1
                                    #show_progress("Inline Comment No:" str(cnt))

                                    commentCount[str(r)] += 1
                                    inlineComment = {}

                                    try:
                                        inlineComment['request_id'] = cIter['request_id']
                                    except:
                                        inlineComment['request_id'] = None
                                    try:
                                        inlineComment['comment_id'] = comment['id']
                                    except:
                                        inlineComment['comment_id'] = None
                                    try:
                                        inlineComment['in_reply_to'] = comment['in_reply_to']
                                    except:
                                        inlineComment['in_reply_to'] = None
                                    try:
                                        inlineComment['patchset_id'] = change['revisions'][r]['_number']
                                    except:
                                        inlineComment['patchset_id'] = None
                                    try:
                                        inlineComment['file_name'] = file
                                    except:
                                        inlineComment['file_name'] = None
                                    try:
                                        inlineComment['line_number'] = comment['line']
                                    except:
                                        inlineComment['line_number'] = None
                                    try:
                                        inlineComment['author_id'] = comment['author']['_account_id']
                                    except:
                                        inlineComment['author_id'] = None
                                    try:
                                        inlineComment['written_on'] = comment['updated']
                                    except:
                                        inlineComment['written_on'] = None

                                    inlineComment['status'] = None

                                    try:
                                        inlineComment['side'] = comment['side']
                                    except:
                                        inlineComment['side'] = None
                                    try:
                                        inlineComment['message'] = comment['message']
                                    except:
                                        inlineComment['message'] = None
                                    try:
                                        inlineComment['start_line'] = comment['range']['start_line']
                                    except:
                                        inlineComment['start_line'] = None
                                    try:
                                        inlineComment['end_line'] = comment['range']['end_line']
                                    except:
                                        inlineComment['end_line'] = None
                                    try:
                                        inlineComment['start_character'] = comment['range']['start_character']
                                    except:
                                        inlineComment['start_character'] = None
                                    try:
                                        inlineComment['end_character'] = comment['range']['end_character']
                                    except:
                                        inlineComment['end_character'] = None

                                    inlineComment['sentiment_score'] = None

                                    inlineCommentList.append(inlineComment)


                        except:
                            print("Exception: " + "Commented file Extraction Failed!")
                            continue
                    except:
                        print("Exception: " + "patchset key not found!")
                        continue
            except:
                print("Exception: " + "revisions key not found!")
                continue

        return inlineCommentList,commentCount
