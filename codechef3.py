def factorial(N) :
    f = 1
    for n in range(1, N+1) :
        f = f * n
    return f

num_tests = int(input())

for n in range(num_tests) :
    num = int(input())
    print(factorial(num))
