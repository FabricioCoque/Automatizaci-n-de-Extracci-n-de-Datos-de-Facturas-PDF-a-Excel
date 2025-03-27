import pdfplumber

def cargar_pdf(ruta_pdf):
   texto_completo= ""
   with pdfplumber.open(ruta_pdf) as pdf:
       for pagina in pdf.pages:
           texto_completo +=pagina.extract_text() + "\n" 
       return texto_completo
   
   

