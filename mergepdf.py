# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:32:25 2020

@author: noelp
"""

from reportlab.pdfgen import canvas
import pdfrw
import pandas as pd

def get_person(df,apellido,nombre):   
    apellido = df.loc[df['Apellido'] == apellido]        
    persona = apellido.loc[df['Nombre'] == nombre]
    return persona

def get_prest(df_persona,prestacion):
    prest = df_persona.loc[df_persona['Prestación'] == prestacion]
    return prest

def create_overlay(df,prestacion,mes_v,fecha):
    ##fecha 02/07/2020
    dia,mes,año= fecha.split('/')
    ## df = get_person(df,apellido,nombre)
    prest = get_prest(df,prestacion)
    
    c = canvas.Canvas('persona.pdf')

    c.drawString(450, 725, mes_v)    
    c.drawString(170, 660, prest['Nombre']+' '+prest['Apellido'])
    c.drawString(240, 620, prest['DNI'])
    c.drawString(240, 590, prest['Afiliado'])
    c.drawString(240, 560, prest['Autorizacion'])
    c.drawString(500, 560, prest['Emisión'])
    if prestacion == 'AT':
        c.drawString(137, 400, 'x')
    else:
        c.drawString(137, 360, 'x')
    
    c.line(30, 320, 550, 310)
    c.line(30, 310, 550, 320)    
    c.drawString(435, 255, 'x')
    c.drawString(400, 239, prest['Día de atención'])
    c.drawString(400, 225, prest['Hora de atención'])
    
    
    c.showPage()    
    c.line(40, 590, 550, 770)
    c.line(40, 770, 550, 590)
    c.line(40, 350, 290, 530)
    c.line(40, 530, 290, 350)
    c.drawString(344, 492, '{}     {}      {}'.format(dia,mes,año))
    c.drawImage('C:/Users/noelp/Documents/laburo/firmas/{}.gif'.format(prest['Prestador']),
                440,345,width=70,height=70,preserveAspectRatio=True)
    
    c.drawString(325, 345, prest['Prestador'])
    c.drawString(367, 370, prest['CUIT'].split['-'][1])
    c.save()

def merge_pdfs(form_pdf, overlay_pdf, output):
    """
    Merge the specified fillable form PDF with the 
    overlay PDF and save the output
    """
    form = pdfrw.PdfReader(form_pdf)
    olay = pdfrw.PdfReader(overlay_pdf)
    
    for form_page, overlay_page in zip(form.pages, olay.pages):
        merge_obj = pdfrw.PageMerge()
        overlay = merge_obj.add(overlay_page)[0]
        pdfrw.PageMerge(form_page).add(overlay).render()
        
    writer = pdfrw.PdfWriter()
    writer.write(output, form)


directory = 'C:/Users/noelp/Documents/laburo python/'
inp = directory+'anexo_5967071_3.pdf'
out = directory+'a3.pdf'

pacientes = pd.read_excel('digit2020.xlsx',sheetname=0,header=0,index_col=False,
                          keep_default_na=True)

for num in pacientes['DNI']:
    persona = pacientes.loc[pacientes['DNI'] == num]
    prest = persona['Prestación']
    for p in prest:
        pdata = persona.loc[prest == p]
        create_overlay(pdata,mes_v,fecha)
        
        
        

create_overlay()
merge_pdfs(inp, 'persona.pdf', '{} {} A3.pdf'.format(apellido,prestador))

