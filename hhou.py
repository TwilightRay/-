import requests, bs4, os, time
#rates-current__table-cell rates-current__table-cell_column_buy
#rates-current__table-cell rates-current__table-cell_column_sell
url = 'https://www.sberbank.ru/ru/quotes/metal'
gold_buy = []
z=requests.get(url)
soup = bs4.BeautifulSoup(z.text,"html.parser")
gold_buy.append(soup.select('rates-current__table-cell rates-current__table-cell_column_buy'))
#gold_sell = soup.select('rates-current__table-cell rates-current__table-cell_column_sell')

print(gold_buy)

