from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('<api-key>', '<secret-key>')


# preparing order data
market_order_data = MarketOrderRequest(
                      symbol="AAPL",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY
                  )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
                )

print("Market order submitted for {} shares of {}".format(market_order.qty, market_order.symbol))
print(market_order)