# function
def parse_vitals(file): # json file
    data = file['patientVitals']
    df = pd.json_normalize(data, record_path=['observationSets', 'observationSegments'], 
                  meta=['dateOfService', 'recordID', ['observationSets', 'rank'],
                        ['observationSets', 'setID']])
    return df
 
