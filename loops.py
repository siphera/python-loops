'''
# ==========WHILE LOOP================
# USING A WHILE LOOP TO INCREMENT COUNTER
count = 0
while count < 20:
    print("number", count)
    count = count + 2
print("done")


num = 2
count = 0
while count <= 20:
    res = num * count
    print(num, "x", count, "=", res)
    count = count + 1

print("done")


gas = 10
while gas > 10:
    print("vroom")
    gas = gas - 1
    if gas == 5:
        print("fill up")
        break
'''



# ==========FOR LOOP=======
'''
for x in range(10, -1, -1):
    print(x)
'''

'''
#FOR LOOP WITH LISTS
ages = [18, 21, 16,12]
for age in ages:
    if age >= 18:
        print("come on in")
    elif age >= 16:
        print("not quite yet")
    else:
        print('get outta here')
'''

'''# FOR LOOP WITH DICTIONARY
d = {"5": "Amber", "9": "Skyler", "4": "Odwa"}
for x in d.items():
    print(x)
'''

# EXCERCISE
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")

    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
