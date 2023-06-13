import time
from selenium import webdriver
import pandas as pd
import pyperclip
import pyautogui

driver = webdriver.Chrome()

# Ler os contatos da coluna 'A' da planilha Excel
df = pd.read_excel('contatos.xlsx', dtype={'A': str})
contatos = df['A']

# Converter os valores para strings
contatos = contatos.astype(str)

# Ler a mensagem da coluna 'B'
mensagem = df['B'][0]  # Assumindo que a mensagem é a mesma para todos os contatos

# Navegue para o site de autenticação
driver.get('https://messages.google.com/web/authentication?hl=pt-BR')

time.sleep(5)

# Maximizar a janela do navegador
driver.maximize_window()

# Posicione o mouse sobre o elemento de input para a mensagem
pyautogui.moveTo(177, 261)

# Clique no elemento de input
pyautogui.click()
time.sleep(1)

time.sleep(10)

# Loop para copiar e enviar cada linha
for contato in contatos:
    
    # Verificar se o valor é 'nan'
    if contato !='nan':
    
        # Copiar o valor de contato para a área de transferência
        pyperclip.copy(contato)

        # Posicione o mouse sobre o elemento de input
        pyautogui.moveTo(672, 263)

        # Clique no elemento de input
        pyautogui.click()
        time.sleep(1)

        # Cole o texto da área de transferência
        pyautogui.hotkey('ctrl', 'v')

        # Pressione a tecla Enter para iniciar a conversa
        pyautogui.press('enter')

        time.sleep(1)

        # Posicione o mouse sobre o elemento de input para a mensagem
        pyautogui.moveTo(662, 962)

        # Clique no elemento de input
        pyautogui.click()
        time.sleep(1)

        # Copie a mensagem para a área de transferência
        pyperclip.copy(mensagem)

        # Cole o texto da área de transferência
        pyautogui.hotkey('ctrl', 'v')

        # Pressione a tecla Enter para enviar a mensagem
        pyautogui.press('enter')

        time.sleep(2)

        # Posicione o mouse sobre o elemento de input para a mensagem
        pyautogui.moveTo(177, 261)

        # Clique no elemento de input
        pyautogui.click()
        time.sleep(1)

# Encerrar o driver
driver.quit()
