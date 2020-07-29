def balanceCalc(balance, annualInterestRate, monthlyPaymentRate, mon = 1):
# #This is to calculate how to pay off debt using a changing variable
    moninterest = annualInterestRate/12
    minpay = (monthlyPaymentRate * balance)
    unpaid = (balance) - (minpay)
    balanceUpdate = (unpaid) + (moninterest * unpaid)
    if mon == 12:
        print('Month ' + str(mon) + ': your remaining balance is ' + str(round(balanceUpdate,2)))
        print('Congrats! You have paid off your debt!')
    else:
        balanceUpdate
        print('Month ' + str(mon) + ': your remaining balance is ' + str(round(balanceUpdate, 2)))
        return balanceCalc(balanceUpdate, annualInterestRate, monthlyPaymentRate,mon + 1)
     
# #This is to calculate paying off debt at a fixed rate that does not change month to month
def balanceCalc(balance, annualInterestRate, mon = 1):
    moninterest = annualInterestRate/12
    #moninterest is the monthly interest, a float
    fixpay = (balance + (balance * (moninterest*12)))/12
    #fixpay is a fixed payment calculating accrued interest based on if balance is constant
    #fixpay is divided by 12 to give a fixed payment over or around 12 months to get to 0
    unpaid = (balance) - (fixpay)
    def balanceCalcUpdate(balance, annualInterestRate, mon = 1):
        #balanceCalcUpdate ensures that balance will be unchanged in balanceCalc so fixpay is stable
        #reused calculations within this local function
        moninterest = annualInterestRate/12
        unpaid = (balance) - (fixpay)
        balanceUpdate = (unpaid) + (moninterest * unpaid)
        #balanceUpdate calculates to make sure we are on track per month to pay off within 12 months
        if mon == 12 or balanceUpdate < 0.00:
            #if we have reached 12 months or balance goes in to negative, the operation ends here
            balanceUpdate = round(balanceUpdate, 2)
#             #round balance to the second float digit
            print('Month ' + str(mon) + ': your remaining balance is ' + str(balanceUpdate))
            print('You paid off your debt by month ' + str(mon) + '! Congrats!')
        else:
            balanceUpdate
            print('Month ' + str(mon) + ': your remaining balance is ' + str(round(balanceUpdate,2)))
            return balanceCalcUpdate(balanceUpdate, annualInterestRate, mon + 1)
    balanceCalcUpdate(balance, annualInterestRate, mon = 1)