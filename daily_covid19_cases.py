# Copyright (C) December 2022 {Sunny Patel} <{sunnypatel124555@gmail.com}>

# This file is part of the {Daily Covid-19 Cases} project.

# The {Daily Covid-19 Cases} project can not be copied, distributed, and/or modified without the express
# permission of {Sunny Patel} <{sunnypatel124555@gmail.com}>.

import tkinter as tk
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# create the main window
window = tk.Tk()
window.title("COVID-19 Tracker")

# create a frame to hold the country selection buttons
frame = tk.Frame(window)
frame.pack()

# create a function to show the global data
def show_global_data():
    # scrape the data from the website
    page = requests.get("https://www.google.com/covid19/")
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find(id="main_table_countries_today")

    # get the total number of cases and deaths
    total_cases = data.find_all("tr")[0].find_all("td")[1].text.strip()
    total_deaths = data.find_all("tr")[1].find_all("td")[1].text.strip()

    # update the cases label with the total cases and deaths
    cases_label.config(text=f"Total Cases: {total_cases}\nTotal Deaths: {total_deaths}")

    # generate a trend graph of the cases over time
    cases = []
    dates = []
    for row in data.find_all("tr")[3:]:
        date = row.find_all("td")[0].text.strip()
        cases_today = row.find_all("td")[1].text.strip()
        cases.append(int(cases_today))
        dates.append(date)

    plt.plot(dates, cases)
    plt.show()

# create a button for global data
global_button = tk.Button(frame, text="Global", command=show_global_data)
global_button.pack(side=tk.LEFT)

# create a function to show the Canadian data
# create a function to show the Canadian data
def show_canada_data():
    # scrape the data from the website
    page = requests.get("https://www.google.com/covid19/")
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find(id="main_table_countries_today")

    # find the table row for Canada
    canada_row = None
    for row in data.find_all("tr"):
        if row.find_all("td")[0].text.strip() == "Canada":
            canada_row = row
            break

    # get the total number of cases and deaths for Canada
    total_cases = canada_row.find_all("td")[1].text.strip()
    total_deaths = canada_row.find_all("td")[3].text.strip()

    # update the cases label with the total cases and deaths for Canada
    cases_label.config(text=f"Total Cases: {total_cases}\nTotal Deaths: {total_deaths}")

    # generate a trend graph of the cases over time for Canada
    cases = []
    dates = []
    for row in data.find_all("tr")[3:]:
        date = row.find_all("td")[0].text.strip()
        cases_today = row.find_all("td")[1].text.strip()
        if date == "Canada":
            cases.append(int(cases_today))
            dates.append(date)

    plt.plot(dates, cases)
    plt.show()

# create a button for Canadian data
canada_button = tk.Button(frame, text="Canada", command=show_canada_data)
canada_button.pack(side=tk.LEFT)

# create a frame to hold the data display
data_frame = tk.Frame(window)
data_frame.pack()

# create a label to display the daily cases
cases_label = tk.Label(data_frame, text="Daily Cases:")
cases_label.pack()

# create a label to display the trend graph
trend_label = tk.Label(data_frame, text="Trend Graph:")
trend_label.pack()

# run the main loop
window.mainloop()