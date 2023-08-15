import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

plt.style.use('ggplot')
pd.set_option("display.max_columns", 200)

df = pd.read_csv('coaster_db.csv')

''' understanding of data (just see what we have) '''

# print(df.shape) -- see the rows and columns number
# print(df.columns) -- to see all columns
# print(df.dtypes) -- to see types of columns
# print(df.describe()) -- see different statistics

''' now i will Clean data '''

# print(df.columns)

df = df[['coaster_name',
         # 'Length', 'Speed',
         'Location', 'Status',
         # 'Opening date',
         # 'Type',
         'Manufacturer',
         # 'Height restriction', 'Model', 'Height',
         # 'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
         # 'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
         # 'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
         # 'Track layout', 'Fastrack available', 'Soft opening date.1',
         # 'Closing date',
         # 'Opened',
         # 'Replaced by', 'Website',
         # 'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
         # 'Single rider line available', 'Restraint Style',
         # 'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
         'year_introduced', 'latitude', 'longitude', 'Type_Main',
         'opening_date_clean',
         # 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
         'speed_mph',
         # 'height_value', 'height_unit',
         'height_ft', 'Inversions_clean', 'Gforce_clean']].copy()

# print(df.shape)

# so I copied names of columns using df.columns and edited it.
# there is a way to delete columns using DROP, but in this situation
# it is faster

# print(df.dtypes)

# I noticed that 'opening_date_clean' is an OBJECT, so I want to change it in date

df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])

# print(df.dtypes)

# now I don't like the names, because some of them starts with lower case

df = df.rename(columns={'coaster_name': 'Coaster_Name',
                        'year_introduced': 'Year_Introduced'})

# print(df.columns)

# now I want to check if we have missing values

# df.isna().sum()

# see if there are duplicates

# df.loc[df.duplicated()]

# print(df.loc[df.duplicated(subset=['Coaster_Name'])])

df = df.loc[~df.duplicated(subset=['Coaster_Name', 'Location', 'opening_date_clean'])].reset_index(drop=True).copy()

# print(df.shape)

''' Visualization & analysis'''

ax = df['Year_Introduced'].value_counts().head(10).plot(kind='bar', title='Top 10 Years Coasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')
# plt.show()

axs = df['speed_mph'].plot(kind='hist', bins=20, title='Coaster Speed (mph)')
axs.set_xlabel('Speed (mph)')
# plt.show()

df.plot(kind='scatter',
        x='speed_mph',
        y='height_ft',
        title='Coaster Speed vs Height')
# plt.show()

sns.scatterplot(x='speed_mph',
                y='height_ft',
                hue='Year_Introduced',
                data=df)

sns.pairplot(df, vars=['Year_Introduced', 'speed_mph',
                       'height_ft', 'Inversions_clean', 'Gforce_clean'],
             hue='Type_Main')

# I will show correlation

"""
df_corr = df[['Year_Introduced', 'speed_mph',
              'height_ft', 'Inversions_clean',
              'Gforce_clean']].dropna().corr()

sns.heatmap(df_corr, annot=True)"""

# plt.show()

''' if we want to find (for example) __ what are the locations with fastest roller coasters (min 10)'''

"""
df.query('Location != "other"') \
    .groupby('Location')['speed_mph']\
    .agg(['mean', 'count'])\
    .query('count >= 10')\
    .sort_values('mean')['mean'].plot(kind='barh', title='Average coaster speed by location')
"""
plt.show()
