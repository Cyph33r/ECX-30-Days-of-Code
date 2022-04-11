from functools import lru_cache


@lru_cache()  # caches each returned value in a dictionary allowing for faster runtime
def fibonacci(n):
    assert isinstance(n, int), f"Only int is allowed \nYou entered a/an {n.__class__}"

    if n in (1, 2):  # base condition
        print(1)
        return 1
    else:
        term = fibonacci(n - 2) + fibonacci(n - 1)  # add up the preceding terms to get the nth terms
        print(term)
        return term


if __name__ == '__main__':
    print(fibonacci(500))
