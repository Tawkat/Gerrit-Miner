
class Gerrit_Queries:

    def testingQuery(self):
        query="/changes/?" + "n=" + str(1)
        return query

    def projectListQuery(self):
        query="/projects/"
        return query

    def changeByProjectQuery(self,projectName):
        #query = "/changes/?q=after:2018-10-22+before:2018-10-23"   ##### Query to extract updated changes within a time interval.
        query = "/changes/?q=after:2016-09-31+project:" + str(projectName)
        return query

    def changeDetailQuery(self,id):
        query="/changes/" + str(id) + "/detail"
        return query

    def topicQuery(self,id):
        query="/changes/" + str(id) + "/topic"
        return query

    def revisionsQuery(self,id):
        query="/changes/" + str(id)
        query+="?o=ALL_REVISIONS"
        return query

    def reqParamsQuery(self,id):
        query="/changes/" + str(id)
        query+="?o=ALL_REVISIONS&o=CURRENT_REVISION&o=CURRENT_COMMIT&o=CURRENT_FILES&o=DOWNLOAD_COMMANDS"
        return query

    def inlineCommentQuery(self,id,patchset):
        query="/changes/" + str(id) + "/revisions/" + str(patchset) + "/comments/"
        return query

    def reviewersQuery(self,id):
        query="/changes/" + str(id) + "/reviewers"
        return query
