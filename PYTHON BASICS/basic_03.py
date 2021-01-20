#Conditionals

x = 3
y = 7
check = True

if x > 3:
    print("It´s greater than 3")
elif x == 3:
    print("It´s equal 3")
else:
    print("It´s lesser than 3")

if x > y:
    print(x > y)
    print("Check: {}".format(check))
elif x < y:
    print(x > y)
    print(check)
    print("Check: {}".format(check))