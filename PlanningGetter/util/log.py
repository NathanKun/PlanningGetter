'''
Created on 2 août 2017

@author: lenglingx, Junyang HE
@referrence: http://ju.outofmemory.cn/entry/259338 - python3使用logging日志记录
'''
# coding:utf-8
import logging
logger = logging.getLogger('eServiceCrawler')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('eServiceCrawler.log')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

def setDebug():
    logger.removeHandler(ch)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)