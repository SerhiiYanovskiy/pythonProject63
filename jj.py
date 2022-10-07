import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import os
import telepot


token = '5720753247:AAGPI7Au8FOgTKQ1PnlDO-1jMfPKi-UYv-I' # telegram token
receiver_id = 544723767 # https://api.telegram.org/bot<TOKEN>/getUpdates
bot = telepot.Bot(token)



sername_list = []
name_list = []
def solved_normal_capcha():
    captcha_img = browser.find_element(By.XPATH,
                                       value='/html/body/div[8]/div[2]/div[2]/img')
    captcha_img.screenshot(r'D:\Users7\Roman\Desktop\zhd_tikets\solver_captcha\captcha.png')
    api_key = os.getenv('APIKEY_2CAPTCHA',
                        
                      )

    solver = TwoCaptcha(api_key)

    try:
        result = solver.normal(r'D:\Users7\Roman\Desktop\zhd_tikets\solver_captcha\captcha.png')

    except Exception as e:
        print(e)

    else:
        code = result["code"]

        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                         '/html/body/div[8]/div[2]/div[2]/input')))
        browser.find_element(By.XPATH,
                             '/html/body/div[8]/div[2]/div[2]/input').send_keys(code)
        time.sleep(1)

        browser.find_element(By.XPATH,
                             "/html/body/div[8]/div[2]/div[3]/button").click()
        time.sleep(1)



email = "dscsdvafvafdvasfvasva@gmail.com"
password = "Gfhjkm12@"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1800,1000")
browser = webdriver.Chrome(executable_path=r"D:\Users7\Roman\Desktop\zhd_tikets\chromedriver.exe",
                           options=options)
browser.get('https://booking.uz.gov.ua/authorization/')
time.sleep(1)
browser.find_element(by=By.XPATH,
                             value='/html/body/div[2]/div/form/input').send_keys(email)
browser.find_element(by=By.XPATH,
                             value="/html/body/div[2]/div/form/div[2]/input").send_keys(password)
browser.find_element(by=By.XPATH,
                             value="/html/body/div[2]/div/form/div[4]/button").click()
time.sleep(1)



with open("data_1.txt", encoding="utf-8") as file:
    i = 0
    for string in file:
        i+=1
        i_1 = i + 1
        browser.execute_script(f"window.open('https://booking.uz.gov.ua/', "
                               f"{i} );")
        time.sleep(1)
        try:
            from_data = string.split(":")[0]
            to_data = string.split(":")[1]
            date_data = string.split(":")[2]
            sername = string.split(":")[3]
            name = string.split(":")[4]


        except IndexError:
            continue
        sername_list.append(sername)
        if name == 0:
            name_list.append("")
        else:
            name_list.append(name)
        browser.switch_to.window(browser.window_handles[i])
        browser.find_element(by=By.XPATH,
                             value="/html/body/div[2]/div[1]/form/div[2]/div[1]/div[1]/input").send_keys(from_data)
        time.sleep(1.5)
        pyautogui.press(['down', 'enter'])
        browser.find_element(by=By.XPATH,
                             value="/html/body/div[2]/div[1]/form/div[2]/div[1]/div[2]/input").send_keys(to_data)
        time.sleep(1)
        pyautogui.press(['down', 'enter'])

        browser.find_element(by=By.XPATH,
                                       value='/html/body/div[2]/div[1]/form/div[2]/div[2]/div[1]/input[2]').click()
        time.sleep(2)

        browser.find_element(by=By.CSS_SELECTOR,
                             value=f'[aria-label="{date_data}"]').click()
        time.sleep(3)




        browser.find_element(by=By.XPATH,
                             value="/html/body/div[2]/div[1]/form/div[3]/div/button").click()
        time.sleep(1)
        try:
            solved_normal_capcha()
        except:
            continue
    n = 0
    m = 0
    list_pages = browser.window_handles
    list_pages.pop(0)
    while True:
        for page in list_pages:
            browser.switch_to.window(page)
            time.sleep(1)

            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[1]/form/div[3]/div/button").click()
                time.sleep(3)
            except:
                m +=1
                continue
            try:
                solved_normal_capcha()
            except:
                print("1")

            m = 0
            time.sleep(1)
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[3]/section/table/tbody/tr[2]/td[6]/div/div[3]/input").click()

            except:
                try:
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[3]/section/table/tbody/tr[3]/td[6]/div[1]/div[3]/input").click()
                except:
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[4]/section/table/tbody/tr[1]/td[6]/div[2]/div[3]/input").click()
                    except:
                        continue



            time.sleep(3)
            try:
                browser.find_element(by=By.CSS_SELECTOR,
                                     value='[class="place fr"]').click()
            except:
                try:
                    browser.find_element(by=By.CSS_SELECTOR,
                                         value='[class="up place fr"]').click()
                except:
                    try:
                        browser.find_element(by=By.CSS_SELECTOR,
                                         value='[class="down place fr"]').click()
                    except:

                        try:
                            browser.find_element(by=By.CSS_SELECTOR,
                                                 value='[class="headrest headrest-left place fr"]').click()
                        except:
                            try:
                                browser.find_element(by=By.CSS_SELECTOR,
                                                     value='[class="headrest headrest-right place fr"]').click()
                            except:
                                continue
            time.sleep(1)
            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[4]/section/div[11]/input").click()
            time.sleep(2)
            browser.find_element(by=By.CSS_SELECTOR,
                                         value='[name="lastname"]').clear()

            browser.find_element(by=By.CSS_SELECTOR,
                                         value='[name="lastname"]').send_keys(sername_list[n])


            browser.find_element(by=By.CSS_SELECTOR,
                                 value='[name="firstname"]').clear()
            browser.find_element(by=By.CSS_SELECTOR,
                                 value='[name="firstname"]').send_keys(name_list[n])
            browser.find_element(by=By.CSS_SELECTOR,
                                 value='[name="firstname"]').click()
            time.sleep(1)
            browser.find_element(by=By.XPATH,
                                 value = "/html/body/div[2]/div[5]/div/div[9]/div[2]/input").click()

            try:
                time.sleep(1)
                solved_normal_capcha()
            except:
                print("")
            bot.sendMessage(receiver_id, f'ticket found {browser.current_url}')
            n+=1


    "dscsdvafvafdvasfvasva@gmail.com"
    "Gfhjkm12@"














