from DB_Tables.Comments_Table import Comment_Table
from DB_Tables.InlineComment_Table import InlineComment_Table
from DB_Tables.PatchDetail_Table import PatchDetail_Table
from DB_Tables.Patch_Table import Patch_Table
from DB_Tables.People_Table import People_Table
from DB_Tables.RequestDetail_Table import RequestDetail_Table
from DB_Tables.Request_Table import Request_Table
from DB_Tables.Reviews_Table import Reviews_Table
from Database.DB_Queries import DB_Queries
from Gerrit_Extractor.ReviewExtractor import ReviewExtractor


class Controller:

    def __init__(self, url='', username='', password=''):
        if url=='':
            url='https://gerrit.iotivity.org/gerrit/'
        self.url = url
        self.username = username
        self.password = password

        self.reviewExtractor=ReviewExtractor(self.url,self.username,self.password)

        self.db = DB_Queries()
        print('DB Connected Successfully')

        self.changeList = []
        self.changeDetailList = []
        self.commentCount = {}
        self.inlineCommentList = []

        self.rt = Request_Table(self.db)
        self.rDetail_Table = RequestDetail_Table(self.db)
        self.pt = People_Table(self.db)
        self.reviewsTable = Reviews_Table(self.db)
        self.ct = Comment_Table(self.db)
        self.iCom = InlineComment_Table(self.db)
        self.pDetailTable = PatchDetail_Table(self.db)
        self.patchTable = Patch_Table(self.db)


    def getProjectList(self):
        self.projectDict,self.projectNameList=self.reviewExtractor.getProjectList()

    def getAllChangeList(self):
        self.changeList=self.reviewExtractor.getAllChangeList(self.projectDict)

    def getChangeDetailList(self):
        self.changeDetailList=self.reviewExtractor.getChangeDetailList(self.changeList)

    def getTopic(self):
        self.changeDetailList=self.reviewExtractor.getTopic(self.changeDetailList)

    def getRevisions(self):
        self.changeDetailList = self.reviewExtractor.getRevisions(self.changeDetailList)

    def getReviewerList(self):
        changeList = self.db.fetchChangeList()
        self.reviewerList=self.reviewExtractor.getReviewerList(changeList)

    def getInlineComment(self):
        changeList = self.db.fetchChangeList()
        self.inlineCommentList, self.commentCount = self.reviewExtractor.getInlineComment(changeList)
        #print(self.inlineCommentList)


    def getPatchDetail(self):
        changeList = self.db.fetchChangeList()
        self.patchDetailList = self.reviewExtractor.getPatchDetail(changeList)
        #print(self.inlineCommentList)



    def extractAllInfo(self):
        self.getProjectList()
        self.getAllChangeList()
        self.getChangeDetailList()
        self.getTopic()
        self.getRevisions()
        self.getPatchDetail()
        self.getInlineComment()
        self.getReviewerList()



    def prepRequest(self):
        self.rt.prepRequest(self.changeDetailList)

    def prepRequestDetail(self):
        self.rDetail_Table.prepRequestDetail(self.changeDetailList)

    def prepComment(self):
        self.ct.prepComment(self.changeDetailList)

    def prepPeople(self):
        # print(self.reviewerList)
        self.pt.prepPeople(self.reviewerList)

    def prepReviews(self):
        # print(self.reviewerList)
        self.reviewsTable.prepReviews(self.reviewerList)

    def prepInlineComment(self):
        self.iCom.prepInlineComment(self.inlineCommentList)

    def prepPatchDetail(self):
        self.pDetailTable.prepPatchDetail(self.patchDetailList)

    def prepPatch(self):
        self.patchTable.prepPatch(self.patchDetailList, self.commentCount)




    def fillAllTable(self):
        self.prepRequest()
        self.prepRequestDetail()
        self.prepComment()
        self.prepInlineComment()
        self.prepPatchDetail()
        self.prepPatch()
        self.prepPeople()
        self.prepReviews()

    def execute(self):
        self.getProjectList()
        self.getAllChangeList()
        self.getChangeDetailList()
        self.getTopic()
        self.getRevisions()

        self.prepRequest()
        self.prepRequestDetail()
        self.prepComment()

        self.getInlineComment()

        self.prepInlineComment()


        self.getReviewerList()

        self.prepPeople()
        self.prepReviews()

        self.getPatchDetail()
        self.prepPatchDetail()
        self.prepPatch()




