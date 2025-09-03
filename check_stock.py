import requests
from bs4 import BeautifulSoup

URL = "https://store.steampowered.com/sale/steamdeckrefurbished/"
PRODUCT_KEYWORDS = "512 GB OLED"

def check_stock():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    page_text = soup.get_text()

    if PRODUCT_KEYWORDS in page_text and "Add to Cart" in page_text:
        print("IN STOCK")
        return True
    else:
        print("OUT OF STOCK")
        return False

if __name__ == "__main__":
    in_stock = check_stock()
    if in_stock:
        with open("stock_status.txt", "w") as f:
            f.write("IN STOCK")
    else:
        with open("stock_status.txt", "w") as f:
            f.write("OUT OF STOCK")
