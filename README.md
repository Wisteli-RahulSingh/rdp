# rdp


http://54.156.114.207/

https://stackoverflow.com/questions/72397751/converting-keys-of-pandas-df-of-dictionaries-to-columns-and-values-as-data

df = pd.concat([df.drop('Data', axis=1), df['Data'].apply(pd.Series)], axis=1)

df = pd.concat([df.drop('Data', axis=1), pd.json_normalize(df['Data'])], axis=1)


# Check for existing columns before unpacking dictionary values
new_cols = pd.DataFrame(df['Data'].tolist()).add_prefix('Data')


df2 = df.drop('Data', axis=1).join(new_cols.loc[:, ~new_cols.columns.duplicated()])

new_cols = json_normalize(df['Data']).add_prefix('Data')

df2 = df.drop('Data', axis=1).join(new_cols)


df_combined = pd.concat([df.drop('Data', axis=1), pd.json_normalize(df['Data'])], axis=1)


df_combined = pd.concat([df.drop('Data', axis=1), pd.DataFrame([{k: v for k, v in d.items()} for d in df['Data']])], axis=1)






