import keyboard as keys
import pyautogui as gui
xPos = 0
yPos = 0
isGrounded = False
extraJump = 0
gravity = 0
horizontalAcceleration = 0
while True:
    print(xPos,",",yPos)


    if keys.read_key() == "space":
        if isGrounded == True:
            gravity += 5
        else:
          if extraJump == 1:
            gravity += 7.5
        if yPos <= 0:
            gravity = 0
        yPos = 0
        isGrounded = True
    else:
        isGrounded = True



    if keys.read_key() == "d":
        if not keys.read_key() == "a":
            horizontalAcceleration += 0.5
    if keys.read_key() == "a":
        if not keys.read_key() == "d":
            horizontalAcceleration += -0.5
    if not keys.read_key() == "a":
        if not keys.read_key() == "d":
            horizontalAcceleration *= 0.75
    if keys.read_key() == "a":
        if keys.read_key() == "d":
            horizontalAcceleration *= 0.75
    xPos += horizontalAcceleration
    yPos += gravity
    
