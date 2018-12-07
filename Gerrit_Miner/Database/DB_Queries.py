import pymysql.cursors
from Database.DB_Config import DB_Config


class DB_Queries:
    def __init__(self, host=DB_Config.host, user=DB_Config.user, password=DB_Config.password, db_name=DB_Config.db_name):
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          db=db_name,

                                          cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()

    def saveReviewer(self, gerrit_id, full_name, preferred_email, username, avatar):
        self.cursor. execute(
            "insert into people (gerrit_id,full_name,preferred_email,username,avatar) values(%s,%s,%s,%s,%s)",
            (gerrit_id, full_name, preferred_email, username, avatar))
        self.connection.commit()

    def saveReviewRequestList(self,request_id,project_id, gerrit_id,gerrit_key,change_id, owner, subject, status, project,
                                 branch,topic,starred, last_updated_on, sort_key, owner_name,owner_email,
                                 created,insertions, deletions):
        self.cursor. execute("INSERT INTO requests "
                                + "(request_id,project_id,gerrit_id,gerrit_key,change_id,owner,subject,"
                                + "status,project,branch,topic,starred,last_updated_on,sort_key,"
                                + "owner_name,owner_email,created,insertions,deletions) VALUES"
                                + "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (request_id,project_id, gerrit_id,gerrit_key,change_id, owner, subject, status, project,
                                 branch,topic,starred, last_updated_on, sort_key, owner_name,owner_email,
                                 created,insertions, deletions))
        self.connection.commit()

    def saveReviewRequestShortList(self, project_id, gerrit_id, gerrit_key, owner, sort_key):
        self.cursor. execute(
            "insert into requests_temp (project_id,gerrit_id,gerrit_key,owner,sort_key) values(%s,%s,%s,%s,%s)",
            (project_id, gerrit_id, gerrit_key, owner, sort_key))
        self.connection.commit()

    def saveDetailsRequest(self, request_id, gerrit_id, project, branch, topic, change_id, subject, status, created,
                           updated,
                           insertions, deletions, sort_key, mergeable, owner, number_patches, current_patch_id):
        self.cursor. execute("INSERT INTO request_detail ( request_id,gerrit_id,project,branch,topic,"
                                + "change_id,subject,status,created,updated,"
                                + "insertions,deletions,sort_key,mergeable,owner,"
                                + "number_patches,current_patch_id)"
                                + " VALUES ( %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)",
                                (request_id, gerrit_id, project, branch, topic, change_id, subject, status, created,
                                 updated,
                                 insertions, deletions, sort_key, mergeable, owner, number_patches, current_patch_id))
        self.connection.commit()

    def patches(self, request_id, revision, patchset_number, comment_count, subject, message, checkout, cherrypick,
                format, pull, author, committer, author_id, created, committed):
        self.cursor. execute("INSERT INTO patches ( " +
                                "request_id,revision,patchset_number," +
                                "comment_count,subject,message,checkout,cherrypick," +
                                "format,pull,author,committer,author_id,created,committed)" +
                                " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (request_id, revision, patchset_number, comment_count, subject, message, checkout,
                                 cherrypick,
                                 format, pull, author, committer, author_id, created, committed))
        self.connection.commit()

    def patchDetails(self, request_id, patchset_id, file_name, change_type, insertions, deletions):
        self.cursor. execute("INSERT INTO patch_details " +
                                "(request_id,patchset_id,file_name,change_type,insertions,deletions)" +
                                " VALUES (%s, %s, %s, %s, %s, %s)",
                                (request_id, patchset_id, file_name, change_type, insertions, deletions))
        self.connection.commit()

    def ReviewComments(self, request_id, message_id, patchset_id, author, created, message):
        self.cursor. execute("INSERT INTO review_comments " +
                                "(request_id,message_id,patchset_id,author,created,message)" +
                                " VALUES (%s,%s,%s,%s,%s,%s)",
                                (request_id, message_id, patchset_id, author, created, message))
        self.connection.commit()

    def Reviews(self, request_id, people_id, verified, reviewed, build):
        self.cursor. execute("INSERT INTO reviews " +
                                "(request_id,people_id,verified,reviewed,build) " +
                                "VALUES (%s,%s,%s,%s,%s)",
                                (request_id, people_id, verified, reviewed, build))
        self.connection.commit()

    def inlineComments(self, comment_id, request_id, in_reply_to, patchset_id, file_name, line_number, author_id,
                       written_on, status, side,
                       message, start_line, end_line, start_character, end_character):
        self.cursor. execute("INSERT INTO inline_comments " +
                                "(comment_id,request_id,in_reply_to,patchset_id,file_name," +
                                "line_number,author_id,written_on,status,side," +
                                "message,start_line,end_line,start_character,end_character) VALUES " +
                                "(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)",
                                (comment_id, request_id, in_reply_to, patchset_id, file_name, line_number, author_id,
                                 written_on, status, side, message, start_line, end_line, start_character,
                                 end_character))
        self.connection.commit()


    def fetchIdList(self):
        idList=[]
        self.cursor.execute("SELECT gerrit_key FROM requests")
        result= self.cursor.fetchall()
        for r in result:
           idList.append(r['gerrit_key'])
        print(idList)
        return idList

    def fetchChangeList(self):
        change=[]
        self.cursor.execute("SELECT request_id,gerrit_key,change_id FROM requests")
        result=self.cursor.fetchall()
        for r in result:
            c = {}
            c['id']=r['gerrit_key']
            c['request_id']=r['request_id']
            c['change_id']=r['change_id']
            change.append(c)

        return change



