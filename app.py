from flask import Flask, request, render_template
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Coloque o HTML em um arquivo chamado 'form.html'

@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    nome = request.form['nome']
    email = request.form['email']

    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"Nome: {nome}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)

    # Salvar o PDF
    pdf_file_path = "formulario.pdf"
    pdf.output(pdf_file_path)

    return f"PDF gerado com sucesso! <a href='/{pdf_file_path}'>Baixar PDF</a>"

if __name__ == '__main__':
    app.run(debug=True)
