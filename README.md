# Price Alert

## Description

The purpose of the algorithm is to monitor the price of an asset and when it goes >= or <= to the prices we set, 
a pop up appears on the screen.

The script works as follows.
1. We get the asset price from the "STOCK" market (Microsoft = MSFT, Tesla=TSLA, Ambev=ABEV) using the yFinance library.
2. We monitor the target until the price we set. We have to enter a price above the current price and a price below the 
current price.

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Price_alert.

```bash
pip install price-alert-rhsm
```

### Guide

```python
from price_alert.price_monitoring import PriceAlert

pa = PriceAlert(asset='TSLA', waiting_time=5)
pa.price_alert_request()
```

Output expected:

```
Consult at: 2022-10-07 12:01:09.266432
Ticker TSLA - Current price = $ 228.4
Type a price bigger than 228.4:
Type a price less than 228.4:
```

### Example:

![](static/test_package.gif)

**Note**: I ran this test on a Saturday, obviously the market was closed, to run the rule I set an equal price
current price to pop up the message box if the price is equal to or higher/lower than the current price.

After entering the values to monitor, just wait for the price movement to hit the target. When this occurs, the 
notification will appear in your window.

### Suggestion to new implementation

1. Monitor multiple assets. Consequently, we need alert for several assets.
2. Option to conversion result to others currency: BRL, EURO, BTC etc
3. Implement options to calculate the price to monitoring as percentual or value


## Author
Rafael Meireles
[LinkedIn](https://www.linkedin.com/in/rafa-hsm/)

## License
[MIT](LICENSE)