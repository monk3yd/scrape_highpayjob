import requests
import csv

from random import random
from time import sleep
from bs4 import BeautifulSoup
from pprint import pprint

# General Variables
rows = []
table_headings_created = False

# Iterate through pages
for current_page in range(1, 35):
    # Parse URL Page
    URL = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{current_page}"
    print(f"Current Page: {current_page}/34")
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, "lxml")

    if not table_headings_created:
        # Scrape table headings
        table_head = soup.select_one(selector=".data-table thead tr")
        headings = [header.getText() for header in table_head]
        rows.append(headings)
        table_headings_created = True
        print("Table Headings Created...")

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

    sleep(random())
# print(rows)

# Create CSV
with open('salaries_updated.csv', "w") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
