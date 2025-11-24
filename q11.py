salary=int(input("Enter the Salary:"))
if salary<30000:
    tax_rate=5
elif salary >30000 and salary<70000:
    tax_rate=15
else:
    tax_rate=25
print("The Final tax is",tax_rate,"%")
