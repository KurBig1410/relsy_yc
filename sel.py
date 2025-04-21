from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os
from dotenv import load_dotenv

from datetime import datetime, timedelta

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASS")

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # включи позже
driver = webdriver.Chrome(options=options)


# Получаем сегодняшнюю дату
today = datetime.today()


def subtract_one_month(date):
    return date - timedelta(days=30)


date_to = today.strftime("%d.%m.%Y")
date_from = subtract_one_month(today).strftime("%d.%m.%Y")


driver.get(
    url=f"https://yclients.com/group_analytics/filial/search/127929/?date_from={date_from}&date_to={date_to}"
)


def auth():
    try:
        # Ждём появления формы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )

        # Вводим данные
        driver.find_element(By.NAME, "email").send_keys(login)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(
            password
        )

        # Кликаем на кнопку входа
        driver.find_element(By.CSS_SELECTOR, "form button[type='submit']").click()

        time.sleep(5)  # дожидаемся редиректа

        # Сохраняем куки
        cookies = driver.get_cookies()
        with open("data/cookies.json", "w") as f:
            json.dump(cookies, f)
        print("✅ Куки сохранены в data/cookies.json")

    except Exception as e:
        print("❌ Ошибка во время логина:", e)

    finally:
        driver.quit()
auth()