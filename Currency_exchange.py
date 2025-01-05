import requests

def fetch_exchange_rate(base_currency, target_currency):
    """Fetch live exchange rate between two currencies."""
    try:
        api_url = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()
        if "rates" in data:
            rate = data["rates"].get(target_currency)
            if rate:
                return rate
            else:
                print(f"Currency {target_currency} not found!")
        else:
            print("Error: Unable to fetch rates.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def currency_converter():
    """Main function to convert currency."""
    print("Welcome to Currency Converter!")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    try:
        amount = float(input(f"Enter the amount in {base_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    exchange_rate = fetch_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed. Please try again.")

if __name__ == "__main__":
    currency_converter()