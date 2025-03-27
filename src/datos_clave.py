import re 


def estructurar_texto(texto_completo):
    # Inicializa un diccionario vacío donde vamos a almacenar los datos extraídos
    datos_factura = {}

    # **Nombre del Proveedor (Banco)**
    proveedor_match = re.search(r"FACTURA\s*\n(.*?)\n", texto_completo)
    if proveedor_match:
        datos_factura['Nombre del Proveedor'] = proveedor_match.group(1).strip()
    
    # **Número de Autorización**
    autorizacion_match = re.search(r"N° Autorización:\s*(\d+)", texto_completo)
    if autorizacion_match:
        datos_factura['Número de Autorización'] = autorizacion_match.group(1)
    
    # **Número de Factura**
    num_factura_match = re.search(r"FACTURA NUMERO:\s*\n([\d\s-]+)", texto_completo)
    if num_factura_match:
        datos_factura['Número de Factura'] = num_factura_match.group(1).strip()
    
    # **Fecha de Pago**
    fecha_pago_match = re.search(r"(\d{2}/\d{2}/\d{4})", texto_completo)
    if fecha_pago_match:
        datos_factura['Fecha de Pago'] = fecha_pago_match.group(1)
    
    # **Fecha de Emisión**
    fecha_emision_match = re.search(r"Fecha Emision\s*\n.*?(\d{2}/\d{2}/\d{4})", texto_completo)
    if fecha_emision_match:
        datos_factura['Fecha de Emisión'] = fecha_emision_match.group(1)

    # **Descripción** del servicio
    descripcion_match = re.search(r"DESCRIPCIÓN\s*CANT\.\s*PRECIO UNITARIO\s*TOTAL\n(.*?)\d{1,3}(?:,\d{3})*(?:\.\d{2})?", texto_completo, re.DOTALL)
    if descripcion_match:
        datos_factura['Descripción'] = descripcion_match.group(1).strip()
    
    # **Valor del Servicio**
    valor_match = re.search(r"Valor Servicio\s*([\d,\.]+)", texto_completo)
    if valor_match:
        datos_factura['Valor Servicio'] = valor_match.group(1)
    
    # **IVA 15%**
    iva_match = re.search(r"IVA 15%\s*([\d,\.]+)", texto_completo)
    if iva_match:
        datos_factura['IVA 15%'] = iva_match.group(1)
    
    # **Total**
    total_match = re.search(r"TOTAL\s*([\d,\.]+)", texto_completo)
    if total_match:
        datos_factura['Total'] = total_match.group(1)

    return datos_factura

