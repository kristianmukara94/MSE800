def my_function(x, y):
    return x / y

try:
    my_function(6, 2)
except ZeroDivisionError as e:
    print(e)
else:
    print("Everything worked OK")
finally:
    print("Always runs")

try:
    print(10 / 2)
except ZeroDivisionError:
    print("zero")
else:
    print("ok")
finally:
    print("done")
