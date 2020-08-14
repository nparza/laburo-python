# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:58:59 2020

@author: noelp
"""

from reportlab.pdfgen import canvas
import pdfrw

def create_overlay():
    '''
    Create basic canvas
    I use this function in order to personalize what information I add to mi form
    '''
    
    c = canvas.Canvas('data.pdf')

    c.drawString(450, 725, 'string')    ### add text    
    c.line(30, 320, 550, 310) ### add line
    c.showPage()    ## skip page
    c.setFillColorRGB(1,1,1) ## change background of added element
    c.drawImage('filename.gif', 440,365,width=70,height=70,
                preserveAspectRatio=True, mask='auto') ## add image, mask ='auto' for transparent backgrounds

    c.save()
     
def merge_pdfs(form_pdf, overlay_pdf, output):
    """
    Merge the specified fillable form PDF with the 
    overlay PDF and save the output
    In this example overlay_pdf is 'data.pdf'
    """
    form = pdfrw.PdfReader(form_pdf)
    olay = pdfrw.PdfReader(overlay_pdf)
    
    for form_page, overlay_page in zip(form.pages, olay.pages):
        merge_obj = pdfrw.PageMerge()
        overlay = merge_obj.add(overlay_page)[0]
        pdfrw.PageMerge(form_page).add(overlay).render()
        
    writer = pdfrw.PdfWriter()
    writer.write(output, form)
    
create_overlay()        
merge_pdfs('input_filename.pdf', 'data.pdf', 'output_filename.pdf')
  