total = int(input("total bill"))
isMember = input("member? yes/no")

if total >= 1000 and isMember == "yes":
	discount = total * 0.10
	print(discount)
else total >= 1000 and isMember == "no":
	discount = total * 0.05
	print(discount)
