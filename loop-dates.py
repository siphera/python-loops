from datetime import datetime, timedelta

# Print ten dates, each two week apart, starting from today, in the form YYYY-MM-DD===>

dt = datetime(2020, 10, 16, 11, 22, 50)

add_dt = dt + timedelta(days=14)
# print(add_dt.strftime("%m-%d-%y %H %M %S%"))

# while loop method
x = 0
while x < 10:
    print(dt)
    dt = dt + timedelta(days=14)
    x = x+1

# for loop method
i = 0
for i in range(10):
    print(dt)
    dt = dt + timedelta(days=14)



