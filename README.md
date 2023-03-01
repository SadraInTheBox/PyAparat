# PyAparat
a simple api for aparat.com


```py
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
```
