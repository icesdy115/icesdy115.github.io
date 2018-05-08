#coding=utf-8
from xml.etree import ElementTree as ET
per=ET.parse('E:\\workspace\\autoTest\\testData\\searchExpression.xml')
p=per.findall('./searchExpression')

for oneper in p:
    for child in oneper.getchildren():
        test = child.text
        t1 = test.split(',')
        name = t1[0]
        passwd = t1[1]
        print(name,' ',passwd)
