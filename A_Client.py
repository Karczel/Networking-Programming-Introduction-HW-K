import socket
import time
import datetime

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',12346))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print("Please specify the amount of money and currency.")
print("Choose your currency:")
print("THB | USD | EUR | SGD")
reply1 = input()
while reply1 not in ['THB', 'USD', 'EUR', 'SGD']:
    print('Please choose one of the available options')
    print("THB | USD | EUR | SGD")
    reply1 = input()
reply1_b = str.encode(reply1)

s.send(reply1_b)

print("Input the amount of your money")

reply2 = input()
while (is_number(str(reply2)) != True):
    print("Please input amount of money in numbers")
    reply2 = input()
reply2_b = str.encode(reply2)
s.send(reply2_b)

print('')
print('Time information:')
print(datetime.datetime.now())
print('')

msg=s.recv(1024)
print(msg.decode())

# * Writing a
# communication protocol for money exchange



# * The
# client sends an “amount of money with a specific currency.”

time.sleep(0.5)

s.close()