# WEB SCRAPING

# Libraries for web scraping
# Request Beautifulsoup, lxml, scrapy, selenium
# API keys
# Exercise: openweathermap.org

# Step1: Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import json

# # Step2: fetch the the web pages

# url = 'http://ryeko.org'

# response = requests.get(url)
# html_content = response.text
# # api_key = 'your api key'

# # Step3: Parse the HTML content using BeautifulSoup

# soup = BeautifulSoup(html_content, 'html.parser')

# # Step4: find the specific data
# data = []
# for item in soup.find_all('a'):
#     title = item.text.strip()
#      link = item.get('href')
#      data.append({title': ' + 'link': link})

# # Step5: Save the data in a CSV file
# csv_file = 'scraped_data.csv'

# with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=['title', 'link'])
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)

# # Step6: save the data to a json file

# json_file = 'scraped_data.json'

# with open(json_file, mode='w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)

# # Step 7: save successfully to csv and json file
# print(f'Data saved to{csv_file} and json file{json_file}')

# Exercise: scrape the data from openweathermap.org
# current weatherdata

api_key = 'f4d0c423ad17b0541176f737878aa966'
city = 'Mbarara'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'


# Make a request to the OpenWeatherMap API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

# Extracting specific data
    weather_data = {
        "city": city,
        "temperature": data['main']['temp'],
        "weather_description": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed']
    }

# Save to JSON file
    json_file = 'weather_data.json'
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(weather_data, file, indent=4, ensure_ascii=False)

# Save to CSV file using csv module
    csv_file = 'weather_data.csv'
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=weather_data.keys())
        writer.writeheader()
        writer.writerow(weather_data)
    
# Confirm data saved
    print(f'Data saved to {csv_file} and {json_file}')
else:
    print(f"Error: {response.status_code}")