import pyautogui

pyautogui.FAILSAFE = False
 
procurar = "sim"

while procurar == "sim":
    try:
        pyautogui.FAILSAFE = False
        img = pyautogui.locateCenterOnScreen('claim.png', confidence=0.7)
        pyautogui.PAUSE = pyautogui.PAUSE = 0.00001
        pyautogui.click(img.x, img.y)
        procurar = "nao"
    
    except:
        print("sem claim")