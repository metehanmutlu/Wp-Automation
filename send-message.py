import os
import pyperclip
import pyautogui as gui
import pandas as pd
import time


class AutoWhatsapp():
    def __init__(self) -> None:
        # input("Whatsapp Web penceresinin açık olduğundan eminseniz ENTER'a basınız.")
        pass

    def start(self):
        self.showWhatsappWindow()

        if not self.isActiveWindow('whatsapp'):
            input(
                'Whatsapp Web penceresinin açık olduğundan emin olup tekrardan çalıştırınız.')
        else:
            self.findUsersAndSendMessages()

    def findUsersAndSendMessages(self):
        users = self.getUsers()
        for user in users:
            btnX, btnY = self.getSearchButton()
            gui.click(button='left', x=btnX, y=btnY, clicks=1)

            name = str(user[0])
            number = str(user[1])
            time.sleep(1)
            if number == 'nan' and name == 'nan':
                continue

            if number == 'nan':
                pyperclip.copy(name)
                gui.hotkey('ctrl', 'v')
                gui.press('enter')

            elif name == 'nan':
                pyperclip.copy(str(int(float(number))))
                gui.hotkey('ctrl', 'v')
                gui.press('enter')

            else:
                pyperclip.copy(name)
                gui.hotkey('ctrl', 'v')
                gui.press('enter')

                self.sendMessage()      
        else:
            pass

    def sendMessage(self):
        time.sleep(0.5)
        messageText = self.getMessageText()
        pyperclip.copy(messageText)
        gui.hotkey('ctrl', 'v')
        gui.press('enter')

    def getMessageText(self):
        path = os.path.dirname(os.path.realpath(__file__))
        path += '/message.txt'
        with open(path, 'r', encoding='UTF-8') as file:
            text = ''.join(file.readlines())
        return text

    def getUsers(self):
        # TODO => Seperate with ';' not ','
        path = os.path.dirname(os.path.realpath(__file__))
        path += '/users.csv'
        df = pd.read_csv(path, sep=';')
        users = df.values.tolist()
        return users

    def getSearchButton(self):
        time.sleep(1)
        path = os.path.dirname(os.path.realpath(__file__))
        path += '/search-2.png'
        buttonLocation = gui.locateOnScreen(path)
        buttonPoint = gui.center(buttonLocation)
        # print(buttonPoint)
        return buttonPoint.x, buttonPoint.y

    def showWhatsappWindow(self):
        for title in gui.getAllTitles():
            if 'whatsapp' in title.lower():
                activeWindow = gui.getActiveWindow()
                whatsapp = gui.getWindowsWithTitle(title)[0]
                activeWindow.minimize()
                whatsapp.minimize()
                whatsapp.maximize()
                break

    def isActiveWindow(self, title: str):
        activeTitle = gui.getActiveWindow().title.lower()
        title = title.lower()
        if title in activeTitle:
            return True
        else:
            return False

    def getPosition(self):
        time.sleep(2)
        return gui.position()

    def getSize(self):
        time.sleep(2)
        return gui.size()


AutoWhatsapp().start()