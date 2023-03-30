## Welcome!
We are CrumbleBear, an orgainization designed to help Chattanooga based organizations leverage their data through visualization, automation, and integration to align, communicate, and shift effort towards serving the mission. In those efforts we work with a lot of local data. One such dataset is TN Child Care which is the basis of this repository and analysis.

### What is the Purpose?
We hope to occomplish a few things with this analysis and subsequnt LinkedIn series. The primary objective is to take others on the journey of a data analytics/visualizaion project, and peal back the curtain on the work involved with such projects. This work will cover data extraction, automation, transformation, integration/loading, and visualization. 

While this project focuses on a TN Child Care dataset, our goal is for others to find parallels between the work in this project and the work they perform day to day. Whether that is finding similar needs in automating a data capture process that is manual today, or integrating data across two systems utilized in the organization.

Since we are also community focused, we thought what better dataset then one impacting manual families in the Chattanooga area: Child Care.

# TN Child Care/Census Datasets
Our analysis will use the TN Child Care dataset currently housed on the chattadata.org website. 

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
