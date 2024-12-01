import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Name': ['All Paper', 'Machine Learning', 'Neural Networks', 'CNN', 'RNN', 'Transformers', 'GNN'],
    'Value': [1942, 801, 466, 223, 84, 43, 12]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(df['Name'], df['Value'], color='white', hatch='//', edgecolor='black', linewidth=2) 

plt.title('Distribution of Research Papers in Local Conferences Since 2020')
plt.xlabel('Type of Paper')
plt.ylabel('Number of Papers')
plt.xticks(rotation=0)

plt.savefig('bar_plot_new_shaded.png')
plt.show()
a =1
