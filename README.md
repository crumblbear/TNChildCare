# **Welcome!**
We are CrumbleBear, an organization designed to help Chattanooga based organizations leverage their data through visualization, automation, and integration so they can align, communicate, and shift effort towards serving the mission. In those efforts we work with a lot of local data. One such dataset is TN Child Care which is the basis of this repository and analysis.

# **What is the Purpose?**
We hope to accomplish a few things with this analysis and subsequent LinkedIn series. The primary objective is to take others on the journey of a data analytics/visualization project, and peal back the curtain on the work involved with such projects. This work will cover data extraction, automation, transformation, integration/loading, and visualization. 

While this project focuses on a TN Child Care dataset, our goal is for others to find parallels between the work in this project and the work they perform day to day. Whether that is finding similar needs in automating a data capture process that is manual today, or integrating data across two systems utilized in the organization.

Since we are also community focused, we thought what better dataset then one impacting families in the Chattanooga area: Child Care.

# **TN Child Care/Census Datasets**
Our analysis will use the TN Child Care dataset currently housed on the chattadata.org website. This dataset includes all of TN but we will filter it down to Hamilton County. 

We will also pull Census data to better understand trends and current child care capacity for the Hamilton County population.

# **Files**
## *Python Files*
There are two Python files included: 1 Jupyter Notebook and 1 Python file. The Python file stores the latest production code, while the notebook can contain test code. 

We will work to keep the code well commented so that others can follow the transformation process. At a high level, the Python script pulls down TN Child Care data from [ChattaData: TN Child Care](https://www.chattadata.org/Education/TN-Child-Care/3gj8-3ijm) via the available API. This piece is important because it will ultimately allow us to automate the data capture inside our Power BI visulalizaton.

While we have performed a number of transmations inside Python, additional transformation are also performed directly inside Power BI.

## *Power BI File*
This file contains all visualizations performed during the analysis and will evolve as the project evolves.

# Citations
- [ChattaData](https://www.chattadata.org/)
- [Census Data](https://www.census.gov/data.html)
