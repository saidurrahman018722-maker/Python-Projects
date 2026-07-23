import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# সুষম (symmetric) distribution
symmetric_data = np.random.normal(50, 10, 1000)
skewed_data = np.concatenate([np.random.normal(30, 5, 900), np.random.normal(
    150, 20, 100)])  # একদিকে ঝুঁকে থাকা (skewed)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(symmetric_data, bins=30)
axes[0].axvline(np.mean(symmetric_data), color="red", label="Mean")
axes[0].axvline(np.median(symmetric_data), color="green",
                linestyle="--", label="Median")
axes[0].set_title("Symmetric Distribution")
axes[0].legend()

axes[1].hist(skewed_data, bins=30)
axes[1].axvline(np.mean(skewed_data), color="red", label="Mean")
axes[1].axvline(np.median(skewed_data), color="green",
                linestyle="--", label="Median")
axes[1].set_title("Skewed Distribution (একদিকে লম্বা লেজ)")
axes[1].legend()

plt.tight_layout()
plt.show()
