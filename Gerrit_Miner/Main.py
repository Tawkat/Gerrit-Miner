#Author: Md. Tawkat Islam Khondaker

from Controller import Controller

if __name__=='__main__':
    url=input('Enter Gerrit URL:(Default)[https://gerrit.iotivity.org/gerrit/]\n')
    username=input('Enter Username:(Default)[None]\n')
    password=input('Enter HTTP Password:(Default)[None]\n')

    controller = Controller(url,username,password)
    controller.execute()
