#coding=utf-8
from grab import grab
import logging

logging.basicConfig(level = logging.DEBUG)

g = Grab()
g.go('https://github.com/login')
g.set_input('login','wangxu831217@hotmail.com')
g.set_input('password','!QAZ2wsx')
g.submit()
g.doc.save('/tmp/x.html')

g.doc('//span[contains(@class, "octicon-sign-out")]').assert_exists()
home_url = g.doc('//a[contains(@class, "header-nav-link name")]/@href').text()
repo_url = home_url + '?tab=repositories'

g.go(repo_url)
for elem in g.doc.select('//h3[@class="repo-list-name"]/a'):
    print('%s: %s' % (elem.text(),
                      g.make_url_absolute(elem.attr('href'))))
