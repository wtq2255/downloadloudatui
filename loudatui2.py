# coding: utf-8

#####################################################
## 作者： witKernel
## 创始时间：2014-07-23

## 描述： 
##     下载 露大腿 网站图片
##     loudatui.py 升级版 

## 注意：
##    需要BeautifulSoup支持

#####################################################

import os, sys
import urllib2,urllib
from bs4 import BeautifulSoup

min_page = 184
max_page = 994

pwd = sys.path[0] + os.sep + "img" + os.sep # 设置图片存放路径为 当前文件夹下的img文件夹
if os.path.exists(pwd) == False: # 若img文件夹不存在 新建文件夹img
	os.makedirs(pwd)

for i in range(min_page, max_page + 1):
	url = "http://loudatui.com/items/" + str(i) + "/zoom" # 设置请求网址

	try:
		html = urllib2.urlopen(url) # 通过urllib2请求URL
		soup = BeautifulSoup(html)
		img = soup.find("img", { "class" : "img" })
		img_src = img.attrs["src"] # 取出img标签中src属性值，即获取图片URL
		img_data = urllib.urlopen(img_src) # 请求图片网址
		name = pwd + str(i) + ".jpg" # 设置图片路径即名称
		f = open(name, "wb") # 新建图片文件
		f.write(img_data.read()) #下载并保存图片
		f.close() # 关闭IO流
		print img_src 
		print (name + " Saved!")
	except Exception:
		pass
print "Download completed!"