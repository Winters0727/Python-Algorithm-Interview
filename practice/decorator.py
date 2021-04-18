def fibo_decorator(func):
    memo = {}
    def decorate(*args, **kwargs):
        if args:
            n = args[0]
        else:
            n = kwargs.get('n')

        if n in memo.keys():
            return memo.get('n')
        else:
            result = func(n)
            memo[str(n)] = result
            return result
            
    return decorate

@fibo_decorator
def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)

for num in range(1, 11):
    print(fibo(num))