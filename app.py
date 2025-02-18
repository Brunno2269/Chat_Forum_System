import webbrowser
from flask import Flask
from threading import Thread
from blueprints.forum import forum_bp
import logging
import signal
import sys

app = Flask(__name__)

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Registrar Blueprints
app.register_blueprint(forum_bp)

@app.errorhandler(404)
def page_not_found(e):
    logger.warning("Página não encontrada: %s", e)
    return {"error": "Página não encontrada"}, 404

def open_browser():
    """Função para abrir o navegador automaticamente."""
    webbrowser.open_new("http://127.0.0.1:5000")

def run_server():
    """Função para executar o servidor Flask."""
    app.run(debug=False)  # Desativamos o debug para evitar conflitos

def signal_handler(sig, frame):
    """Função para capturar o sinal de fechamento da guia e encerrar o servidor."""
    logger.info("Servidor encerrado.")
    sys.exit(0)

if __name__ == '__main__':
    logger.info("Iniciando o servidor Flask...")
    
    # Capturar sinais de interrupção (Ctrl+C ou fechamento da guia)
    signal.signal(signal.SIGINT, signal_handler)
    
    # Abrir o navegador em uma thread separada
    thread = Thread(target=open_browser)
    thread.daemon = True
    thread.start()

    # Executar o servidor Flask
    run_server()