# rdp


http://54.156.114.207/

https://stackoverflow.com/questions/72397751/converting-keys-of-pandas-df-of-dictionaries-to-columns-and-values-as-data

df = pd.concat([df.drop('Data', axis=1), df['Data'].apply(pd.Series)], axis=1)






