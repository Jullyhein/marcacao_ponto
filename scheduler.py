#!/usr/bin/env python
# coding: utf-8
import os
import schedule
import time
import subprocess
import smtplib
import datetime
import logging
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_EMAIL = os.getenv("SENHA_EMAIL")
SMTP_SERVIDOR = os.getenv("SMTP_SERVIDOR")
SMTP_PORTA = int(os.getenv("SMTP_PORTA", 587))  # padrão: 587
EMAIL_DESTINATARIO = [
    email.strip() for email in os.getenv("EMAIL_DESTINATARIO", "").split(",") if email.strip()
]

logging.basicConfig(
    filename="script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

print("Horario atual do sistema:", datetime.datetime.now())

def enviar_email(assunto, mensagem):
    """Funcao para enviar um e-mail."""
    try:
        msg = MIMEText(mensagem, "plain", "utf-8")
        msg["Subject"] = assunto
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = ", ".join(EMAIL_DESTINATARIO)

        with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as servidor:
            servidor.starttls()  # Ativa segurança TLS
            servidor.login(EMAIL_REMETENTE, SENHA_EMAIL)
            servidor.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIO, msg.as_string())

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


def executar_script():
    print("Executando principal.py")
    try:
        subprocess.run(["python", "principal.py"], check=True)
        print("Execucaoo concluida com sucesso!")
        logging.info("Execucao concluida com sucesso!")
        enviar_email("Job Concluido ", "Ponto executado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar principal.py: {e}")
        enviar_email("Erro no Job ", f"Erro ao executar principal.py: {e}")
    finally:
        print("Encerrando o agendador.")
        exit()

# Agendando a tarefa para rodar todo dia �s 09:00
schedule.every().day.at("09:35").do(executar_script)

print("Agendador iniciado! Aguardando horario...")
while True:
    schedule.run_pending()
    logging.info("Verificacao de tarefas pendentes...") 
    time.sleep(60)  
