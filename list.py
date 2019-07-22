month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days =len(days_in_month)

print(num_days)
if 31 in days_in_month:
	print("number of days contain 31")
print(type(days_in_month[0]))
days_in_month.append(5)
print(days_in_month)
days_in_month.remove(31)
print(days_in_month)
days_in_month.pop()
print(days_in_month)
print(days_in_month.count(5))
print(days_in_month)
gaurav= True
if gaurav is True:
	print(gaurav)