# coding: utf-8

#####################################################
## 作者： witKernel
## 创始时间：2014-07-23

## 描述： 
##     下载 露大腿 网站图片

## 注意：
##    需要BeautifulSoup支持

#####################################################

import os, sys
import urllib2,urllib
from bs4 import BeautifulSoup

url = 'http://loudatui.com?page=' # 设置请求网址
page = 12 # 设置下载图片页数（每页25张图片）

pwd = sys.path[0] + os.sep + "img" + os.sep # 设置图片存放路径为 当前文件夹下的img文件夹
if os.path.exists(pwd) == False: # 若img文件夹不存在 新建文件夹img
	os.makedirs(pwd)

for i in range(page):
	html = urllib2.urlopen(url + str(i)) # 通过urllib2请求URL

	soup = BeautifulSoup(html) # 对请求的HTML页面进行BeautifulSoup处理
	img = soup.select("img.img") # 获取HTML页面中img标签
	img_length = len(img) # 获取img标签数量


	for j in range(img_length): # 对img标签进行遍历
		img_src = img[j].attrs["src"] # 取出img标签中src属性值，即获取图片URL
		img_src = img_src[:-5] + "large" # 将下载的图片设为大图，此处"large"，可修改为"small"、"middle"
		img_data = urllib.urlopen(img_src) # 请求图片网址
		name = pwd + str(j+i*25) + ".jpg" # 设置图片路径即名称
		f = open(name, "wb") # 新建图片文件
		f.write(img_data.read()) #下载并保存图片
		f.close() # 关闭IO流
		print img_src 
		print (str(j+i*25) + " Saved!")

print "Download completed!"
