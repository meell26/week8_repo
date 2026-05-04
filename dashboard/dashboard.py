import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../features/features.csv")

df.plot(kind='bar')
plt.title("Threat Features")
plt.show()