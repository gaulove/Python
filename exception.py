while True:

	try:
		x = int(input("Please enter the value of x"))
		break
	except:
		print("Please Enter the valid number")
	finally:
	
		print("Program executed")
