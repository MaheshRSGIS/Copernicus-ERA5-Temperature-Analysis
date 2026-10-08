#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
print(sys.executable)


# In[3]:


import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import netCDF4
import cdsapi
import os

print("Everything is working!")


# In[4]:


os.chdir("C:/Users/MAHESH MAJUMDER")
os.getcwd()


# In[5]:


print(os.path.exists(r"C:\Users\MAHESH MAJUMDER\.cdsapirc"))


# In[6]:


client = cdsapi.Client()
print("CDS API is working!")


# In[7]:


file_path = r"E:\TemperatureData\reanalysis-era5-land-timeseries-sfc-2m-temperaturenwrbkq8f.nc"

ds = xr.open_dataset(file_path)

print("File opened successfully!")
print("Dimensions:", ds.dims)
print("Variables:", list(ds.data_vars))
print("Coordinates:", list(ds.coords))
print(ds)


# In[8]:


print(ds["t2m"].attrs)


# In[9]:


temperature_c = ds["t2m"] - 273.15
temperature_c.attrs["units"] = "°C"
print(temperature_c)


# In[10]:


print(ds.latitude.values)
print(ds.longitude.values)


# In[11]:


study_temp = temperature_c.mean(
    dim=["latitude", "longitude"]
)
print(study_temp)


# In[12]:


df = study_temp.to_dataframe(name="temperature_C")
df.head()


# In[13]:


print("Dimensions:")
print(ds.dims)

print("\nCoordinates:")
print(list(ds.coords))

print("\nVariables:")
print(list(ds.data_vars))


# In[14]:


print(ds["t2m"].dims)
print(ds["t2m"].shape)


# In[15]:


print("study_temp dimensions:", study_temp.dims)
print("study_temp coordinates:", list(study_temp.coords))


# In[16]:


print(study_temp.valid_time.min().values)
print(study_temp.valid_time.max().values)


# In[17]:


monthly_temp = study_temp.resample(
    valid_time="1MS"
).mean()


# In[18]:


print(monthly_temp)


# In[19]:


monthly_df = monthly_temp.to_dataframe(
    name="temperature_C"
).reset_index()

print(monthly_df.head())


# In[20]:


annual_temp = study_temp.resample(
    valid_time="1YS"
).mean()


# In[21]:


annual_df = annual_temp.to_dataframe(
    name="temperature_C"
).reset_index()

print(annual_df.head())


# In[22]:


annual_df["year"] = annual_df["valid_time"].dt.year

print(annual_df.head())


# In[23]:


plt.figure(figsize=(12, 5))

plt.plot(
    annual_df["year"],
    annual_df["temperature_C"]
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Annual Mean Temperature")

plt.grid(True)

plt.show()


# In[25]:


from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(
    annual_df["year"],
    annual_df["temperature_C"]
)

print("Temperature trend =", slope, "°C/year")
print("Temperature trend =", slope * 10, "°C/decade")
print("R² =", r_value**2)
print("p-value =", p_value)


# In[26]:


trend = intercept + slope * annual_df["year"]

plt.figure(figsize=(12, 5))

plt.plot(
    annual_df["year"],
    annual_df["temperature_C"],
    label="Annual Mean Temperature"
)

plt.plot(
    annual_df["year"],
    trend,
    linestyle="--",
    label=f"Trend = {slope*10:.3f} °C/decade"
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Annual Temperature Trend")

plt.legend()
plt.grid(True)

plt.show()


# In[27]:


summer_temp = monthly_temp.where(
    monthly_temp.valid_time.dt.month.isin([5, 6, 7, 8, 9]),
    drop=True
)


# In[28]:


summer_annual = summer_temp.resample(
    valid_time="1YS"
).mean()


# In[29]:


summer_df = summer_annual.to_dataframe(
    name="summer_temperature_C"
).reset_index()

summer_df["year"] = summer_df["valid_time"].dt.year

print(summer_df.head())


# In[30]:


plt.figure(figsize=(12, 5))

plt.plot(
    summer_df["year"],
    summer_df["summer_temperature_C"]
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("May–September Mean Temperature")

plt.grid(True)

plt.show()


# In[31]:


os.chdir("E:\TemperatureData")


# In[32]:


annual_df.to_csv(
    r"E:\TemperatureData\annual_temperature.csv",
    index=False
)


# In[33]:


monthly_df.to_csv(
    r"E:\TemperatureData\monthly_temperature.csv",
    index=False
)


# In[34]:


summer_df.to_csv(
    r"E:\TemperatureData\summer_temperature.csv",
    index=False
)

