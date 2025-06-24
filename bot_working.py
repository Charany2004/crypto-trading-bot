class MockClient:
    def futures_create_order(self, symbol, side, type, quantity):
        return {
            "orderId": 123456,
            "status": "FILLED",
            "symbol": symbol,
            "side": side,
            "type": type,
            "quantity": quantity
        }

class BasicBot:
    def __init__(self, api_key, api_secret):
        # Normally we'd connect to Binance here
        self.client = MockClient()  # Using mock instead of real Binance

    def place_market_order(self, symbol, side, quantity):
        try:
            result = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            print("Mock Order Placed:", result)
            with open("bot.log", "a") as log_file:
                log_file.write(str(result) + "\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    print("=== Mock Binance Trading Bot ===")
    api_key = input("API Key (demo): ")
    api_secret = input("API Secret (demo): ")
    bot = BasicBot(api_key, api_secret)

    symbol = input("Symbol (e.g. BTCUSDT): ")
    side = input("Side (BUY or SELL): ").upper()
    quantity = float(input("Quantity: "))

    bot.place_market_order(symbol,side,quantity)
