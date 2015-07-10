__author__ = 'user'
#-*- coding: utf-8 -*-

import wx
import io
import facebook
import json
import requests
import mechanize

class GUI (wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Manger",size=(400,300))
        panel=wx.Panel(self)
        buttonClose = wx.Button(panel, label="exit", pos=(50,50), size=(120,60))
        buttonSearch = wx.Button(panel, label="Search", pos=(220,50), size=(120,60))
        buttonGet = wx.Button(panel, label="Get", pos=(50,150), size=(120,60))
        self.Bind(wx.EVT_BUTTON, self.closeButton, buttonClose)
        self.Bind(wx.EVT_BUTTON, self.searchButton, buttonSearch)
        self.Bind(wx.EVT_BUTTON, self.getButton, buttonGet)

    def closeButton(self, event):
        self.Close(True)

    def searchButton(self, event):
        graph = facebook.GraphAPI(access_token='CAACEdEose0cBABQIC4Jmxu60ZAdn13exIyScgdGidURuLvYo1cribyARwhKc0z3kXmRZAalEwOmZCsWyKufLFkkWUoxeWTR2ylC8eTYqCKX9wl50CerHhTHn6MwMeMZBl99wliLvIcUXBn8ZBZCRu7x24JBq2cI4jYJxgpbWXOQ6qR7WCEyo30dzzPoW3CVSPRsBZAZBz8uS7MbTq1byt2SEsgwc62zXYKxWW2ZA7a1ccsgZDZD')
        memberList = graph.get_connections(id='/v2.0/697169560399276', connection_name='members', limit=1000,)
        with io.open('C:\Users\user\Desktop\members.txt', 'w', encoding='utf-8') as f1:
            strMemberList = unicode(json.dumps(memberList, ensure_ascii=False, indent=1))
            f1.write(strMemberList)
        f1.close()
        with io.open('C:\Users\user\Desktop\members.txt', 'r', encoding='utf-8') as f2:
            strMemberInfo = f2.read()
        f2.close()
        memberInfo = json.loads(strMemberInfo.encode("utf-8"))
        for i in range(0,len(memberInfo['data'])):
            print memberInfo['data'][i]['id']

    def getButton(self, event):
            br = mechanize.Browser()
            br.set_handle_robots(False)
            response = br.open("https://www.facebook.com/app_scoped_user_id/387082924764362/")
            print response.read()

if __name__=='__main__':
    app = wx.PySimpleApp()
    frame = GUI(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
