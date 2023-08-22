import pandas as pd

data = pd.read_json("206800.json")

print(data.to_string())