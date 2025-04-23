from bs4 import BeautifulSoup
import json
import pandas as pd
import re

def parse_html():
    # Загружаем HTML из JSON
    input_path = "data/response.json"
    with open(input_path, "r", encoding="utf-8") as f:
        raw_json = json.load(f)
        html = raw_json["content"]

    # Парсим HTML
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    # Получаем заголовки
    headers = [th.get_text(strip=True) for th in table.find_all("thead")[0].find_all("th")]

    # Получаем строки таблицы
    data = []
    for row in table.find_all("tbody")[0].find_all("tr"):
        cols = row.find_all("td")
        if not cols:
            continue
        cleaned = [re.sub(r'\s+', ' ', col.get_text(strip=True)).strip() for col in cols]
        data.append(cleaned)

    # Создаем DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Сохраняем как JSON
    output_path = "data/response_out.json"
    df.to_json(output_path, orient="records", force_ascii=False, indent=2)

    # import ace_tools as tools; tools.display_dataframe_to_user(name="Филиалы", dataframe=df)

    output_path