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
