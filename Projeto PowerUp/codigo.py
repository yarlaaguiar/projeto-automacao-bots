# Passo 1: Entrar no sistema da empresa.
# Passo 2: Fazer login.
# Passo 3: Abrir a base de dados.
# Passo 4: Cadastrar um produto.
# Passo 5: Repetir passo 4 até acabar a lista de produtos.

# pyautogui.click -> Clica em um local específico da tela.
# pyautogui.write -> Escreve um texto.    
# pyautogui.press -> Pressiona uma tecla específica do teclado.
# pyautogui.hotkey -> Pressiona uma combinação de teclas ou atalho de teclado.

import pyautogui
import csv
import time
pyautogui.PAUSE = 0.5 
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Passo 1: Entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)  # Espera 2 segundos para o navegador abrir
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)  # Espera 3 segundos para a página carregar

# Passo 2: Fazer login
pyautogui.click(x=481, y=407)  # Clica no campo de email
pyautogui.write('yarla.aguiar1@gmail.com')  # Digite seu email
pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
pyautogui.write('senhaqualquer')  # Digite sua senha
pyautogui.press('enter')  # Pressiona Enter para fazer login
time.sleep(3)  # Espera 3 segundos para a página carregar

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl 
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar um produto
    # código
    pyautogui.click(x=408, y=295)  # Clica no campo de cadastro do produto11.0  
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)  # Digite o código do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)  # Digite a marca do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)  # Digite o tipo do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)  # Digite a categoria do produtoConferir estoque

    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
    #preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)  # Digite o preço do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)  # Digite o custo do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o próximo campo
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)  # Digite a observação do produto

    pyautogui.press('enter')  # Pressiona Enter para cadastrar o produto

    #voltar para o início da tela para cadastrar o próximo produto
    pyautogui.scroll(5000)  # Rola a tela para cima para voltar ao início da página
    time.sleep(1)  # Espera 1 segundo para a tela rolar

# Passo 5: Repetir passo 4 até acabar a lista de produtos
