![Captura de tela de 2025-02-18 15-47-35](https://github.com/user-attachments/assets/ebae1057-0fc2-4fe8-9baa-036a1b139257)

# Fórum de Discussão
Este é um sistema simples de fórum de discussão desenvolvido com Python (Flask) para o backend e HTML/CSS/JavaScript para o frontend. Ele permite que os usuários criem tópicos e adicionem comentários.

## Funcionalidades
- Criação de tópicos com título e conteúdo.
- Adição de comentários em tópicos existentes.
- Interface responsiva e moderna.
- Abertura automática no navegador ao iniciar o servidor.
- Encerramento automático do servidor ao fechar a guia do navegador.

## Estrutura do Projeto
forum/
│
├── app.py                # Backend principal
├── blueprints/           # Módulos separados para rotas
│   └── forum.py          # Rotas específicas do fórum
├── utils/                # Funções utilitárias
│   └── data_manager.py   # Gerenciador de dados simulados
├── templates/
│   └── index.html        # Frontend (HTML)
├── static/
│   ├── css/
│   │   └── styles.css    # Estilos CSS
│   └── js/
│       └── script.js     # Lógica JavaScript
└── requirements.txt       # Dependências do projeto

## Requisitos
- Python 3.6 ou superior
- Flask (`pip install Flask`)
- Um navegador moderno

## Como Executar
1. Clone o repositório:
   git clone https://github.com/Brunno2269/Chat_Forum_System.git
