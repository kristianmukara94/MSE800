if __name__ == "__main__":
   
    number = int(input("Please enter a number:"))

    def fibonacci_series(number):
        series = []
        a, b = 0, 1
        for _ in range(number):
            series.append(a)
            a, b = b, a + b
        return series    
        
print(fibonacci_series(number))