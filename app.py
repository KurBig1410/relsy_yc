import requests
import json
from datetime import datetime, timedelta


# Получаем сегодняшнюю дату
today = datetime.today()


def subtract_one_month(date):
    return date - timedelta(days=29)


date_to = today.strftime("%d.%m.%Y")
date_from = subtract_one_month(today).strftime("%d.%m.%Y")


def getjson():
    url = f"https://yclients.com/group_analytics/filial/search/127929/?date_from={date_from}&date_to={date_to}"
    # Загружаем куки из cookies.json
    with open("data/cookies.json", "r") as f:
        raw_cookies = json.load(f)

    session = requests.Session()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/25.2.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "X-Yclients-Application-Action": "",
        "X-Yclients-Application-Name": "biz.erp.web",
        "X-Yclients-Application-Platform": "legacy JS-1.0",
        "X-Yclients-Application-Version": "1.0.0",
        "Referer": f"https://yclients.com/group_analytics/filial/search/127929/?date_from={date_from}&date_to={date_to}",
    }

    # Устанавливаем куки в сессию
    for cookie in raw_cookies:
        session.cookies.set(cookie["name"], cookie["value"])

    response = session.get(url, headers=headers)
    content_type = response.headers.get("Content-Type", "")

    if response.status_code == 200:
        if "application/json" in content_type:
            try:
                data = response.json()
                output_path = "data/response.json"
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"✅ JSON сохранён в: {output_path}")
            except json.JSONDecodeError:
                print("❌ Ошибка при разборе JSON.")
        elif "text/html" in content_type:
            output_path = "response.html"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"✅ HTML сохранён в: {output_path}")
        else:
            print("⚠️ Неизвестный тип контента:", content_type)
            print("Сохраняю как текст…")
            with open("response.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("✅ Сохранено в: response.txt")
    else:
        print("❌ Ошибка запроса:", response.status_code)
        print(response.text)
