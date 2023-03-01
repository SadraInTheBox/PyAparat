import requests as req
import json, sys
import threading as th

class Aparat:
	def __init__(self, username:str):
		self.username = username
		url = "https://www.aparat.com/etc/api/profile/username/"+self.username
		res = req.get(url)
		if len(str(res.text)) <= 70:
			sys.exit()

	def folowers(self):
		url = "https://www.aparat.com/etc/api/profile/username/"+self.username
		with req.get(url) as res:
			data = json.loads(str(res.text))
		return data["profile"]["follower_cnt"]

	def foloweds(self):
		url = "https://www.aparat.com/etc/api/profile/username/"+self.username
		with req.get(url) as res:
			data = json.loads(str(res.text))
		return data["profile"]["followed_cnt"]