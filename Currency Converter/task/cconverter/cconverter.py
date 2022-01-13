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
# import string
#
# my_template = string.Template("I will get $sum $currency from the sale of $value conicoins")
# CURRENCIES = ['RUB', 'ARS', 'HNL', 'AUD', 'MAD']
# EXCHANGE_RATE = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
#
# try:
#     conicoins = float(input())
#     for currency in CURRENCIES:
#         print(my_template.substitute(sum=round(conicoins * EXCHANGE_RATE[currency], 2), currency=currency,
#                                      value=conicoins))
# except ValueError:
#     print("You should enter number")

# ------------------------------STAGE 5-----------------------------------
# import json
# import string
# import requests
#
# CURRENCY_TEMPLATE = string.Template("http://www.floatrates.com/daily/$your_currency_code.json")
#
# currency_code = input()
# currency_host = CURRENCY_TEMPLATE.substitute(your_currency_code=currency_code)
#
# try:
#     r = requests.get(currency_host)
#     currency_dict = json.loads(r.text)
#     print(currency_dict['usd'])
#     print(currency_dict['eur'])
# except Exception:
#     print("Something went wrong")

# ------------------------------STAGE 6-----------------------------------
import json
import string
import requests


def get_rate(_currency_host, _currency_to_exchange):
    try:
        _r = requests.get(_currency_host)
        _currency_dict = json.loads(_r.text)
        return _currency_dict[_currency_to_exchange.lower()]['rate']
    except Exception:
        print("Something went wrong")


CURRENCY_TEMPLATE = string.Template("http://www.floatrates.com/daily/$your_currency_code.json")

user_currency_code = input()
user_currency_code_f = user_currency_code.lower()
currency_host = CURRENCY_TEMPLATE.substitute(your_currency_code=user_currency_code_f)
EXCHANGE_RATE = {}

try:
    r = requests.get(currency_host)
    currency_dict = json.loads(r.text)
    EXCHANGE_RATE['usd'] = currency_dict['usd']['rate'] if user_currency_code_f != 'usd' else 1
    EXCHANGE_RATE['eur'] = currency_dict['eur']['rate'] if user_currency_code_f != 'eur' else 1
    currency_to_exchange = input()
    while currency_to_exchange:
        currency_to_exchange_f = currency_to_exchange.lower()
        amount = float(input())
        print("Checking the cache…")
        if currency_to_exchange_f in EXCHANGE_RATE.keys():
            print("Oh! It is in the cache!")
            print(f"You received {round(amount * EXCHANGE_RATE[currency_to_exchange_f], 2)} {currency_to_exchange}")
        else:
            print("Sorry, but it is not in the cache!")
            rate = get_rate(currency_host, currency_to_exchange_f)
            EXCHANGE_RATE[currency_to_exchange_f] = rate
            print(f"You received {round(amount * rate, 2)} {currency_to_exchange}")
        currency_to_exchange = input()
except Exception:
    print("Something went wrong")
