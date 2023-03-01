from Aparat import Aparat, Window
import asyncio

username = input("username > ")
user = Aparat(username)
window = Window(user)
#try:
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(window.show())
#except:
#	pass