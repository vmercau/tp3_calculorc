import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("tp3.csv",sep=r'\s*,\s*',header=0, engine='python')
Y = df['Tiempo promedio'].tolist()
X = df['RC(FΩ)'].tolist()
yerr=df['error t'].tolist()
xerr=df['error RC'].tolist()


print(xerr)
z, residuals, rank, singular_values, rcond = np.polyfit(X, Y, 1, full=True)
print("residuals RC")
print(residuals)
p = np.poly1d(z)
plt.plot(X,p(X),"r--",color='red')
plt.errorbar(X, Y,xerr=xerr,yerr=yerr)
#plt.set_title('Resistores A y B en Serie', fontsize=14)
plt.xlabel('RC (FΩ = s)',fontsize=18)
plt.ylabel('Tiempo promedio (s)',fontsize=18)
plt.title('Tiempo característico', fontsize=20)
plt.show()

