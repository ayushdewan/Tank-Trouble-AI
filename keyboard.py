import pyautogui, time

def shoot():
	pyautogui.keyDown("q")
	time.sleep(0.5)
	pyautogui.keyUp("q")
def right():
	pyautogui.keyDown("f")
	time.sleep(0.5)
	pyautogui.keyUp("f")
def left():
	pyautogui.keyDown("s")
	time.sleep(0.5)
	pyautogui.keyUp("s")
def forward():
	pyautogui.keyDown("e")
	time.sleep(0.1)
	pyautogui.keyUp("e")
def backward():
	pyautogui.keyDown("d")
	time.sleep(0.5)
	pyautogui.keyUp("d")
