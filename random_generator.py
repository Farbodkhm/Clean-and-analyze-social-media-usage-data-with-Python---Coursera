import random
import pandas as pd
import numpy as np


periods_long = 500

categories = ["Food", "Travel", "Fashion", "Fitness", "Music", "Culture", "Family", "Health"]

data = {
    "Date": pd.date_range(start='2021-01-01', periods=periods_long),
    "Category": [random.choice(categories) for _ in range(periods_long)],
    "Likes": np.random.randint(0, 10000, size=periods_long),
}

data = pd.DataFrame(data)

print(data.head(5))