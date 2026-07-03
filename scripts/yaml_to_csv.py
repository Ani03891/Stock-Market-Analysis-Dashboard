import os
import yaml
import pandas as pd
data_folder = "Data"
output_folder = "output_csv"
os.makedirs(output_folder,exist_ok=True)
print("Folders ready")
yaml_files = os.listdir(data_folder)
for month_path in yaml_files:
    month_path = os.path.join(data_folder,month_path)
    if os.path.isdir(month_path):
         print(month_path)
         month_files = os.listdir(month_path)
         for file in month_files:
             print(file)
             file_path = os.path.join(month_path,file)
             print(file_path)
             with open(file_path,"r",encoding="utf-8") as f:
                data = yaml.safe_load(f)
                df= pd.DataFrame(data)
                csv_name = file.replace(".yaml",".csv")
                csv_path= os.path.join(output_folder,csv_name)
                df.to_csv(csv_path,index=False)
             print(f"{csv_name} saved")


   
    
        



