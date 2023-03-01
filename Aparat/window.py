from pygame import (
	display, image, init, time,
	transform
)
init()
from pygame.font import Font, init
init()
from pygame.event import get as get_ev
from pygame import *
import sys
from .request import Aparat, req
url = "https://www.aparat.com/etc/api/profile/username/"


font = Font("./Aparat/font.fon", 100)

words = "abcdefghijklmnopqrstuvwxyz"
words += words.upper()
words += "1234567890.!@#$%^&*()_-=+`~/\\[]{}>?<"

def UserNameInput():
	win = display.set_mode((400, 400))
	display.set_caption("who are you?")
	username = ""

	open_ = True
	text = font.render("type your aparat id > ", True, (0, 0, 2))

	enter_t = font.render("next", True, (0,0,0))
	enter_r = Rect(
		5,
		win.get_height()-5-enter_t.get_height(),
		100,
		50
	)

	while open_:
		win.fill((255, 255, 255))

		usTxt = font.render(username, True, (0,0,0))

		win.blit(enter_t, enter_r)
		win.blit(text, (5, 5))
		win.blit(usTxt, 
			(
				5,
				text.get_height()+5
			)
		)

		for event in get_ev():
			if event.type == QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.unicode in words:
					username += event.unicode
				elif event.key == K_BACKSPACE:
					username = username[:-1]
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if enter_r.collidepoint(event.pos):
						open_ = False
						win.fill((0, 0, 255))

		display.update()

	with req.get(url+username) as res:
		if res.status_code != 200:
			username = UserNameInput()

	return username


class Window:
	followers = 0
	followeds = 0
	username = None
	def __init__(self, **kawargs):
		user = Aparat(UserNameInput())
		self.username = user.username
		self.user = user
	async def update(self, followers:int, followeds:int):
		self.followers = followers
		self.followeds = followeds

	async def show(self):
		w, h = 700, 300
		window = display.set_mode((w, h))
		display.set_caption(f"aparat.com/{self.username}")

		c = 0

		self.followers = self.user.followers()
		self.followeds = self.user.followeds()
		avatar = self.user.avatar()

		while True:
			c+=1
			if c == 2000:
				c = 0
				self.folowers = self.user.followers()
				self.foloweds = self.user.followeds()
				#avatar = self.user.avatar()
			window.fill((255, 255, 255))

			window.blit(
				avatar,
				(
					window.get_width()-avatar.get_width()-5,
					5
				)
			)

			followers = font.render(
				"followers : "+str(self.followers),
				True, (0, 0, 0)
			)
			followers = transform.scale(
				followers,
				(
					followers.get_width()*2,
					followers.get_height()*2
				)
			)
			followeds = font.render(
				"followings : "+str(self.followeds),
				True, (0, 0, 0)
			)
			followeds = transform.scale(
				followeds,
				(
					followeds.get_width()*2,
					followeds.get_height()*2
				)
			)

			window.blit(followeds, (5, 5))
			window.blit(followers, (5, followers.get_height()+5))

			for event in get_ev():
				if event.type == QUIT:
					sys.exit()

			display.flip()
			display.update()
			clock = time.Clock()
			clock.tick(clock.get_fps())