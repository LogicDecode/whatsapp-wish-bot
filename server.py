from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

Link = "https://web.whatsapp.com/"
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=./User_Data')
browser = webdriver.Chrome(
    'chromedriver/chromedriver.exe', options=chrome_options)
browser.get(Link)
time.sleep(10)

names = []
with open('names.txt') as namesfile:
    for name in namesfile:
        names.append(name.rstrip())

pyautogui.press(['tab', 'tab', 'tab'])


def send_message(name):
    time.sleep(2)
    search_bar = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    search_bar.click()
    browser.execute_script('''
    document.querySelector("#side > div._2EoyP > div > label > div > div._3FRCZ.copyable-text.selectable-text").innerText = '';
    ''')
    pyautogui.write(name)
    time.sleep(2)
    user = browser.find_element_by_xpath(
        '//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    msg_box.click()
    pyautogui.write(
        'Hey {}, Wishing you and your family, a very very Happy Diwali!! Be safe and happy'.format(name.split()[0]))
    button = browser.find_element_by_xpath(
        '//span[@data-icon="send"]')
    button.click()


for name in names:
    send_message(name)
