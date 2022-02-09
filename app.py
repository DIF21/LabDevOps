from flask import Flask
# incluindo import os para adequar docker
import os
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Gerson SC"

if __name__ == '__main__':
    # incluindo import os para adequar docker
    port = os.getenv('PORT')
    # incluido '0.0.0.0', port=port para adequar docker
    app.run('0.0.0.0', port=port)
