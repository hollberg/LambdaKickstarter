# """
# parse_data.py
# Read raw, merged kickstarter *.csv file for cleaning and processing
# """
#
# # *** IMPORTS ***
# import numpy as np
# import pandas as pd
# # import psycopg
#
#
# # *** READ DATA ***
# raw_file = 'data/Kickstarter_Merged_Data_With_Lat_Lng.csv'
#
# df_raw = pd.read_csv(raw_file)
#
# print(df_raw.head(1).T)
#
# print(df_raw.columns)
#
# # print(df_raw.value_counts('id'))
# print(df_raw.info())
# print(df_raw.describe())
#
# # Print column names and types
# columns = df_raw.columns
# types = df_raw.dtypes
#
# df = pd.DataFrame(list(zip(columns, types)), columns=['Col', 'DType'])
#
# print(df)
