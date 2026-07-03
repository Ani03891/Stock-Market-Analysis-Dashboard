import os
import pandas as pd
csv_folder = "output_csv"
csv_files = os.listdir(csv_folder)
all_data = []
for file in csv_files:
    file_path = os.path.join(csv_folder,file)
    df = pd.read_csv(file_path)
    all_data.append(df)
print(len(all_data))
master_df =pd.concat(all_data,ignore_index = True)
print(master_df.head())
print(master_df.shape)
master_df.to_csv("master_stock_data.csv",index=False)
print("Master file saved")


