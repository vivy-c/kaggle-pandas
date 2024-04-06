import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")

# Your code here
desc = reviews.description

first_description = reviews.description[0]

first_row = reviews.iloc[0]

first_descriptions = desc.head(10)

indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

cols = ['country', 'variety']
df = reviews.loc[:99, cols]

italian_wines = reviews[reviews.country == 'Italy']

italian_wines = reviews[reviews.country == 'Italy']