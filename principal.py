#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import glob
import time
import datetime
import pyautogui
import subprocess
import paramiko
import tempfile
import pygetwindow as gw
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


user_data_dir = tempfile.mkdtemp()

load_dotenv()
senha_site = os.getenv("senha")
email_site=os.getenv("email")

options = Options()
options.add_argument(f'--user-data-dir={user_data_dir}')
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\SOLAR\\", 
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_setting_values.automatic_downloads": 1
})

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


download_path = r"C:\SOLAR"
files = glob.glob(os.path.join(download_path, '*'))

if not files:
    print(f"O diretório '{download_path}' está vazio. Nenhum arquivo será deletado.")
else:
    
    for f in files:
        try:
            os.remove(f)
            print(f"{f} foi deletado.")
        except Exception as e:
            print(f"Erro ao deletar {f}: {e}")



driver.get("https://www.dimepkairos.com.br/Dimep/Account/LogOn?ReturnUrl=%2FDimep%2FPonto")
WebDriverWait(driver, 15).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "ui-widget-overlay"))
)
driver.maximize_window()


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "LogOnModel_UserName"))).send_keys(email_site)
driver.find_element(By.ID, "LogOnModel_Password").send_keys(senha_site)
driver.find_element(By.ID, "btnFormLogin").click()


try:
    botao_modal = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "soCloseModal"))
    )
    botao_modal.click()
    print("Modal fechado com sucesso.")
except (TimeoutException, NoSuchElementException) as e:
    print("Modal não foi exibido ou já estava fechado.")

time.sleep(2)


try:
    span_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[2]/div[2]/span[2]"))
    )
    span_element.click()
except Exception:
    print("Elemento span[2] não encontrado, seguindo o fluxo normalmente.")


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Tab2"))
    )
    tab_marcacoes = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "Tab2"))
    )
    tab_marcacoes.click()
    print("Aba 'Marcações' acessada com sucesso.")
except Exception as e:
    print(f"Erro ao acessar a aba 'Marcações': {e}")


time.sleep(2)
driver.find_element(By.XPATH,
                    '/html/body/header/div[2]/div[2]/span[2]').click()

time.sleep(2)
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div').click()
time.sleep(2)

data_atual = datetime.datetime.now() 
umdia = data_atual - datetime.timedelta(days=10)

data_formatada_atual = data_atual.strftime("%d/%m/%Y")
data_formatada_umdia = umdia.strftime("%d/%m/%Y")
time.sleep(2)
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[1]/div/input').click()
time.sleep(2)
data= driver.find_element(By.XPATH,
                          '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[1]/div/input')

data.send_keys(data_formatada_umdia)
time.sleep(2)

driver.find_element(By.XPATH,
                    '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/div/input').click()
time.sleep(2)
data01= driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/div/input')
time.sleep(2)
data01.send_keys(data_formatada_atual)
time.sleep(2)

pesquisar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "SearchButton"))
)


pesquisar_button.click()
time.sleep(5)

driver.find_element(By.XPATH,
                     '/html/body/div[1]/div[5]/div[1]/div/div[2]/div[2]/div/label').click()
time.sleep(2)

driver.find_element(By.ID, "MaisExportar").click()
time.sleep(2)  

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "ExportarAFD"))
)


exportar_afd = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ExportarAFD"))
)
exportar_afd.click()
time.sleep(5)  

span_exportar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@id="ExportarAFD"]/span'))
)
span_exportar.click()
time.sleep(35)


download_path = r"C:\SOLAR"

arquivos_renomear = {
    "marcacoes_0001.txt": "REL015.txt",
    "marcacoes_0002.txt": "REL012.txt",
    "marcacoes_0003.txt": "REL014.txt",
    "marcacoes_0004.txt": "REL013.txt"
}

for antigo, novo in arquivos_renomear.items():
    origem = os.path.join(download_path, antigo)
    destino = os.path.join(download_path, novo)
    try:
        if os.path.exists(origem):
            os.rename(origem, destino)
            print(f"{antigo} renomeado para {novo}")
        else:
            print(f"{antigo} não encontrado.")
    except Exception as e:
        print(f"Erro ao renomear {antigo}: {e}")


time.sleep(3)


subprocess.Popen(['explorer', download_path])
time.sleep(3)

try:
    filezilla_window = gw.getWindowsWithTitle('SOLAR')[0]
    filezilla_window.restore() 
    filezilla_window.maximize()
    filezilla_window.activate()
except Exception as e:
    print(f"Não foi possível manipular a janela do Explorer: {e}")


time.sleep(10)

usuario = os.getenv("SFTP_USUARIO")
senha = os.getenv("SFTP_SENHA")
host = os.getenv("SFTP_HOST").strip()
porta = int(os.getenv("SFTP_PORTA", 22))

# Caminhos e arquivos
local_folder = os.getenv("LOCAL_FOLDER")
remote_folder = os.getenv("REMOTE_FOLDER")
arquivos = [arq.strip() for arq in os.getenv("ARQUIVOS", "").split(",") if arq.strip()]

# Conecta via SFTP
transport = paramiko.Transport((host, porta))
transport.connect(username=usuario, password=senha)

sftp = paramiko.SFTPClient.from_transport(transport)

# Acessa pasta remota
try:
    sftp.chdir(remote_folder)
except IOError:
    print(f"Pasta remota '{remote_folder}' não encontrada.")
    sftp.close()
    transport.close()
    exit()

# Envia os arquivos
for nome in arquivos:
    local_path = os.path.join(local_folder, nome)
    remote_path = f"{remote_folder}/{nome}"
    try:
        sftp.put(local_path, remote_path)
        print(f"{nome} enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar {nome}: {e}")

sftp.close()
transport.close()
driver.quit()