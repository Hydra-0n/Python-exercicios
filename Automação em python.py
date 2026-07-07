import pyautogui
import time

link = "https://www.youtube.com/"

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("backspace")

pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=469, y=151)

pyautogui.write("ich hasse kinder till lindemann")
time.sleep(1)
pyautogui.press("enter")

time.sleep(1)
pyautogui.click(x=194, y=367)



