# Price Alert

## Description

Basically we get a price of asset using yFinance library and monitoring the until target the price we defined.
To execute use this:

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