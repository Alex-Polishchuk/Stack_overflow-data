# Xander_Project

This project includes the importing, cleaning, transformation, storage and visualisation of the raw data from the 2022 stack overflow (SO) survey

**Folder** named **Data**; contains, unsurprisingly, the raw data which has been cleaned to fit the max gitHub file size. This contains the original survey data as well as the clean data with renamed columns

**Folder** named **Data**; contains csv files which have been transformed ready for visualisations from the survey data, ready to be visualised with seaborn or powerBI.

**File** named *column_rename.ipynb*; renames the columns of stack overflow data for clarity

**File** named *data_to_fitSize.ipynb*; removes unnecessary data so that raw data can fit into 100MB file size limit

**File** named *population_count.ipynb*; cleans population data, calculates the per capita number of respondents to the stack overflow (data is normalised)

**File** named *survey_result_explore.ipynb*; initial exploration of data, calculates the number of developers who use / want to learn certain programming languages and database technologies

Dependencies Required:
Pandas
openpyxl
MatPlotLib
Plotly