
# 📘 Sistema de Registro de Frequência Escolar

Este projeto é um sistema simples desenvolvido em **Django** para cadastrar alunos e registrar a presença deles.  
Foi feito como atividade prática para fins educativos.

---

## 🚀 Tecnologias Usadas
- Python
- Django
- HTML
- CSS
- SQLite (banco de dados padrão do Django)

---

## 🔧 Como Rodar o Projeto

### 1. Criar ambiente virtual
python -m venv venv

### 2. Ativar o ambiente virtual

**Windows:**
venv\Scripts\activate

**Linux/Mac:**
source venv/bin/activate

### 3. Instalar dependências
pip install -r requirements.txt

### 4. Rodar migrações
python manage.py migrate

### 5. Iniciar o servidor
python manage.py runserver

Acessar no navegador:  
**http://127.0.0.1:8000/**

---

## 📌 Funcionalidades

- Cadastro de alunos  
- Registro de frequência  
- Listagem de alunos  
- Listagem de frequência  
- Edição e exclusão  
- Interface simples e funcional  

---

## 📚 Modelos do Sistema

### **Aluno**
- Nome  
- Idade  
- Turma  

### **Frequência**
- Aluno  
- Data  
- Presente (Sim/Não)

---

## 📁 Estrutura Geral
- Projeto dividido em **apps** (ex: alunos, frequencias)  
- Templates organizados  
- URLs separadas  
- Formularios usando `forms.py`  

---

## 📜 Licença
Projeto desenvolvido apenas para fins educacionais.
