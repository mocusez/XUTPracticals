TARIFF = {"TARIFF_11": 0.244618, "TARIFF_12": 0.210618, "TARIFF_31": 0.136928, "TARIFF_41": 0.106928}
print("Electricity Bill Estimator")
print(f"There are {len(TARIFF)} kinds of tariff:")
for i in TARIFF.keys():
    print(i)

tariff = int(input("Which tariff are you using?"))
cents_per_kwh = 1
name = "TARIFF_" + str(tariff)

while name not in TARIFF.keys():
    print("Error, please choose one of the options")
    tariff = int(input("Which tariff are you using? "))
cents_per_kwh = TARIFF[name]


daily_use_in_kwh = float(input("What is the daily use in kWh? "))
number_billing_days = float(input("What is the number of billing days? "))
estimated_bill = (cents_per_kwh * 100) * daily_use_in_kwh * number_billing_days
estimated_bill_in_dollars = estimated_bill / 100
print("Your estimated bill is: ${0:.2f}".format(estimated_bill_in_dollars))
