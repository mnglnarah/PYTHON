def factorial(n):
    #Calculating Factorail of number
    if n == 0 :
        return 1
    return n * factorial(n -1)

if __name__ == "__main__":
    num = 5
    print(factorial(num))