
# Como Rodar o Projeto StockWise em Qualquer Máquina

Este é um guia completo para rodar o projeto Django **StockWise** localmente. Ideal para apresentações na faculdade ou uso pessoal.

---

## 📁 Estrutura Esperada da Pasta

Você deve ter uma pasta com o nome `StockWise` contendo os arquivos abaixo:

```
StockWise/
├── core/
├── static/
├── stockwise/
├── manage.py
├── requirements.txt
├── README.txt  ← (este arquivo)
└── db.sqlite3  ← (opcional: caso use SQLite)
```

> ✅ **Importante**: certifique-se de que o Python esteja instalado na máquina.

---

## 🧭 PASSO A PASSO

### 1. Abra o terminal ou prompt de comando

Acesse a pasta onde está o projeto. Exemplo:

```bash
cd Desktop
cd StockWise
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No **Windows**:

```bash
venv\Scripts\activate
```

- No **Linux/Mac**:

```bash
source venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. (Se necessário) Configure o banco SQLite

Edite o `stockwise/settings.py` e altere a parte do banco para:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Se quiser apagar o banco antigo e começar do zero:

```bash
del db.sqlite3  # ou rm db.sqlite3 no Linux/Mac
python manage.py migrate
```

---

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

Preencha as informações (nome de usuário, email, senha).

---

### 6. Rode o servidor local

```bash
python manage.py runserver
```

Abra no navegador:
👉 http://127.0.0.1:8000

---

### 7. Faça login e use o sistema!

Parabéns 🎉
