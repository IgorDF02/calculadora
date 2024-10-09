from flask import Flask, request, render_template
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('valores.html')  # Coloque o HTML em um arquivo chamado 'valores.html'

@app.route('gerar_pdf', methods=['POST'])
def gerar_pdf():
    liquidez_g = request.form['liquidez_g']
    liquidez_c = request.form['liquidez_c']
    liquidez_s = request.form['liquidez_s']
    liquidez_i = request.form['liquidez_i']
    
    mb = request.form['mb']
    mo = request.form['mo']
    ml = request.form['ml']
    roe  = request.form['roe']
    roa  = request.form['roa']
    
    comp_end = request.form['ecomp_end']
    end_geral = request.form['end_geral']
    part_cap = request.form['part_cap']

    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"Liquidez Geral: {liquidez_g}", ln=True)
    pdf.cell(200, 10, txt=f"Liquidez Corrente: {liquidez_c}", ln=True)
    pdf.cell(200, 10, txt=f"Liquidez Seca: {liquidez_s}", ln=True)
    pdf.cell(200, 10, txt=f"Liquidez Imediata: {liquidez_i}", ln=True)

    pdf.cell(200, 10, txt=f"Margem Bruta: {mb}", ln=True)
    pdf.cell(200, 10, txt=f"Margem Operacional: {mo}", ln=True)
    pdf.cell(200, 10, txt=f"Margem Líquida: {ml}", ln=True)
    pdf.cell(200, 10, txt=f"Retorno sobre o PL (ROE): {roe}", ln=True)
    pdf.cell(200, 10, txt=f"Retorno sobre os ativos (RSI ou ROA): {roa}", ln=True)
    
    pdf.cell(200, 10, txt=f"Composição de Endividamento: {comp_end}", ln=True)
    pdf.cell(200, 10, txt=f"Endividamento Geral: {end_geral}", ln=True)
    pdf.cell(200, 10, txt=f"Participação do Capitais de terceiros: {part_cap}", ln=True)

    # Salvar o PDF
    pdf_file_path = "formulario.pdf"
    pdf.output(pdf_file_path)

    return f"PDF gerado com sucesso! <a href='{pdf_file_path}'>Baixar PDF</a>"

if __name__ == '__main__':
    app.run(debug=True)
