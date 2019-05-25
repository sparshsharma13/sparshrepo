#!/usr/bin/env python3
import pandas as pd
import numpy as np
df=pd.read_csv("flightdelays.csv")
data=df[df['Origin']=='SFO']['ArrDelay'].head(3)
data.to_csv("first3sfo.csv")
first3sfo=pd.read_csv("first3sfo.csv" , header=None)[1]
print(first3sfo)
dest=df['Dest'].value_counts().head(3)
print(dest)
print("Sparsh Sharma")
