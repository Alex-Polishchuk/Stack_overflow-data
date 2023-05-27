import pandas as pd
import csv
import requests


def excel_reader(path, df_name):
    df_name = pd.read_excel(path)

    print(df_name.head())

excel_reader(r"Data\NBT21MTT_Outputs.xlsx","df_M-T")

