import pandas as pd
import requests
import json
import credentials as cred
from dotenv import load_dotenv
import os 

# Setting header and data components for API request
headers = {
    'Authorization': os.environ.get('AUTHORIZATION'),
    'Accept': 'application/json',
    'Content-type': 'application/json',
}

data = {
    'app_token': os.environ.get('APPTOKEN'),
}

# Performing API call to ChattaData's TN Child Care dataset. If an error occurs, the program exits
try:
    response = requests.get('https://www.chattadata.org/resource/3gj8-3ijm.json?county=HAMILTON', data=data)
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f'The following error occured while making the get request: {err}')
    raise SystemExit()

dataframe = pd.json_normalize(response.json())

# Function that houses many of the data transformations on the dataset
def dataframeMods(dataframe):

    # Converting date fields to a date/time format
    dataframe[['license_approval_date', 'date_open']] = dataframe[['license_approval_date', 'date_open']].apply(pd.to_datetime, yearfirst=True, unit='ns', errors='coerce') #Some dates are invalid so set errors to 'coerce' to fill with NaN

    # Separating the Location Point column into individual Latitude and Longitude fields
    dataframe[['long', 'lat']] = dataframe['location_point.coordinates'].apply(lambda x: pd.Series(x))

    # Extracting the alpha interavals from the age columns to create number and category columns
    dataframe[['minimum_age_num', 'minimum_age_cat']] = dataframe['minimum_age'].str.extract(r'(\d+)([a-zA-Z]+)')
    dataframe[['maximim_age_num', 'maximum_age_cat']] = dataframe['maximum_age'].str.extract(r'(\d+)([a-zA-Z]+)')

    # Standardizing minimum age into a yearly basis
    dataframe.loc[dataframe['minimum_age_cat'] == 'WK', 'minimum_age_num'] = dataframe['minimum_age_num'].astype(int) / 52
    dataframe.loc[dataframe['minimum_age_cat'] == 'MO', 'minimum_age_num'] = dataframe['minimum_age_num'].astype(int) / 12
    dataframe.loc[dataframe['minimum_age_cat'] == 'YR', 'minimum_age_num'] = dataframe['minimum_age_num'].astype(int)

    # Standardizing the format of Agency Name
    dataframe['agency_name'] = dataframe['agency_name'].str.title()

    # Converting Open and Close Times into military format for future analysis
    dataframe['open_time'] = pd.to_datetime(dataframe['open_time'], format='%I:%M %p').dt.strftime('%H:%M')
    dataframe['close_time'] = pd.to_datetime(dataframe['close_time'], format='%I:%M %p').dt.strftime('%H:%M')

    return dataframe

dataframe = dataframeMods(dataframe)

# This chain method is dropping unncessary columns, 
# Corrects the mailing state column name,
# Converts Ys and Ns to 1s and 0s
# Creates a Unique column per Agency and drops duplicate records
final_df = (dataframe
.drop(columns=['agency_phone', 'agency_contact', 'mailing_street', 'mailing_city', 'mialing_state', 'mailing_zip', 'no_smoking', 'no_dogs', 'no_cats', 'no_pets', 'child_and_adult_care_food', 'program_evaluator', 'program_evaluator_phone_number', 
    'report_date_beginning_of_month', 'location_point.coordinates', 'license_approval_date', 'unique_id']) # Mailing state is misspelled in the dataset
.replace(['Y', 'N'], [1, 0])
.assign(agency_name_age = dataframe['agency_name'].astype(str) + dataframe['minimum_age'].astype(str))
.drop_duplicates(subset=['agency_name_age'], keep='last')
.drop(columns=['agency_name_age'])
.reset_index(drop=True)
)

#final_df.to_csv('tn_child_care.csv', index=False)