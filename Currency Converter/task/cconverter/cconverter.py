# ------------------------------STAGE 1-----------------------------------
# print("Meet a conicoin!")

# ------------------------------STAGE 2-----------------------------------
import string

my_template = string.Template("I have $number conicoins.\n"
                              "$number conicoins cost $dollars dollars.\n"
                              "I am rich! Yippee!")
try:
    conicoins = int(input())
    dollars = conicoins * 100
    print(my_template.substitute(number=conicoins, dollars=dollars))
except ValueError:
    print("You should enter number")
