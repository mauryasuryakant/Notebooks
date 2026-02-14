from collect_data import collected_data as cd
import pandas as pd

df = pd.read_csv("../linear-data.csv")
print(cd.data_2d(df, 1))