import pandas as pd
import ydata_profiling as pp

df = pd.read_csv('mentalStressDataSet.csv')
df.head

profile = pp.ProfileReport(df)
profile.to_file(output_file="ActualReport.html")