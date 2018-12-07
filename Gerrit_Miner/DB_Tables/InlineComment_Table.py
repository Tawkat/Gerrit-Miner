from Utilities.Log_Progessbar import show_progress


class InlineComment_Table:
    def __init__(self,db):
        self.db=db

    def iComAttr(self,iCom):
        '''print("comment_id,request_id,in_reply_to,patchset_id,file_name,line_number,author_id,written_on,status,format,side,message,start_line,end_line,start_character,end_character")
        print(iCom['comment_id'],iCom['request_id'], iCom['in_reply_to'], iCom['patchset_id'],
                             iCom['file_name'],iCom['line_number'], iCom['author_id'],
                            iCom['written_on'], iCom['status'], iCom['side'],
                            iCom['message'], iCom['start_line'], iCom['end_line'],
                        iCom['start_character'], iCom['end_character'])'''

        self.db.inlineComments(iCom['comment_id'],iCom['request_id'], iCom['in_reply_to'], iCom['patchset_id'],
                                iCom['file_name'],iCom['line_number'], iCom['author_id'],
                                iCom['written_on'], iCom['status'], iCom['side'],
                                iCom['message'], iCom['start_line'], iCom['end_line'],
                                iCom['start_character'], iCom['end_character'])


    def printInlineCommentList(self,iComList):
        self.iComList=iComList
        for i,iCom in enumerate(self.iComList,1):
            show_progress("Inserting Inline Comment Table", i, len(self.iComList))
            self.iComAttr(iCom)


    def prepInlineComment(self,inlineCommentList):
        #print(self.inlineCommentList)
        iComList=[]
        print('Preparing InlineComments Table...')
        for inlineComment in inlineCommentList:
            #print(inlineComment)
            iCom = {}

            try:
                iCom['request_id'] = inlineComment['request_id']
            except:
                iCom['request_id'] = None
            try:
                iCom['comment_id'] = inlineComment['comment_id']
            except:
                iCom['comment_id'] = None
            try:
                iCom['in_reply_to'] = inlineComment['in_reply_to']
            except:
                iCom['in_reply_to'] = None
            try:
                iCom['patchset_id'] = inlineComment['patchset_id']
            except:
                iCom['patchset_id'] = None
            try:
                iCom['file_name'] = inlineComment['file_name']
            except:
                iCom['file_name'] = None
            try:
                iCom['line_number'] = inlineComment['line_number']
            except:
                iCom['line_number'] = None
            try:
                iCom['author_id'] = inlineComment['author_id']
            except:
                iCom['author_id'] = None
            try:
                iCom['written_on'] = inlineComment['written_on']
            except:
                iCom['written_on'] = None

            iCom['status'] = None

            try:
                iCom['side'] = inlineComment['side']
            except:
                iCom['side'] = None
            try:
                iCom['message'] = inlineComment['message']
            except:
                iCom['message'] = None
            try:
                iCom['start_line'] = inlineComment['start_line']
            except:
                iCom['start_line'] = None
            try:
                iCom['end_line'] = inlineComment['end_line']
            except:
                iCom['end_line'] = None
            try:
                iCom['start_character'] = inlineComment['start_character']
            except:
                iCom['start_character'] = None
            try:
                iCom['end_character'] = inlineComment['end_character']
            except:
                iCom['end_character'] = None

            iCom['sentiment_score'] = None

            iComList.append(iCom)



        self.printInlineCommentList(iComList)
