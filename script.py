import json
import os
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable

webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))
number_of_images = 3
headless = True
min_resolution=(500,500)
max_resolution=(500,500)

dataset = "D:\\Projects\\Web\\Google-Image-Scraper\\wine-global-products.json"
with open(dataset, 'r') as file:
  collection = json.load(file)

for item in collection:
  if ("image" in item):
    continue
  image_scraper = GoogleImageScraper(webdriver_path, image_path, item["name"], number_of_images, headless, min_resolution, max_resolution)
  image_urls = image_scraper.find_image_urls()
  item["image"] = image_urls
  dump = "D:\\Projects\\Web\\Google-Image-Scraper\\wine-global-products-dump.json"
  with open(dump, 'w') as file:
    json.dump(collection, file, indent=2)
