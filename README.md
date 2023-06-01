# Xander_Project, going through the stack overflow yearly survey to find out some interesting insights
This project includes the importing, cleaning, transformation, storage and visualisation of the raw data from the 2022 stack overflow (SO) survey

### This repository: 
**Data:**

**Folder** named **Data**; contains, unsurprisingly, the raw data which has been cleaned to fit the max gitHub file size. This contains the original survey data as well as the clean data with renamed columns

**Folder** named **Visualise_Data**; contains csv files which have been transformed ready for visualisations from the survey data, ready to be visualised with seaborn or powerBI.

**Folder** named **Database**; contains SQL database files which have been transformed and ready for storage.

**Notebooks:**


**File** named *programming_language_split.ipynb*; calculates the number of developers who use / want to learn certain programming languages and database technologies

**File** named *python_data_vis.ipynb*; showcasing some python visualisations with some simpler data in the survey

**File** named *column_rename.ipynb*; renames the columns of stack overflow data for clarity

**File** named *data_to_fitSize.ipynb*; removes unnecessary data so that raw data can fit into 100MB file size limit, original file can be found [here](https://insights.stackoverflow.com/survey)

**File** named *population_count.ipynb*; cleans population data, calculates the per capita number of respondents to the stack overflow. Original file can be found [here](https://data.worldbank.org/indicator/SP.POP.TOTL)

**File** named *store_as_db.ipynb*; store the csv files using sql database for alternate storage method

Dependencies Required:
Pandas
openpyxl
MatPlotLib
Plotly
SQLLite3