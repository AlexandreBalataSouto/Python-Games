#Dictionaries
capitals = {"Japan":"Tokyo","Korea":"Seoul"}

print(capitals)
print(len(capitals))

capital = capitals["Japan"]
print(capital)

capitals["China"] = "Beijing"
print(capitals)

print("--------------------------------------------")
for country in capitals:
    capital = capitals[country]
    print("The capital of {} is {}".format(country,capital))