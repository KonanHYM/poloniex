#coding:utf-8
import pandas as pd
import numpy as np

filefullpath = "/Users/Konan/Downloads/Chapter 4_StudentReview.xlsx"
df = pd.read_excel(filefullpath,skiprows=[0])
print df
print type(df)
