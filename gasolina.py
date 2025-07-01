import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

gasolina_pd = pd.read_csv("/content/da-expratmod19-ebac/gasolina.csv")
print(gasolina_pd)

maior_vl = gasolina_pd.loc[gasolina_pd['venda'].idxmax()]
menor_vl = gasolina_pd.loc[gasolina_pd['venda'].idxmin()]

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_pd, x="dia", y="venda",
                         color="orange", linewidth=2.5, marker='o')
  plt.scatter(maior_vl["dia"], maior_vl["venda"], color="green", s=50, zorder=5, label="Valor máximo")
  plt.scatter(menor_vl["dia"], menor_vl["venda"], color="red", s=50, zorder=5, label="Valor mínimo")
  plt.plot(gasolina_pd["dia"], gasolina_pd["venda"], color="orange", linewidth=2.5, marker='o')
  grafico.set(title='Preço da gasolina por dia', xlabel='Dias', ylabel='R$ de venda');
  plt.legend()
  plt.savefig("gasolina.png", dpi=300)