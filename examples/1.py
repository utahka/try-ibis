# %%

from urllib.request import urlretrieve

import ibis
from rich import print

ibis.set_backend("polars")

# %%
for i in range(1, 6):
    urlretrieve(
        f"https://raw.githubusercontent.com/pola-rs/polars/main/examples/datasets/foods{i}.csv",
        f"./csv/foods{i}.csv",
    )

# %%

q = ibis.read_csv("csv/foods1.csv")
print(q.compile().collect())
# %%
