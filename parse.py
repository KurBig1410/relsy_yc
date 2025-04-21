import json
from bs4 import BeautifulSoup
import pandas as pd

def parse():
    # Загрузка JSON-файла
    with open("data/response.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    html = raw["content"]

    # Парсим HTML
    soup = BeautifulSoup(html, "html.parser")

    # Находим таблицу
    table = soup.find("table")

    # Получаем заголовки
    headers = [th.get_text(strip=True) for th in table.find_all("th")]

    # Собираем строки
    rows = []
    for tr in table.find("tbody").find_all("tr"):
        cells = [td.get_text(strip=True).replace("\xa0", " ") for td in tr.find_all("td")]
        if cells:  # чтобы пропустить пустые строки (например, итог)
            rows.append(cells)

    # Создаём DataFrame и сохраняем в CSV
    df = pd.DataFrame(rows, columns=headers)
    df.to_csv("data/filial_stats.csv", index=False, encoding="utf-8-sig")

    print("✅ Данные сохранены в файл: filial_stats.csv")
