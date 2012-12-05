#!/usr/bin/env python2
#-*- mode: python -*-
#-*-coding: utf-8 -*-
from grab import Grab, error
import re, json


class VK(Grab):
    def __init__(self, aid, email, passwd):
        Grab.__init__(self, hammer_mode = True, hammer_timeouts = ((2,5), (10, 15), (20, 45)))
        self.aid = aid
        self.email = email
        self.passwd = passwd
        self.auth_app()
        
    def _check_code(self, fun = None, err = None):
        if self.response.code != 200:
            return err
        else:
            return fun

    def _check_response(self, fun = None):
        vk_res = json.loads(self.response.body)
        if vk_res.has_key(u"error") and vk_res[u"error"] == 5:
                self.auth_app()
        return fun != None and fun(vk_res) or vk_res
            
    def auth_app(self):
        self.go("https://oauth.vk.com/authorize?client_id=%d&scope=audio&redirect_uri=http://oauth.vk.com/blank.html&display=popup&response_type=token" % self.aid)
        self._check_code(self._auth_form, self.auth_app)()

    def _auth_form(self):
        self.choose_form(xpath = "//form")
        self.set_input("email", self.email)
        self.set_input('pass', self.passwd)
        self.submit()
        self._check_code(fun = self._get_tocken, err = self._auth_form)()

    def _get_tocken(self):
        self.tocken = re.search("access_token=([^&]+).+", self.response.head ).group(1)
    
    def call(self, vk_fun, **args):
        qstring = "access_token=%s&%s" % (self.tocken, "&".join(["%s=%s" % (k,v) for k, v in args.items()]))
        self.go("https://api.vk.com/method/%s?%s" % (vk_fun, qstring))
        return  self._check_code(fun = self._check_response)()
                
    def get_user_songs(self, uid):
        return self.call("audio.get", uid = uid)
        

if __name__ == "__main__":
    vk = VK(0, 'your@email', 'passwd')
    print vk.get_user_songs(12345)
