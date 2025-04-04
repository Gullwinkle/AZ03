from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Edge()

try:
    # Открываем страницу
    url = "https://www.divan.ru/category/divany"
    driver.get(url)

    time.sleep(5)
    from selenium import webdriver
    import time

    # Прокручиваем страницу вниз
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        current_position = driver.execute_script("return window.pageYOffset")
        window_height = driver.execute_script("return window.innerHeight")
        scroll_up_position = current_position - (3 * window_height)
        driver.execute_script(f"window.scrollTo(0, {scroll_up_position});")
        time.sleep(2)  # Пауза после прокрутки вверх

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        else:
            last_height = new_height

    print("Прокрутка завершена")
    divans = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="product-card"]')

    parsed_data = []

    for divan in divans:
        try:
            name = divan.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
            link = divan.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
            price = divan.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')

        except Exception as e:
            print(f"Произошла ошибка при парсинге: {e}")
            continue

        parsed_data.append([name, price, link])

    driver.quit()

    with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Название', 'Цена', 'Ссылка'])
        writer.writerows(parsed_data)

finally:
    # Закрываем браузер
    driver.quit()