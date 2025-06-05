# 📌 Automacão de Exportação de Marcações - Solar Group

Este projeto realiza a automação completa de extração de registros de marcações do site da DIMEP, renomeia os arquivos baixados e envia via SFTP para o servidor TOTVS da Solar Group.

---

## ⚙️ Funcionalidades

✅ Acesso automático ao portal da DIMEP      
✅ Preenchimento de filtros e data de pesquisa      
✅ Download automático de arquivos de marcação      
✅ Renomeação dos arquivos baixados        
✅ Envio via SFTP para o servidor remoto TOTVS     
✅ Uso de variáveis seguras com `.env`            
✅ Compatível com execução manual ou via agendamento (ex: Task Scheduler)

---

## 📁 Estrutura

```
TI - ponto/
│
├── principal.py            # Script principal de automação
├── scheduler.py            # (Opcional) Script para agendamento
├── requirements.txt        # Dependências do projeto
├── .env                    # Variáveis sensíveis (NÃO subir para o Git!)
└── README.md               # Este documento
```

---

## 🔐 Variáveis de Ambiente (.env)

Crie um arquivo `.env` com o seguinte conteúdo:

```env
# Credenciais de login
email=seu.email@dominio.com.br
senha=sua_senha_dimep

# SFTP
SFTP_USUARIO=ftp_...
SFTP_SENHA=...
SFTP_HOST=...
SFTP_PORTA=..
REMOTE_FOLDER=...

# Caminhos
LOCAL_FOLDER=C:...
ARQUIVOS=REL012.txt,REL013.txt,REL014.txt,REL015.txt

# E-mail de aviso (se usar função de e-mail)
EMAIL_REMETENTE=...
SENHA_EMAIL=senha_do_email
SMTP_SERVIDOR=smtp.office365.com
SMTP_PORTA=...
EMAIL_DESTINATARIO=...
```

---

## 💻 Instalação

1. Clone este repositório ou copie os arquivos
2. Crie o ambiente virtual:

```bash
python -m venv .venv
```

3. Ative o ambiente:

* **PowerShell**

  ```bash
  .\.venv\Scripts\Activate.ps1
  ```
* **CMD**

  ```cmd
  .venv\Scripts\activate.bat
  ```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Execução

Execute o script agendador com:

```bash
python scheduler.py
```
OU

Execute o script principal com:

```bash
python principal.py
```

> O navegador será iniciado, os arquivos exportados e enviados ao servidor remoto automaticamente.

---

## 🧪 Testes

Testes unitários são recomendados para funções críticas. Execute com:

```bash
pytest
```

---

## ❗ Observações

* O script depende do layout atual do portal da DIMEP. Mudanças visuais podem exigir ajustes nos seletores.
* Evite compartilhar o arquivo `.env` publicamente.
* Para execução automatizada, use **Agendador de Tarefas** (`Schedule`).

---

## ⚒️ Requisitos

* Python 3.9 ou superior
* Google Chrome instalado
* Acesso ao portal DIMEP com permissão de download
* Acesso SFTP configurado no TOTVS

---

## 📬 Suporte

Em caso de dúvidas, entre em contato com:
[jullyensoares@hotmail.com](mailto:jullyensoares@hotmail.com)

---

