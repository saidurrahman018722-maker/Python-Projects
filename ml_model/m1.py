def error(w):
    return (w-3)**2 + 5


def gradiant(w):
    return (w-3)*2


learning_rate = 0.1
w = 0

for i in range(100):
    w = w-learning_rate*gradiant(w)
    print(f"in step {i+1} , weight={w}, error={error(w):.2f}")
