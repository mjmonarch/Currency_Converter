# ------------------------------STAGE 1-----------------------------------
# print("Meet a conicoin!")

# ------------------------------STAGE 2-----------------------------------
# import string
#
# my_template = string.Template("I have $number conicoins.\n"
#                               "$number conicoins cost $dollars dollars.\n"
#                               "I am rich! Yippee!")
# try:
#     conicoins = int(input())
#     dollars = conicoins * 100
#     print(my_template.substitute(number=conicoins, dollars=dollars))
# except ValueError:
#     print("You should enter number")

# ------------------------------STAGE 3-----------------------------------
# import string
#
# my_template = string.Template("The total amount of dollars: $dollars")
# try:
#     conicoins = int(input("Please, enter the number of conicoins you have:"))
#     try:
#         rate_input = input("Please, enter the exchange rate:")
#         rate = int(rate_input)
#     except ValueError:
#         try:
#             rate = float(rate_input)
#         except ValueError:
#             print("You should enter numbers")
#     dollars = conicoins * rate
#     print(my_template.substitute(dollars=dollars))
# except ValueError:
#     print("You should enter numbers")

# ------------------------------STAGE 4-----------------------------------
import string

my_template = string.Template("I will get $sum $currency from the sale of $value conicoins")
CURRENCIES = ['RUB', 'ARS', 'HNL', 'AUD', 'MAD']
EXCHANGE_RATE = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}

try:
    conicoins = float(input())
    for currency in CURRENCIES:
        print(my_template.substitute(sum=round(conicoins * EXCHANGE_RATE[currency], 2), currency=currency,
                                     value=conicoins))
except ValueError:
    print("You should enter number")
