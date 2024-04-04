import pandas as pd

alunos = {'Nome':['joão', "Maria", "José"], "Nota":[10,0.5,10], "Aprovado":["Sim", "Não", "Sim"]}

dataframe = pd.DataFrame(alunos)

print(dataframe.head(2))