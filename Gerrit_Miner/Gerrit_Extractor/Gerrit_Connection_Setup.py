import sys
from pygerrit2.rest import GerritRestAPI
from requests.auth import HTTPDigestAuth,HTTPBasicAuth

from Gerrit_Extractor.Gerrit_Queries import Gerrit_Queries


class Connection_Setup:

    def __init__(self,url,username,password):
        self.url=url
        self.gQ=Gerrit_Queries()

        if username=='' and password=='':
            self.auth=None
        else:
            self.username=username
            self.password=password

            self.auth = HTTPDigestAuth(self.username, self.password)


    def setConnection(self):

        try:
            self.rest = GerritRestAPI(url=self.url,auth=self.auth)  #############################################
            dummy = self.rest.get(self.gQ.testingQuery())

        except:
            try:
                if self.auth is not None:
                    self.auth = HTTPBasicAuth(self.username, self.password)
                self.rest = GerritRestAPI(url=self.url, auth=self.auth)
                dummy = self.rest.get(self.gQ.testingQuery())
            except:
                sys.exit('Authentication Failed!')

        return self.rest