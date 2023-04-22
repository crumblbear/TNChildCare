import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

key = os.environ.get('CENSUS_KEY')
zip_codes = '37302,37315,37321,37341,37343,37350,37363,37373,37377,37379,37402,37403,37404,37405,37406,37407,37408,37409,37410,37411,37412,37415,37416,37419,37421'
detail_tables = {
    'B01001A_003E': 'WHITE MALE',
    'B01001A_018E': 'WHITE FEMALE',
    'B01001B_003E': 'BLACK OR AFRICAN AMERICAN MALE',
    'B01001B_018E': 'BLACK OR AFRICAN AMERICAN FEMALE',
    'B01001C_003E': 'AMERICAN INDIAN AND ALASKA NATIVE MALE',
    'B01001C_018E': 'AMERICAN INDIAN AND ALASKA NATIVE FEMALE',
    'B01001D_003E': 'ASIAN MALE',
    'B01001D_018E': 'ASIAN FEMALE',
    'B01001E_003E': 'NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER MALE',
    'B01001E_018E': 'NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER FEMALE',
    'B01001F_003E': 'OTHER MALE',
    'B01001F_018E': 'OTHER FEMALE',
}
years = ['2011', '2021']
detail_table_fields = ",".join(detail_tables.keys())

df = pd.DataFrame()

for year in years:
    if df.empty:
        url_acs_detail = f'https://api.census.gov/data/{year}/acs/acs5?get=NAME,{detail_table_fields}&for=zip%20code%20tabulation%20area:{zip_codes}&in=state:47&key={key}'

        response = requests.request(url=url_acs_detail, method="GET")
        response.raise_for_status()
        data = response.json()

        df=pd.DataFrame(data[1:], columns=data[0]).rename(columns=detail_tables)
        df['YEAR'] = year
        df.drop(columns=['NAME','state'],inplace=True)

        city_mapping = {
            '37302': 'Apison',
            '37315': 'Collegedale',
            '37321': 'Dayton',
            '37341': 'Harrison',
            '37343': 'Hixson',
            '37350': 'Lookout Mtn',
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

        df = df.rename(columns={"zip code tabulation area": "ZIPCODE"})

        df['CITY'] = df['ZIPCODE'].map(city_mapping)
        df['WHITE'] = df['WHITE MALE'].astype(int) + df['WHITE FEMALE'].astype(int)
        df['BLACK OR AFRICAN AMERICAN'] = df['BLACK OR AFRICAN AMERICAN MALE'].astype(int) + df['BLACK OR AFRICAN AMERICAN FEMALE'].astype(int)
        df['AMERICAN INDIAN AND ALASKA NATIVE'] = df['AMERICAN INDIAN AND ALASKA NATIVE MALE'].astype(int) + df['AMERICAN INDIAN AND ALASKA NATIVE FEMALE'].astype(int)
        df['ASIAN'] = df['ASIAN MALE'].astype(int) + df['ASIAN FEMALE'].astype(int)
        df['NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER'] = df['NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER MALE'].astype(int) + df['NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER FEMALE'].astype(int)
        df['OTHER'] = df['OTHER MALE'].astype(int) + df['OTHER FEMALE'].astype(int)

        df = df.drop(columns=[column for column in detail_tables.values()])
    else:
        url_acs_detail = f'https://api.census.gov/data/{year}/acs/acs5?get=NAME,{detail_table_fields}&for=zip%20code%20tabulation%20area:{zip_codes}&key={key}'

        response = requests.request(url=url_acs_detail, method="GET")
        response.raise_for_status()
        data = response.json()

        df2=pd.DataFrame(data[1:], columns=data[0]).rename(columns=detail_tables)
        df2['YEAR'] = year
        df2.drop(columns=['NAME',],inplace=True)

        city_mapping = {
            '37302': 'Apison',
            '37315': 'Collegedale',
            '37321': 'Dayton',
            '37341': 'Harrison',
            '37343': 'Hixson',
            '37350': 'Lookout Mtn',
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

        df2 = df2.rename(columns={"zip code tabulation area": "ZIPCODE"})

        df2['CITY'] = df2['ZIPCODE'].map(city_mapping)
        df2['WHITE'] = df2['WHITE MALE'].astype(int) + df2['WHITE FEMALE'].astype(int)
        df2['BLACK OR AFRICAN AMERICAN'] = df2['BLACK OR AFRICAN AMERICAN MALE'].astype(int) + df2['BLACK OR AFRICAN AMERICAN FEMALE'].astype(int)
        df2['AMERICAN INDIAN AND ALASKA NATIVE'] = df2['AMERICAN INDIAN AND ALASKA NATIVE MALE'].astype(int) + df2['AMERICAN INDIAN AND ALASKA NATIVE FEMALE'].astype(int)
        df2['ASIAN'] = df2['ASIAN MALE'].astype(int) + df2['ASIAN FEMALE'].astype(int)
        df2['NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER'] = df2['NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER MALE'].astype(int) + df2['NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER FEMALE'].astype(int)
        df2['OTHER'] = df2['OTHER MALE'].astype(int) + df2['OTHER FEMALE'].astype(int)

        df2 = df2.drop(columns=[column for column in detail_tables.values()])
        df = pd.concat([df, df2], axis=0)
        df = df.reset_index(drop=True)

print(df)
df.to_csv('census_race_11_21.csv', index=False)