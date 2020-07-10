# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:22:04 2020

@author: noelp
"""

from reportlab.pdfgen import canvas
import pdfrw
import os
#%%
def create_overlay(dia, mes, año):
        
    c = canvas.Canvas('modif.pdf')
    c.setFillColorRGB(1,1,1)
    c.rect(440,722,50,15,stroke=0,fill=1)
    c.setFillColorRGB(0,0,0)
    c.drawString(450, 725, mes)    
    c.showPage()
    c.drawString(344, 492, '{}     {}      {}'.format(dia,mes,año))
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

create_overlay('07','junio','2020')

direc = 'C:/Users/noelp/Documents/laburo/anexo 3/'
for filename in os.listdir(direc+'armadosV2'):
    pdftk filename output 'destfile.pdf' uncompress
    merge_pdfs(filename,'modif.pdf', direc+'armados'+filename)    