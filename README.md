# TNChildCare
An analysis of child care in Hamilton County, TN. 

There are several files used in this analysis.

### Python Script
The Python script pulls down TN Child Care data from https://www.chattadata.org/Education/TN-Child-Care/3gj8-3ijm via the available API. The primary purpose of the script is to automate the data caputre via the API and perform initial data transformation to get data prepared for Power BI. The transformations inside Python are minimal since additional transformations will be performed in Power BI.

### Power BI

- Total Years: Standardized age ranges served into years. We do this by adding 1 to Maximum Age and subtracting Minimum Age (rounded down)
- Yearly Capacity: Total Years multipied by Capacity (rounded up)
- Filter off agencies with a minimum age of 5 or more to align with Census

### Citations
chattadata.org: https://www.chattadata.org/
census data: https://www.census.gov/data.html
