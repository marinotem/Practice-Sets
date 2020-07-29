# import math
# # gives definitions
# def polysum(n, s):
# # n is the number of sides, float or integer
# # s is the length of each side, float or integer
# # perimeter is length of the outside of the polgyon
# # trynna figure math shit out oh my godddd
#     area = (0.25*n*s**2)/math.tan(math.pi/n)
#     perimeter = n*s
#     squaredperimeter = perimeter**2
#     result = round((area + squaredperimeter),4)
#     return(result)

#     print('Month' + str(mon) + ': your remaining balance is ' + str(balance))

#     def balanceCalc(balance, annualInterestRate, monthlyPaymentRate, mon = 1):
# #This is to calculate shit
#     moninterest = annualInterestRate/12
#     minpay = (monthlyPaymentRate * balance)
#     unpaid = (balance - minpay)
#     balanceUpdate = (unpaid) + (moninterest * unpaid)

#     if mon == 12:
#         return round(balanceUpdate, 2)
#     else:
#         moninterest
#         minpay
#         unpaid
#         balanceUpdate
#         balanceUpdate = round(balanceUpdate, 2)
#         print('Month ' + str(mon) + ': your remaining balance is ' + str(balanceUpdate))
#         return balanceCalc(balanceUpdate, annualInterestRate, monthlyPaymentRate,mon + 1)
     
# print(balanceCalc(42, 0.2, 0.04,))
balance = 100
fixpay = (balance + (balance*(0.0167*12)))/12
unpaid = balance - fixpay
print(unpaid)
print(fixpay)