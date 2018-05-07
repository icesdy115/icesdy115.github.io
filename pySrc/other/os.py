# coding=utf-8

import os
if os.getuid()==0:
    print('root')
else:
    print('not root')