from pywinauto import mouse, keyboard
from pywinauto.application import Application
from time import sleep

pickup_line = "Hello I am a human! How are you fellow human?!"
swipes = 100
app = Application(backend="win32").start("/Program Files/Google/Chrome/Application/chrome.exe")
sleep(1)
keyboard.send_keys("{VK_LWIN down}{VK_UP}{VK_LWIN up}")
sleep(2)
mouse.click(button="left", coords=(1188, 56))
sleep(1)
keyboard.send_keys("tinder.com")
sleep(1)
keyboard.send_keys("{ENTER}")
sleep(1)
mouse.click(button="left", coords=(1830, 110))
sleep(1)
mouse.click(button="left", coords=(1057, 471))
sleep(1)
mouse.click(button="left", coords=(821, 565))
sleep(5)


# ---------------- Swipe motion ---------------- #
for i in range(1, swipes):
    mouse.click(button="left", coords=(1301, 211))
    mouse.press(button="left", coords=(1301, 211))
    mouse.release(button="left", coords=(1515, 207))


# --------------- Messages any new matches ----- #
for i in range(1, 10):
    mouse.click(button="left", coords=(55, 167))
    mouse.click(button="left", coords=(184, 265))
    keyboard.send_keys(pickup_line)

mouse.click(button="left", coords=(1888, 13))
