import requests
from bs4 import BeautifulSoup

def get_real_time_price(stock_code):
    """
    Fetches real-time price and change for a given stock code from investing.com.

    Args:
        stock_code (str): The stock code (e.g., 'BTC/USD').

    Returns:
        tuple: A tuple containing the price (str) and change (str),
               or an empty tuple if data is unavailable.
    """

    url = f'https://www.investing.com/crypto/{stock_code}'

    try:
        response = requests.get(url, headers={'User-Agent': 'your_user_agent'})  # Add user-agent to respect website policies
        response.raise_for_status()  # Raise exception for non-200 status codes
        soup = BeautifulSoup(response.content, 'lxml')

        price_element = soup.find('span', class_='price-change')
        if price_element:
            price = price_element.find('span', class_='thin').text.strip()
            change_element = price_element.find_next_sibling('span')
            change = change_element.text.strip() if change_element else ''
            return price, change
        else:
            return '', ''  # Return empty values if price element not found
    except requests.exceptions.RequestException as e:  # Handle all request exceptions
        print(f"Error fetching data: {e}")
        return '', ''

if __name__ == '__main__':
    stock_code = 'bitcoin'
    price, change = get_real_time_price(stock_code)

    if price:
        print(f"Real-time price for {stock_code}: {price}")
        print(f"Change: {change}")
    else:
        print(f"Unable to retrieve real-time price for {stock_code}.")
