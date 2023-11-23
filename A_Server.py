import socket
import time
import datetime
from forex_python.converter import CurrencyRates

def tobyte(string):
    #str to byte
    return string.encode('utf-8')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',12346))
s.listen(1)
conn,info = s.accept()

c = CurrencyRates()

# * Writing a
# communication protocol for money exchange


# - The client prompts with “Please specify the amount of money and currency.”
# - 4 currencies are required:
#           * Thai Baht
#           * US dollar
#           * Euro
#           * Singapore Dollar
msg=conn.recv(1024)
print(msg)

currency = msg.decode('utf-8')

print(currency)

currency_list = ['THB','USD','EUR','SGD']
currency_list.remove(currency)

print(f'remaining currency {currency_list}')

msg=conn.recv(1024)
print(msg)

amount = float(msg)
print(amount)
# * Server
# responses with
#- Date and time occur.
#- Convert to all 3 other currencies.

money_list = []
for i in (currency_list):
    money_list.append(c.convert(currency,i,amount))


if (currency == 'THB'):
    conn.send(tobyte(f"USD: {money_list[0]:.2f}"
          f"\nEUR: {money_list[1]:.2f}"
          f"\nSGD: {money_list[2]:.2f}"))


elif (currency == 'USD'):
    conn.send(tobyte(f"THB: {money_list[0]:.2f}"
          f"\nEUR: {money_list[1]:.2f}"
          f"\nSGD: {money_list[2]:.2f}"))


elif (currency == 'EUR'):
    conn.send(tobyte(f"THB: {money_list[0]:.2f}"
          f"\nUSD: {money_list[1]:.2f}"
          f"\nSGD: {money_list[2]:.2f}"))


elif (currency == 'SGD'):
    conn.send(tobyte(f"THB: {money_list[0]:.2f}"
          f"\nUSD: {money_list[1]:.2f}"
          f"\nEUR: {money_list[2]:.2f}"))


else:
    conn.send(tobyte('error'))

print('Perfect!')

time.sleep(0.3)

s.close()