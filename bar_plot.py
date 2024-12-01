import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['All Paper', 'Machine Learning','Neural Networks', 'CNN', 'RNN', 'Transformers', 'GNN'],
    'Value': [1942,801, 466, 223,84, 43, 12]
}

df = pd.DataFrame(data)


df.plot(kind='bar', x='Name', y='Value', legend=False,figsize=(12, 6))
plt.xticks(rotation=0)
plt.title('Doistribution of research papers in local conferences since 2020')
plt.xlabel('Type of Paper')
plt.ylabel('Number of Papers')
plt.savefig('bar_plot_new.png')
plt.show()
