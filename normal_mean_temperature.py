import fitgrid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import datetime



filename_nrmlmeantemp = "nrmlmeantemp.csv"
fields = []
rows = []
temperature_data = pd.read_csv(
    filename_nrmlmeantemp,
    usecols=['LOCATION', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])

print(temperature_data)
months_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
n_timestamps = len(months_list)
n_epochs = len(temperature_data.LOCATION)
print(n_timestamps)
print(n_epochs)
temperature_dataframe = pd.DataFrame()


for i in range(n_epochs):
    for j in range(n_timestamps):
        #print(temperature_data.LOCATION[i])
        temperature_dataframe = temperature_dataframe.append(
            {
                #'epochs': 1 + i,

                'epochs':(temperature_data.LOCATION[i]),
                #'times': 100 * np.tile(range(n_timestamps), n_epochs),
                'times': months_list[j],
                #'temperature': np.random.random(n_timestamps * n_epochs),
                'temperature': temperature_data.iloc[i][j+1]
            },
            ignore_index=True
        )
    #temperature_dataframe[temperature_data.LOCATION[i]].apply(lambda x: str(x)).unique()

# this index is required!
temperature_dataframe.set_index(['epochs', 'times'], inplace=True)
print(temperature_dataframe)






epochs_fg = fitgrid.epochs_from_dataframe(
    temperature_dataframe,
    time='times',
    #epoch_id=temperature_data.LOCATION,
    epoch_id = "epochs",
    channels=['temperature']
)


print(epochs_fg)


lm_grid = fitgrid.lm(
    epochs_fg,
    RHS='temperature'
)
