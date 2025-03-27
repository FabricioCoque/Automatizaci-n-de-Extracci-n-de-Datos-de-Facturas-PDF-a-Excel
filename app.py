import streamlit as st
import os
import pandas as pd
import openpyxl
from src.extractor import cargar_pdf
from src.datos_clave import estructurar_texto

# Título de la aplicación
st.title("📂 Factura Extractor - Generador de Reportes")

# Entrada de texto para la ruta de la carpeta
ruta_carpeta = st.text_input("📁 Ingresa la ruta de la carpeta que contiene los PDFs:", "")

# Botón para procesar los archivos PDF
if st.button("📊 Generar Reporte en Excel"):
    if ruta_carpeta and os.path.isdir(ruta_carpeta):
        lista_facturas = []
        
        # Recorrer los archivos PDF dentro de la carpeta
        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith(".pdf"):
                ruta_pdf = os.path.join(ruta_carpeta, archivo)
                
                # Extraer texto del PDF
                texto_extraido = cargar_pdf(ruta_pdf)
                
                # Extraer datos estructurados
                datos_factura = estructurar_texto(texto_extraido)
                
                # Agregar datos a la lista
                lista_facturas.append(datos_factura)
        
        # Convertir datos en DataFrame
        if lista_facturas:
            df = pd.DataFrame(lista_facturas)
            ruta_excel = os.path.join(ruta_carpeta, "facturas.xlsx")
            
            # Guardar en Excel
            df.to_excel(ruta_excel, index=False, engine="openpyxl")
            
            st.success(f"✅ Archivo Excel generado exitosamente en:\n📄 {ruta_excel}")
        else:
            st.warning("⚠ No se encontraron archivos PDF válidos en la carpeta.")
    else:
        st.error("❌ Ingresa una ruta válida de carpeta.")

