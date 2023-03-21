import pandas as pd

x = pd.read_csv(r"C:\Users\aluno.laboratorio\Desktop\microdados\MICRODADOS.csv", encoding='latin-1', sep=';', low_memory=False)

x.columns =[column.replace(" ", "_") for column in x.columns]

x.query('Municipio == "CARIACICA" \
        and ComorbidadeTabagismo =="Sim"', inplace = True)

print(x)