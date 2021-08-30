import pyperclip
import pyautogui as gui
import pandas as pd
import time


class AutoWhatsapp():
    def __init__(self) -> None:
        # input("Whatsapp Web penceresinin açık olduğundan eminseniz ENTER'a basınız.")
        self.start()

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
            screen = self.getSize()
            gui.click(button='left', x=(screen.width) - (screen.width *
                                                         625/10000), y=(screen.height) - (screen.height * 1/2), clicks=1)
            # print(gui.KEYBOARD_KEYS)
            gui.press('tab', presses=2, interval=0.025)
            # self.getSearchButton()

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

            time.sleep(0.5)
            messageText = self.getMessageText()
            pyperclip.copy(messageText)
            gui.hotkey('ctrl', 'v')
            gui.press('enter')
        else:
            pass

    def getMessageText(self):
        with open('message.txt', 'r', encoding='UTF-8') as file:
            text = ''.join(file.readlines())
        return text

    def getUsers(self):
        # TODO => Seperate with ';' not ','
        df = pd.read_csv('users.csv', sep=';')
        users = df.values.tolist()
        return users

    def getSearchButton(self):
        buttonLocation = gui.locateOnScreen('search-2.png')
        # buttonPoint = gui.center(buttonLocation)
        print(buttonLocation)
        # btnX, btnY = buttonPoint
        # print(btnX, btnY)

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


AutoWhatsapp()
