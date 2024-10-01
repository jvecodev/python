print("Hello")
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a,b = b, a + b

fibonacci(10) 