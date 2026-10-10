def read_int(prompt, minimum=None, maximum=None):
    while True:
        text = input(prompt)

        try:
            number = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum is not None and number < minimum:
            print("Number must be at least", minimum)
            continue

        if maximum is not None and number > maximum:
            print("Number must be at most", maximum)
            continue

        return number


# Test: type abc, 0, 99, then 5
result = read_int("Enter a number from 1 to 10: ", 1, 10)
print("You entered:", result)
