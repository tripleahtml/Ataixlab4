import requests

def get_data(endpoint):
    base_url = "https://trade.ataix.kz/user/orders?s=1INCH%2FUSDT&t=0"
    try:
        response = requests.get(f"{base_url}{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Қате орын алды: {e}")
        return None

def main():
    print("### Валюталар тізімі ###")
    currencies = get_data("/currencies")
    if isinstance(currencies, list):
        for currency in currencies:
            print(currency)
        print(f"Жалпы валюталар саны: {len(currencies)}")
    
    print("\n### Сауда жұптары ###")
    symbols = get_data("/symbols")
    if isinstance(symbols, list):
        for symbol in symbols:
            print(symbol)
        print(f"Жалпы сауда жұптары саны: {len(symbols)}")
    
    print("\n### Монеталар мен токендердің бағалары ###")
    prices = get_data("/prices")
    if isinstance(prices, list):
        print(f"{'Символ':<10} {'Баға':>15}")
        print("-" * 26)
        for price in prices:
            if isinstance(price, dict) and 'symbol' in price and 'price' in price:
                print(f"{price['symbol']:<10} {price['price']:>15}")
    
    print("\n✅ Деректер сәтті алынды!")

if __name__ == "__main__":
    main()
