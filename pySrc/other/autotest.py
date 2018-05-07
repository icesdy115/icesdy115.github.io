from selenium import webdriver
import time

def auto():
    b = webdriver.Chrome()
    b.get('http://www.baidu.com')
    time.sleep(3)
    b.close()

if __name__ == '__main__':
    auto()
