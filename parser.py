import re

import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML

from data.config import RECEIVER, ADMIN


class CurrencyParser:
    def __init__(self, difference: int = 0.1):
        self.url = 'https://www.profinance.ru/chart/usdrub/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 YaBrowser/22.1.0.2517 Yowser/2.5 Safari/537.36',
                        'cookie': 'JSESSIONID=2C3D43ADD7CBB98DDEBB1100FF477939'}
        self.difference = difference

        self.price = 0
        self.update_price()

    def update_price(self):
        full_page = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = float(re.findall(r"\d+.\d+", soup.find("table", class_="stat news").find_all("td")[4].text)[0])
        self.price = convert

    async def check_currency(self):
        from loader import bot

        old_price = self.price
        self.update_price()
        if self.price >= old_price + self.difference:
            await bot.send_message(RECEIVER, f"🔴 Цена выросла на <b>{round(self.price - old_price, 2)}</b>₽\nТекущий курс: <b>{self.price}</b>₽")
            await bot.send_message(ADMIN, f"🔴 Цена выросла на <b>{round(self.price - old_price, 2)}</b>₽\nТекущий курс: <b>{self.price}</b>₽")
        elif self.price <= old_price - self.difference:
            await bot.send_message(RECEIVER, f"🟢 Цена упала на <b>{round(old_price - self.price, 2)}</b>₽\nТекущий курс: <b>{self.price}</b>₽")
            await bot.send_message(ADMIN, f"🟢 Цена упала на <b>{round(old_price - self.price, 2)}</b>₽\nТекущий курс: <b>{self.price}</b>₽")
        else:
            self.price = old_price


if __name__ == "__main__":
    currency = CurrencyParser()