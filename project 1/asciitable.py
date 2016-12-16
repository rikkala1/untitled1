__author__ = 'jc446932'
lower = 10
upper = 100
#print("Enter a number (" + str(lower) + "-" + str(upper) + "):")
str = "enter a number {} - {}:".format(lower, upper)
print(str)

for i in range(lower, upper,):
    print("{} {}".format(i, chr(i)))


