import requests

class CurrencyService:
    API_BASE_URL = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json'

    def get_exchange_rates(self, target_currencies: list) -> dict:
        response = requests.get(self.API_BASE_URL)
        if response.status_code != 200:
            raise Exception("Failed to fetch exchange rates")
        
        data = response.json()
        exchange_rates = {currency: data['usd'].get(currency, 1) for currency in target_currencies}
        return exchange_rates