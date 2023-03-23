import pandas as pd

x = pd.read_csv("MICRODADOS.csv", encoding='latin-1', sep=";", low_memory=False)

x.columns =[column.replace(" ", "_") for column in x.columns]

x.query('Municipio == "CARIACICA"\
        and ComorbidadeTabagismo =="Sim"\
        and Evolucao == "Óbito pelo COVID-19"\
        and DataObito > "2019"', inplace = True)

print(x)

