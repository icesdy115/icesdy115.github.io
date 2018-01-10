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
    	<script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
		<script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
		<!-- 新 Bootstrap 核心 CSS 文件 -->
		<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
		<!-- 可选的Bootstrap主题文件（一般不用引入） -->
		<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
	    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <link href="default.css" rel="stylesheet">
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
