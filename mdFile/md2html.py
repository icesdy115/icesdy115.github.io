# -*- coding: utf-8 

import markdown
import os
#import imp
import sys 
#imp.reload(sys)  
#sys.setdefaultencoding('utf8')

def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html>
    <head>
	<meta http-equiv="Content-Type" content="text/html; charset=GB2312" />
    <link href="default.css" rel="stylesheet">
    <link href="github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret



if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('usage: md2html source_filename target_file')
        sys.exit()

    infile = open(sys.argv[1],'r',encoding='utf-8')
    md = infile.read()
    infile.close()

    
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])


    outfile = open(sys.argv[2],'a')
    outfile.write(md2html(md))
    outfile.close()

    print('convert %s to %s success!'%(sys.argv[1],sys.argv[2]))