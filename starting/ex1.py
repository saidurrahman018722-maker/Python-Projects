import numpy as np
import pandas as pd


def calculate_total(prices, tax_rate):
    total = 0
    for amounts in prices:
        total += amounts

    tax_amount = total * tax_rate/100
    ans = total + tax_amount
    print(total)
    print(f"the tax amount is {tax_amount}")
    return ans


prices = [12, 435, 128, 23]

arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]])

print(arr.sum(axis=1))

rng = np.random.default_rng()
arr = rng.integers(low=1, high=100, size=(3, 3))
print(arr)
