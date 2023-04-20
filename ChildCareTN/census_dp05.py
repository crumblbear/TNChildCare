import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

df = pd.DataFrame()
years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
key = os.environ.get('CENSUS_KEY')
fields_pre_2017 = 'DP05_0001E,DP05_0005E,DP05_0006E,DP05_0007E,DP05_0059E,DP05_0060E,DP05_0061E,DP05_0062E,DP05_0063E,DP05_0064E'
fields_post_2016 = 'DP05_0001E,DP05_0005E,DP05_0006E,DP05_0007E,DP05_0064E,DP05_0065E,DP05_0066E,DP05_0067E,DP05_0068E,DP05_0069E'
zip_codes = '37302,37315,37321,37341,37343,37350,37363,37373,37377,37379,37402,37403,37404,37405,37406,37407,37408,37409,37410,37411,37412,37415,37416,37419,37421'

field_mapping_post_2016 = {
    'DP05_0001E': 'TOTAL POPULATION',
    'DP05_0005E': 'TOTAL POPULATION_UNDER 5 YEARS',
    'DP05_0006E': 'TOTAL POPULATION_5 TO 9 YEARS',
    'DP05_0007E': 'TOTAL POPULATION_10 TO 14 YEARS',
    'DP05_0064E': 'TOTAL POPULATION_WHITE',
    'DP05_0065E': 'TOTAL POPULATION_BLACK OR AFRICAN AMERICAN',
    'DP05_0066E': 'TOTAL POPULATION_AMERICAN INDIAN AND ALASKA NATIVE',
    'DP05_0067E': 'TOTAL POPULATION_ASIAN',
    'DP05_0068E': 'TOTAL POPULATION_NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER',
    'DP05_0069E': 'TOTAL POPULATION_SOME OTHER RACE',
    "zip code tabulation area": "ZIPCODE",
}

fields_mapping_pre_2017 = {
'DP05_0001E': 'TOTAL POPULATION',
'DP05_0005E': 'TOTAL POPULATION_UNDER 5 YEARS',
'DP05_0006E': 'TOTAL POPULATION_5 TO 9 YEARS',
'DP05_0007E': 'TOTAL POPULATION_10 TO 14 YEARS',
'DP05_0059E': 'TOTAL POPULATION_WHITE',
'DP05_0060E': 'TOTAL POPULATION_BLACK OR AFRICAN AMERICAN',
'DP05_0061E': 'TOTAL POPULATION_AMERICAN INDIAN AND ALASKA NATIVE',
'DP05_0062E': 'TOTAL POPULATION_ASIAN',
'DP05_0063E': 'TOTAL POPULATION_NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER',
'DP05_0064E': 'TOTAL POPULATION_SOME OTHER RACE',
"zip code tabulation area": "ZIPCODE",
}


for year in years:

    if df.empty:
        url_pre_2020 = f'https://api.census.gov/data/{year}/acs/acs5/profile?get=NAME,{fields_pre_2017}&for=zip%20code%20tabulation%20area:{zip_codes}&in=state:47&key={key}'        
        response = requests.request(url=url_pre_2020, method="GET")
        response.raise_for_status()
        data = response.json()

        df=pd.DataFrame(data[1:], columns=data[0]).rename(columns=fields_mapping_pre_2017)
        df['YEAR'] = year
        df.drop(columns=['NAME', 'state'],inplace=True)

    elif year in ['2011', '2012', '2013', '2014', '2015', '2016',]:
        url_pre_2020 = f'https://api.census.gov/data/{year}/acs/acs5/profile?get=NAME,{fields_pre_2017}&for=zip%20code%20tabulation%20area:{zip_codes}&in=state:47&key={key}'
        response = requests.request(url=url_pre_2020, method="GET")
        response.raise_for_status()
        data = response.json()

        df2=pd.DataFrame(data[1:], columns=data[0]).rename(columns=fields_mapping_pre_2017)
        df2.drop(columns=['NAME', 'state'],inplace=True)
        df2['YEAR'] = year
        df = pd.concat([df, df2], axis=0)

    elif year in ['2017', '2018', '2019']:
        url_pre_2020 = f'https://api.census.gov/data/{year}/acs/acs5/profile?get=NAME,{fields_post_2016}&for=zip%20code%20tabulation%20area:{zip_codes}&in=state:47&key={key}'
        response = requests.request(url=url_pre_2020, method="GET")
        response.raise_for_status()
        data = response.json()

        df2=pd.DataFrame(data[1:], columns=data[0]).rename(columns=field_mapping_post_2016)
        df2.drop(columns=['NAME', 'state'],inplace=True)
        df2['YEAR'] = year
        df = pd.concat([df, df2], axis=0)
    else:
        url_post_2019 = f'https://api.census.gov/data/{year}/acs/acs5/profile?get=NAME,{fields_post_2016}&for=zip%20code%20tabulation%20area:{zip_codes}&key={key}'
        response = requests.request(url=url_post_2019, method="GET")
        response.raise_for_status()
        data = response.json()

        df2=pd.DataFrame(data[1:], columns=data[0]).rename(columns=field_mapping_post_2016)
        df2.drop(columns=['NAME',],inplace=True)
        df2['YEAR'] = year
        df = pd.concat([df, df2], axis=0)

city_mapping = {
    '37302': 'Apison',
    '37315': 'Collegedale',
    '37321': 'Dayton',
    '37341': 'Harrison',
    '37343': 'Hixson',
    '37350': 'Lookout Mountain',
    '37363': 'Ooltewah',
    '37373': 'Sale Creek',
    '37377': 'Signal Mountain',
    '37379': 'Soddy Daisy',
    '37402': 'Chattanooga',
    '37403': 'Chattanooga',
    '37404': 'Chattanooga',
    '37405': 'Chattanooga',
    '37406': 'Chattanooga',
    '37407': 'Chattanooga',
    '37408': 'Chattanooga',
    '37409': 'Chattanooga',
    '37410': 'Chattanooga',
    '37411': 'Chattanooga',
    '37412': 'Chattanooga',
    '37415': 'Chattanooga',
    '37416': 'Chattanooga',
    '37419': 'Chattanooga',
    '37421': 'Chattanooga',
}

df = df.reset_index(drop=True)
df['CITY'] = df['ZIPCODE'].map(city_mapping)