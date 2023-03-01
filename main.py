from Aparat import Aparat, Window
import asyncio

window = Window()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(window.show())