bank_balance = 100
phone_balance = int(input("Please enter the phone balance"))
print(phone_balance, bank_balance)
if phone_balance <5:
	phone_balance +=10
	bank_balance -=10
print(phone_balance, bank_balance)