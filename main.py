from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv", sep=',')

pdf = FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False)

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align="L")
    pdf.line(10, 21, 200, 21)

    pdf.ln(265)
    pdf.set_font(family='Times', style='B', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align="R")

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family='Times', style='B', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align="R")

pdf.output("output.pdf")