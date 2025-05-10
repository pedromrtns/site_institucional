# Site Institucional

## Estrutura do Projeto
```
site_institucional/
│
├── apps/                    # Todas as aplicações do projeto
│   └── core/               # Aplicação principal
│       ├── migrations/     
│       ├── static/        
│       │   ├── css/       
│       │   ├── js/        
│       │   └── images/    
│       ├── templates/     
│       ├── tests/         
│       ├── admin.py      
│       ├── apps.py       
│       ├── models.py     
│       ├── urls.py       
│       └── views.py      
│
├── setup/                  # Configurações do projeto
│   ├── settings/          
│   │   ├── __init__.py   
│   │   ├── base.py       # Configurações base
│   │   ├── local.py      # Configurações de desenvolvimento
│   │   └── production.py # Configurações de produção
│   ├── urls.py           
│   └── wsgi.py           
│
├── static/                # Arquivos estáticos do projeto
│   ├── css/              
│   ├── js/               
│   └── images/           
│
├── templates/             # Templates globais
│   ├── base.html         
│   └── includes/         
│
├── .env                   # Variáveis de ambiente
├── .gitignore            
├── manage.py             
├── requirements/          # Requisitos separados por ambiente
│   ├── base.txt          
│   ├── local.txt         
│   └── production.txt    
└── requirements.txt       # Aponta para requirements/production.txt
```

## Configuração do Ambiente

1. Clone o repositório
```bash
git clone [url-do-repositorio]
cd site_institucional
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements/local.txt  # Para desenvolvimento
pip install -r requirements.txt        # Para produção
```

4. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

5. Execute as migrações
```bash
python manage.py migrate
```

6. Crie um superusuário
```bash
python manage.py createsuperuser
```

7. Execute o servidor de desenvolvimento
```bash
python manage.py runserver
```

## Desenvolvimento

- Use `python manage.py test` para executar os testes
- Siga o PEP 8 para estilo de código Python
- Mantenha a documentação atualizada
- Use branches para novas features

## Produção

Para deploy em produção:
1. Atualize `ALLOWED_HOSTS` no arquivo `.env`
2. Configure `DEBUG=False`
3. Use um servidor WSGI apropriado (ex: Gunicorn)
4. Configure um servidor web (ex: Nginx) como proxy reverso
