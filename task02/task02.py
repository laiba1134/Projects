import pandas 
df = pandas.read_csv("data.csv",header=None)
df.columns = ['station', 'date', 'observation', 'value', 'mflag', 'qflag', 'sflag', 'obstime']
df.to_csv("data_h.csv",index=False)