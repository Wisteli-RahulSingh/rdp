# rdp


http://54.156.114.207/

json_data = json.loads(data)

# Normalize JSON data into a structured DataFrame with prefixed column names
df = pd.json_normalize(
    json_data,
    'observationRequestSegments',
    ['placerID', 'observationDateTime', 'isFinal', ('recordID', 'observationRequestRecordID')]
)
df = df.explode('observationSegments').reset_index(drop=True)
df = pd.concat([df.drop(['observationSegments'], axis=1), df['observationSegments'].apply(pd.Series)], axis=1)

# Print the DataFrame
print(df)








