import pandas as pd
import matplotlib.pyplot as plt


#rcparams = run configuration parameters

df = pd.read_csv('thai/thai-export/export 2012 August 39011019090.csv')

df.plot()

plt.show()
