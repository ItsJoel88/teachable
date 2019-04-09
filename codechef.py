withdrawal = input()
balance = input()

withdrawal=int(withdrawal)
balance=float(balance)

if withdrawal+0.5<balance and withdrawal%5==0:
    balance=balance-withdrawal-0.5
    print('%.2f'%balance)
else:
    print('%.2f'%balance)
