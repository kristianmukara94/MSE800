try:
    print(10 / 2)
except ZeroDivisionError:
    print("zero")
else:
    print("ok")
finally:
    print("done")