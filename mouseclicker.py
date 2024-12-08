import pynput.mouse as ms
import keyboard

while True:
	while keyboard.is_pressed('|') != True:
		ms.Events