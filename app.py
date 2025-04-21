import requests
import json

def getjson():
    url = "https://yclients.com/group_analytics/filial/search/127929/?date_from=16.03.2025&date_to=16.04.2025"
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
        "Referer": "https://yclients.com/group_analytics/filial/127929/?date_from=16.03.2025&date_to=16.04.2025",
        # "Cookie": "lang=1; erp_language_id=1; yc_utm_campaign=; yc_utm_content=; yc_utm_term=; yc_utm_click_id=; tmr_lvid=75d6d25a24f523e45af50496a057e6af; tmr_lvidTS=1743509051264; _gcl_au=1.1.731756392.1743509052; original_utm_campaign_v2=(not_set); original_utm_term_v2=(not_set); adrdel=1743509052321; adrcid=Afw8VvBXxgry7WzvlL0e0Ug; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1743595452351%2C%22sl%22%3A%7B%22224%22%3A1743509052351%2C%221228%22%3A1743509052351%7D%7D; adtech_uid=af44c2ea-1854-419c-ad84-d727b92ef1f2%3Ayclients.com; top100_id=t1.7735337.1135596623.1743509100247; spid=1743509659999_59a1750b89995d9e4ae0f381cff8d71d_2kai4rbar6m5lx6u; _ym_uid=1743509662373616708; _ym_d=1743509662; yc_user_id=13115260; _ymab_param=-78vjLM9glukHPOp1cluqHYpEdSuCPrVhgS5I061rYhyfS6LtwIWSl2DlhXsUGxVtUNrDmTqTGDOeOla0HE4Ss-OcBg; original_utm_source_v2=e.mail.ru; original_utm_medium_v2=referral; original_utm_referer_v2=https://e.mail.ru/; yc_referer_full=https%3A%2F%2Fwww.yclients.com%2F; analytics-udid=4iSBuGMPgYOdEOYFXhHRaN1kTMCzqXcHuCK4rgKz; tracking-index=17; x-feature-waiting-room-web=1; auth=u-13115260-1d5c637fc89d4677acd25; ycl_language_id=1; yc_referral_url=; flsid=b973c85c-b4e6-48b1-a201-3009b870c23c; yc_company_id=565149; app_service_group=0; _gid=GA1.2.2070529521.1744793772; _ym_isad=2; _ym_visorc=w; _ga=GA1.1.633009811.1743509051; _ga_4Z5R7DZBLZ=GS1.2.1744793772.4.1.1744793777.55.0.0; _ga_CZ0CKD8R74=GS1.1.1744793771.2.1.1744793786.0.0.0; spsc=1744793792541_4a3b89b8a603a9eb5d5d040fca8d7f34_f7f9cc33a6cf20143973c216e7b6896d; t3_sid_7735337=s1.1698950423.1744793787496.1744793792793.7.5.1.0; domain_sid=QCtE-T4w73NHba-EY12ra%3A1744793793292; yc_utm_source=direct; yc_utm_medium=none; tmr_detect=0%7C1744795684711; _ga_P2LM7D8KSM=GS1.1.1744793771.13.1.1744796174.60.0.0; _ga_X3P164PV59=GS1.1.1744793787.13.1.1744796174.60.0.0; _ga_3M9TPBMV14=GS1.1.1744793772.13.1.1744796174.60.0.0",
    }
    # payload = {"email": "Suhrab.k@mail.ru", "password": "rx3kgx"}

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
