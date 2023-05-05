import os
import pandas as pd
import matplotlib.pyplot as plt


#rcparams = run configuration parameters

os.system('tput reset')

###########
#input_file = "C:\\....\\consumer_complaints.csv"
#dataset = pd.read_csv(input_file)
#df = pd.DataFrame(dataset)
#cols = [1,2,3,4]
#df = df[df.columns[cols]]
###########


file = 'thai/thai-export/export 2012 August 39011019090.csv'

dataframe = pd.read_csv(file)

columns = [2, 3]

dataframe = dataframe[dataframe.columns[columns]]

dataframe.plot()

plt.xlabel('Time step')
plt.ylabel('Price')

plt.show()
