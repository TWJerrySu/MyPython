#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     29/11/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests,json

TOKEN = "eyug2ebt8x2ovd4ncs874lsorxghny2i35kknyilloz6djwcdi"
TWWPHPSESSID = "cf6d7dc1d942a9071178b6dd68bcfc08"
ID = "0932208479"
password = "870cd34387781acbb5e3c82097dead41"
debug = False

headers = {"X-XSRF-TOKEN":TOKEN,'Content-Type':"application/x-www-form-urlencoded"}
cookies = {"XSRF-TOKEN":TOKEN,"TWWPHPSESSID":TWWPHPSESSID,'lang':"zh_tw"}

class KKAPI:
    def query_sessid(self):
        url = "https://www.kkbox.com/play/"
        r = requests.get(url,stream=True)
        if debug:
            print r.cookies['TWWPHPSESSID']
        #global SEID
        SEID = r.cookies['TWWPHPSESSID']
        print "SessionID:%s" % SEID

    def query_all_my_music(self):
        url = "https://www.kkbox.com/play/api/cpl_get_playlist.php?type=all"
        r = requests.get(url,headers=headers,cookies=cookies)
        req = json.loads(r.text)
        if debug:
            print r.text
        assert req["status"] == 1,'Status:%s,Message:%s'%(req["status"],req["msg"])
        global playlist
        playlist = req['playlist_ver']
        print "Get playlist ID:%s"% playlist
        for i in  range(len(req["data"])):
            print "My music :" + str(i) + "." + req["data"][i]['name']
        return req

    def add_new_songbook(self,name):
        url = "https://www.kkbox.com/play/api/cpl_add_playlist.php"
        pay_load = {'playlist_ver':playlist,'playlist_name':name}
        r = requests.post(url,headers=headers,cookies=cookies,data=pay_load)
        if debug:
            print r.text
        req = json.loads(r.text)
        assert req["status"] == 1,'Status:%s,Message:%s'%(req["status"],req["msg"])
        id = req["data"]["id"]
        all_music = self.query_all_my_music()
        for i in range(len(all_music["data"])):
            if id == all_music["data"][i]["id"] and name == all_music["data"][i]["name"]:
                print "Verified Pass.Add %s is successful" % name
                break
        else:
            raise AssertionError("Verified Failed.Add failed")

    def login(self):
        url = "https://www.kkbox.com/play/api/login.php"
        pay_load = {'uid':ID,'pwd':password}
        r = requests.post(url,headers=headers,cookies=cookies,data=pay_load)
        if debug:
            print r.text
        if len(r.text) < 100:
            raise AssertionError("Login Failed")
        else:
            print "Login okay"

    def search(self,keyword):
        url = "https://www.kkbox.com/play/api/search.php?word=%s" % keyword

        r = requests.get(url,headers=headers,cookies=cookies)
        if debug:
            print r.text
        req = json.loads(r.text)
        assert req["status"] == 1,'Status:%s,Message:%s'%(req["status"],req["msg"])
        for a in range(len(req['albums'])):
            print "Search results:" + str(a) + "." + req['albums'][a]['album_name']

    def change_profile(self,name,des):
        url = "https://www.kkbox.com/play/api/mybox_profile_edit.php"
        pay_load = {"nickname":name,"intro":des}
        r = requests.post(url,headers=headers,cookies=cookies,data=pay_load)
        if debug:
            print r.text
        req = json.loads(r.text)
        assert req["status"] == 1,'Status:%s,Message:%s'%(req["status"],req["msg"])
        print req["msg"]

if __name__ == '__main__':
    k = KKAPI()
    k.login()
    k.query_all_my_music()
    k.change_profile('Jerry','Iamhere')
    k.query_sessid()
    k.add_new_songbook("books4")
    k.search('Armin')
