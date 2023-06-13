# Enviador de Mensagens Automático

Este é um script em Python para automatizar o envio de mensagens usando o Google Messages Web. Ele lê os contatos e as mensagens de um arquivo Excel e envia as mensagens para os contatos especificados.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python: selenium, pandas, pyperclip, pyautogui
- ChromeDriver

Certifique-se de ter o Python instalado no seu sistema e as bibliotecas necessárias instaladas. Você também precisará do ChromeDriver para o Selenium. Verifique se o ChromeDriver é compatível com a versão do seu navegador Google Chrome.

## Configuração

1. Faça o download ou clone este repositório.
2. Instale as bibliotecas Python necessárias executando o comando: `pip install -r requirements.txt`.
3. Baixe o ChromeDriver compatível com a versão do seu navegador Google Chrome e coloque o arquivo executável na mesma pasta do script.

## Uso

1. Coloque os contatos no arquivo Excel 'contatos.xlsx'. Certifique-se de que os contatos estejam na coluna 'A' do arquivo e tenha apenas números.
2. Escreva a mensagem que deseja enviar na coluna 'B' do arquivo Excel. Essa mensagem será a mesma para todos os contatos.
3. Execute o script `sms.py`.
4. Aguarde enquanto o script automatiza o envio das mensagens.

## Observações

- É necessária a autenticação via leitura de QR Code pelo celular no site https://messages.google.com/web/

