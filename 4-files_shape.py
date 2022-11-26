import pandas as pd
 
df_2013 = pd.read_csv("citibike_final_2013.csv", sep="\t")
df_2013_name = 'citibike_final_2013'
df_2013_shape= df_2013.shape

df_2018 = pd.read_csv("citibike_final_2018.csv", sep="\t")
df_2018_name = 'citibike_final_2018'
df_2018_shape= df_2018.shape

df_2020 = pd.read_csv("citibike_final_2020.csv", sep="\t")
df_2020_name = 'citibike_final_2020'
df_2020_shape= df_2020.shape



data = {'File name':[df_2013_name,df_2018_name,df_2020_name],'Shape': [df_2013_shape,df_2018_shape,df_2020_shape]}
final_df = pd.DataFrame(data)
print(final_df)
