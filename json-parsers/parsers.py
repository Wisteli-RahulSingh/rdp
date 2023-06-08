import json
import pandas as pd


# vitals parser
def parse_vitals(file): # json file
    data = file['patientVitals']
    df = pd.json_normalize(data, record_path=['observationSets', 'observationSegments'], 
                  meta=['dateOfService', 'recordID', ['observationSets', 'rank'],
                        ['observationSets', 'setID']])
    return df
 
    
# medications parser
def parse_medications(file): # josn file
    df = pd.json_normalize(file['patientMedications'])
    return df


# patient demographics parser
def flatten_demographics(nested_data, parent_key=''): # helper function
    flatten_data = {}
    if isinstance(nested_data, dict):
       for key, value in nested_data.items():
           new_key = parent_key + '.' + key if parent_key else key
           flatten_data.update(flatten_demographics(value, new_key))
    elif isinstance(nested_data, list):
        for i, item in enumerate(nested_data):
            new_key = parent_key + '.' + str(i) if parent_key else str(i)
            flatten_data.update(flatten_demographics(item, new_key))
    else:
       flatten_data[parent_key] = nested_data
    return flatten_data   

def parse_demographics(file): # json file
    data = file['patientDemographics']
    flatten_data = flatten_demographics(data)
    df = pd.DataFrame.from_records([flatten_data])
    return df


# parse problems
def parse_problems(file): # json file
    df = pd.json_normalize(file['patientProblems'], max_level=1)
    concept_mapping_cols = [col for col in df.columns if col.startswith("conceptMappings.")]
    df = df.explode(concept_mapping_cols)
    return df
