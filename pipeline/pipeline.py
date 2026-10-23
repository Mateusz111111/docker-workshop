import sys
import pandas as pd

print('arguments:', sys.argv)

month = int(sys.argv[1]) if len(sys.argv) > 1 else 0


df = pd.DataFrame({"day" : [1, 2], "num_passengers" : [3, 4]})
print(df.head())

df.to_parquet(f"data/passengers_{month}.parquet")
print(f"Hello pipeline for month {month}")


