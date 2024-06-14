import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


def real_time_price(stock_code):
    url =
    try:
        r = requests.get(url)
        web_content = 