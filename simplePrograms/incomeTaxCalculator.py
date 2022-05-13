import taxBrackets

income = float(input("please enter your total income "))

#import the province's tax brackets
NS = taxBrackets.NS
ON = taxBrackets.ON

def calculateTax(income, prov, provLabel):
    remainingIncome = 1
    lastBracket = 0
    totalTax = 0
    for i in range(len(prov)):
        bracket = prov[i][0]
        taxRate = prov[i][1]

        if bracket == "over" and remainingIncome == 1:
            totalTax += (income - lastBracket) * taxRate
        else:
            if remainingIncome == 0:
                continue
            elif income < bracket:
                print(f"income {income} is less than bracket {bracket}")
                totalTax += (income - lastBracket) * taxRate
                remainingIncome = 0
            elif income > float(bracket):
                taxable = bracket - lastBracket
                totalTax += taxable * taxRate
                #print("total tax from bracket", i, "is", (taxable * taxRate))
        lastBracket = bracket
    print(f"total tax for {provLabel} is {totalTax}")

calculateTax(income, NS, "NS")
calculateTax(income, ON, "Ontario")


