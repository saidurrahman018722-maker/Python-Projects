# cnt = 0
# for num in range(100):
#     if num % 2 == 0:
#         cnt += 1

# print(f"the total even number upto 100 is {cnt}")

# arr = ["name", "email", "password", "id", "createAt"]

# arr.insert(1, "something")

# print(arr)
# nums = [1, 100, 23, 65, 45, 34]
# # nums.sort(reverse=True)
# print(sorted(nums))
from functools import wraps
import logging


# def full_name(first_name, last_name):
#     return f"{first_name} {last_name}"


# def some_func(func, *args):
#     logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)
#     return func(*args)


# result = some_func(full_name, "saif", "rahman")
# print(result)


def full_name(func):
    logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"u ran the function->>>> {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@full_name
def name(first_name, last_name):
    print(f"{first_name} {last_name}")


print(name.__name__)
