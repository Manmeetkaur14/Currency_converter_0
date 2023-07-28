with open("currencydata.txt") as f:
  lines = f.readlines()

  currencyDict = {}
for line in lines:
  parsed = line.split("\t")
  currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter The Amount:"))
print("Enter the currency which u want to convert  into Available options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Enter the currency from the Above given List ")
print(
    f"{amount} INR is equal to the {amount*float(currencyDict[currency])}  {currency}"
)
