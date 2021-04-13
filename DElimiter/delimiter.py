"""
This very basic script was written to clean up some csv files with multiple delimiters. 
It could probably be done a lot easier in excel, but what's the fun in that?
"""

import pandas as pd
import yaml 

with open('vars.yaml') as f:

    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    print(yaml_data)
    file = yaml_data["file"]
    print(file)



data = pd.read_csv(file, sep='[,|/|&]', engine='python') # add or remove delimiters here as needed, they can be separated by the | symbol
print(data)
data.to_csv(r'./output.csv', index=False)
