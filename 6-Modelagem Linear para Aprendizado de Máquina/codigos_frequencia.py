
import pandas as pd

# Leitura da base de dados
df = pd.read_excel("base_dados_solar_automacao.xlsx")

# Frequência da variável quantitativa discreta
freq_discreta = df['Qtd_Dispositivos_Conectados'].value_counts().sort_index()
freq_discreta_df = pd.DataFrame({
    'Qtd_Dispositivos_Conectados': freq_discreta.index,
    'Frequência Absoluta': freq_discreta.values,
    'Frequência Relativa (%)': (freq_discreta.values / len(df) * 100).round(2)
})

print("Tabela de Frequência - Qtd_Dispositivos_Conectados")
print(freq_discreta_df)

# Frequência da variável quantitativa contínua
classes_continua = pd.cut(df['Energia_Gerada_kWh'], bins=6)
freq_continua = classes_continua.value_counts().sort_index()
freq_continua_df = pd.DataFrame({
    'Faixa de Energia (kWh)': freq_continua.index.astype(str),
    'Frequência Absoluta': freq_continua.values,
    'Frequência Relativa (%)': (freq_continua.values / len(df) * 100).round(2)
})

print("\nTabela de Frequência - Energia_Gerada_kWh")
print(freq_continua_df)
