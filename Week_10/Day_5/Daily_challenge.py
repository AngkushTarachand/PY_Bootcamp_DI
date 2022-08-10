import time


import requests

before = time.time()
response = requests.get("https://google.com")
after = time.time()

print(f"do get api request to google took {after - before} sec")
