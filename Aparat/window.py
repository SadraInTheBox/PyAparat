from pygame import (
	display, image, init, time,
	transform
)
init()
from pygame.font import Font, init
init()
from pygame.event import get as get_ev
from pygame import QUIT
import sys
from .request import Aparat

font = Font("./Aparat/font.fon", 100)

class Window:
	folowers = 0
	foloweds = 0
	username = None
	def __init__(self, user:Aparat):
		self.username = user.username
		self.user = user
	async def update(self, folowers:int, foloweds:int):
		self.folowers = folowers
		self.foloweds = foloweds

	async def show(self):
		w, h = 700, 300
		window = display.set_mode((w, h))
		display.set_caption(f"aparat.com/{self.username}")

		c = 0

		while True:
			c+=1
			if c == 2000:
				c = 0
				self.folowers = self.user.folowers()
				self.foloweds = self.user.foloweds()
			window.fill((255, 255, 255))

			folowers = font.render(
				"folowers : "+str(self.folowers),
				True, (0, 0, 0)
			)
			folowers = transform.scale(
				folowers,
				(
					folowers.get_width()*2,
					folowers.get_height()*2
				)
			)
			foloweds = font.render(
				"foloweds : "+str(self.foloweds),
				True, (0, 0, 0)
			)
			foloweds = transform.scale(
				foloweds,
				(
					foloweds.get_width()*2,
					foloweds.get_height()*2
				)
			)

			window.blit(foloweds, (5, 5))
			window.blit(folowers, (5, folowers.get_height()+10))

			for event in get_ev():
				if event.type == QUIT:
					sys.exit()

			display.flip()
			display.update()
			clock = time.Clock()
			clock.tick(clock.get_fps())