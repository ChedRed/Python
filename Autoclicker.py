import time
from pynput.mouse import Button, Controller
mouse = Controller()
while True:
    print("Input Function")
    func = input("")
    if func.lower() == "cpstest":
        print("Input CPS")
        cps = input("")
        print("Input Time")
        itme = input("")
        time.sleep(3)
        for i in range(int(cps) * int(itme)):
            time.sleep(0.1 / (int(cps) * int(itme)))
            mouse.click(Button.left, 1)