from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from threading import Thread, Event
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import string
import random
import sys
import os

from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    FIRST_EXCEPTION,
)

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "sp"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


def load_data(start_data, end_data):

    script_dir = os.path.dirname(os.path.realpath("__file__"))
    data_file = os.path.join(script_dir, "x.csv")

    data_account = []

    with open(data_file) as csv_data_file:
        data_account = list(csv.reader(csv_data_file, delimiter=","))

    data_account = data_account[int(start_data) : int(end_data)]

    return data_account


def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920, 1200")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def run_bot(data_account, recover=1):
    kw = data_account[0]

    driver = web_driver()
    driver.maximize_window()

    try:

        
        username =  kw.replace(" ", "-")
        fix_username = username+'_leaked_v'+random_string(4)

        judul =f'{kw} Leaked Video onlyfans' 

        kalimat = kw
        kata_pertama = kalimat.split()[0]


        driver = web_driver()
        driver.maximize_window()

        driver.get("https://fex.plus/en")
        time.sleep(4)

        email = driver.find_element(By.CSS_SELECTOR, 'h3.name').text
        password = 'tESUEB@WUB77sh'

        time.sleep(2)
        driver.get("https://www.spatial.io/")
        time.sleep(4)

        driver.find_element(By.XPATH, '//*[@id="headerNav"]/div/div[2]/div/div/button[2]/div').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/div/div[2]/button[3]').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/form/label/div[2]/input').send_keys(email)
        time.sleep(1)

        driver.find_element(By.XPATH, ' //*[@id="radix-:rf:"]/div/div/span/div/div/form/button').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/form/label/input').send_keys(password)
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/form/button').click()
        time.sleep(10)

        driver.get("https://fex.plus/en/")
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, '.mail.row.no-gutters.new').click()
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        link_konfimasi = driver.find_element(By.CSS_SELECTOR, "td[align='center'] div a u").find_element(By.XPATH, "..").get_attribute("href")
        time.sleep(1)
        driver.get(link_konfimasi)

        time.sleep(3)

        # login akun

        driver.get("https://www.spatial.io/")

        time.sleep(4)

        driver.find_element(By.XPATH, '//*[@id="headerNav"]/div/div[2]/div/div/button[2]/div').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/div/div[2]/button[3]').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/form/label/div[2]/input').send_keys(email)
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/form/button').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/form/label/div[2]/input').send_keys(password)
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="radix-:rf:"]/div/div/span/div/div/form/button').click()
        time.sleep(15)

        # set username
        driver.find_element(By.XPATH, '//*[@id="username"]').clear()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(fix_username)
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="terms"]').click()
        time.sleep(2)

        driver.execute_script('document.querySelector("button.w-full").click()')
        time.sleep(4)


        driver.execute_script('document.querySelector("button.border-white").click()')

        time.sleep(2)

       
        driver.get(f"https://www.spatial.io/@{fix_username}")
        time.sleep(20)

        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div[2]/div[1]/button').click()
        time.sleep(2)


        input_element2 = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Name"]')

        # Pilih semua teks dan hapus
        input_element2.send_keys(Keys.CONTROL + 'a')  
        time.sleep(2)
        input_element2.send_keys(Keys.BACKSPACE) 

        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Name"]').send_keys(judul)
        time.sleep(2)
        

        konten = f'Click on the (Website) Icon 🌐 ➜➜➜  TOP RIGHT CORNER ... Get {kw} Leaked OF All Files Updated.'


        textarea = driver.find_element(By.CSS_SELECTOR, 'textarea.w-full.grow.bg-transparent.text-sm')

        # Buat ActionChains
        actions = ActionChains(driver)

        actions.move_to_element(textarea).click().send_keys(konten).perform()

        time.sleep(5)
        lp =f'https://clipsfans.site/{kata_pertama}'
        driver.find_element(By.CSS_SELECTOR,'input.w-full[placeholder="https://website.com"]').send_keys(lp)
   
        button ='button[type="submit"]'
        driver.execute_script(f"document.querySelector('{button}').click()")
        time.sleep(2)


        response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": driver.current_url})
            .execute()
        )

        time.sleep(5)

        print(f"SUKSES CREATE: {kw}", file=sys.__stderr__)

        time.sleep(5)
        driver.close()
    except Exception as e:
        if recover == 0:
            print(
                f"TERJADI ERROR: ${e}",
                file=sys.__stderr__,
            )
            #driver.close()
            return e

        run_bot(data_account, recover - 1)


def main():

    if len(sys.argv) < 3:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    start_data = int(sys.argv[1])
    end_data = int(sys.argv[2])

    workers = 1

    if not start_data and not end_data:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    data = load_data(start_data, end_data)

    futures = []
    line_count = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(start_data + 1, end_data + 1):
            try:
                futures.append(
                    executor.submit(
                        run_bot,
                        data[line_count],
                    )
                )
            except:
                pass
            line_count += 1

    wait(futures, return_when=FIRST_EXCEPTION)


if __name__ == "__main__":
    main()
