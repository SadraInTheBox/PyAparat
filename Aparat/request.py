import requests as req
import json, sys, os
import threading as th
from pygame import image
from wget import download

class Aparat:
	def __init__(self, username:str):
		self.username = username
		url = "https://www.aparat.com/etc/api/profile/username/"+self.username
		res = req.get(url)
		if len(str(res.text)) <= 70:
			sys.exit()

	def followers(self):
		url = "https://www.aparat.com/etc/api/profile/username/"+self.username
		with req.get(url) as res:
			data = json.loads(str(res.text))
		return data["profile"]["follower_cnt"]

	def followeds(self):
		url = "https://www.aparat.com/etc/api/profile/username/"+self.username
		with req.get(url) as res:
			data = json.loads(str(res.text))
		return data["profile"]["followed_cnt"]

	def avatar(self):
		url = "https://www.aparat.com/etc/api/profile/username/"+self.username
		with req.get(url) as res:
			data = json.loads(str(res.text))
		avatar = data["profile"]["pic_b"]
		try:
			os.remove("./Aparat/avatar.png")
		except:pass
		download(avatar, "./Aparat/avatar.png")
		surface = image.load("./Aparat/avatar.png")
		return surface