ERA5-Land Temperature Trend Analysis Using Python

OVERVIEW:

This project analyzes 2 m air temperature data from the ERA5-Land reanalysis dataset using Python. It processes NetCDF climate data to examine monthly and annual temperature variations, estimate long-term temperature trends, and investigate May–September temperature patterns.

OBJECTIVES:

Process ERA5-Land temperature data in NetCDF format.
Convert temperature values from Kelvin to degrees Celsius.
Calculate spatially averaged temperature across available latitude and longitude grid cells.
Generate monthly and annual mean temperature time series.
Estimate temperature trends using linear regression.
Analyze May–September mean temperature variations.
Export processed datasets as CSV files.

DATA AND METHODOLOGY:

The analysis uses the t2m variable, representing 2 m air temperature, with temporal and spatial coordinates. The Python library xarray is used to open and process the multidimensional dataset.

Temperature values are converted from Kelvin to Celsius by subtracting 273.15. Spatial averaging is performed across the available latitude and longitude dimensions to produce a regional time series.

The spatially averaged temperature series is resampled to calculate monthly and annual means. Annual temperature values are visualized using Matplotlib. The scipy.stats.linregress function estimates the linear temperature trend, expressed in °C/year and °C/decade. The analysis also calculates R² and the p-value to help interpret the regression results.

For seasonal analysis, monthly temperature values from May through September are selected and averaged by year. The resulting series is plotted to examine variations during this period.

LIBRARIES USED:
Python: Programming and analysis
xarray: Multidimensional climate data processing
NumPy: Numerical operations
pandas: Time-series processing and CSV export
Matplotlib: Data visualization
SciPy: Statistical analysis and linear regression
netCDF4: NetCDF data support

AUTHOR:
Mahesh Majumder

RESEARCH AREAS: 
Cryosphere and Glaciology, Climate data analysis, remote sensing, GIS, and geospatial applications.
