from flask import Flask, request, render_template, send_from_directory
from fpdf import FPDF
import os

app = Flask(__name__)

# Definindo um diretório para armazenar os PDFs gerados
UPLOAD_FOLDER = 'static/pdfs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('valores.html')  # Certifique-se de ter o arquivo 'valores.html' na pasta 'templates'

@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    # Verificar se as chaves existem no formulário
    form_data = {
        'liquidez_g': 'Liquidez Geral',
        'liquidez_c': 'Liquidez Corrente',
        'liquidez_s': 'Liquidez Seca',
        'liquidez_i': 'Liquidez Imediata',
        'mb': 'Margem Bruta',
        'mo': 'Margem Operacional',
        'ml': 'Margem Líquida',
        'roe': 'Retorno sobre o PL (ROE)',
        'roa': 'Retorno sobre os ativos (RSI ou ROA)',
        'ecomp_end': 'Composição de Endividamento',
        'end_geral': 'Endividamento Geral',
        'part_cap': 'Participação do Capitais de terceiros'
    }
    
    # Extrair os valores do formulário
    form_values = {}
    for key, label in form_data.items():
        form_values[key] = request.form.get(key, 'Não informado')
    
    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Adicionar dados ao PDF
    for key, label in form_data.items():
        pdf.cell(200, 10, txt=f"{label}: {form_values[key]}", ln=True)
    
    # Gerar o nome do arquivo PDF
    pdf_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'formulario.pdf')
    pdf.output(pdf_file_path)

    # Retornar o link para o arquivo gerado
    return f"PDF gerado com sucesso! <a href='/static/pdfs/formulario.pdf'>Baixar PDF</a>"

# Rota para servir arquivos estáticos (PDFs gerados)
@app.route('/static/pdfs/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
