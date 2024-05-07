import pyautogui as pa
import time 
import pandas as pd

# comando para nao bugar sistema
pa.PAUSE = 0.5

# entrando no navegador 

pa.press("win")
pa.write("brave") # navegador da sua escolha ou que vc utiliza
pa.press("enter")


# adicionando link

pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(3) # tempo de carregar site

# login

pa.click (x=547, y=377)
pa.write("qualquer_email@email.com")
pa.press("tab")
pa.write("senhasegura123")
pa.click (x=802, y=531) #botao de logar


# importando base de dados.

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Cadastrar produtos automaticamente 

for linha in tabela.index:
    pa.click (x=554, y=259)
    codigo = tabela.loc[linha, "codigo"]
    pa.write(str(codigo))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")
    obs = tabela.loc [linha, "obs"]
    if not pd.isna(obs):
        pa.write(str(tabela.loc[linha, "obs"]))
    pa.press("tab")
    pa.press("enter")    
    pa.scroll(4000)