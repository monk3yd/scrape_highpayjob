import requests
import csv

from bs4 import BeautifulSoup
from pprint import pprint

# for page in range():
# Parse URL Page
# https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/2
URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/1"
response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

rows = []

# Scrape table headings
table_head = soup.select_one(selector=".data-table thead tr")
headings = [header.getText() for header in table_head]
rows.append(headings)

# Scrape table data
table_cell = soup.select(selector=".data-table__cell")
i = 0
row = []
for data in table_cell:
    if i > 5:
        rows.append(row)
        row = []
        i = 0
    filtered_data = data.getText().split(":")[1]
    row.append(filtered_data)
    i += 1
# print(rows)

# Create CSV
with open('salaries_updated.csv', "w") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
