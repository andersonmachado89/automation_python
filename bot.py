import pyautogui
import pandas as pd
import time

#tempo para execução de um comando e outro
pyautogui.PAUSE = 0.5

# Visualizando a nomenclatura das teclas
# print(pyautogui.KEYBOARD_KEYS)

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=647, y=528)
pyautogui.write('anderson.machadop@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhasenha')
pyautogui.press('tab')
pyautogui.press('enter')

#importar a base de dados
tabela = pd.read_csv('produtos.csv')
# print(tabela.columns)

for linha in tabela.index:
    pyautogui.click(x=612, y=361)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca'] ))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo'] ))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria'] ))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario'] ))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo'] ))
    pyautogui.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)