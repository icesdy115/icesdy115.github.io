#coding=utf-8
import pychrome

br = pychrome.Browser(url="http://127.0.0.1:9222")
tabs = br.list_tab()

if not tabs :  
    tab = br.new_tab()
else:
    tab = tabs[0]

def request_will_sent(**kwargs):
    print ("loading...:%s" % kwargs.get('request').get('url'))

tab.set_listener("Network.requestWillBeSent", request_will_sent)

tab.call_method("Network.enable")
tab.call_method("Page.navigate", url="http://www.innojoy.com", _timeout=5)

tab.wait(5)

tab.stop()

br.close_tab(tab)