import bear

print("Example of modular programming.")

num = 20
newNum = bear.add_five(num)
print("Using my module: " + str(newNum))

# Doing this because it appears Python is pass by reference, not value!
newNum = bear.subtract_five(newNum)

print("Using my module again: " + str(newNum))