import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat = df_cat.groupby(['cardio', 'variable'])['value'].value_counts().unstack().fillna(0).reset_index()
    
    fig = sns.catplot(data=df_cat, kind="bar", x="variable", y="value", hue="cardio", ci=None)
    
    fig = fig.fig
    
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                  (df['height'] >= df['height'].quantile(0.025)) & 
                  (df['height'] <= df['height'].quantile(0.975)) & 
                  (df['weight'] >= df['weight'].quantile(0.025)) & 
                  (df['weight'] <= df['weight'].quantile(0.975))]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(10, 8))

    fig, ax = plt.subplots()
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', ax=ax)

    fig.savefig('heatmap.png')
    return fig
