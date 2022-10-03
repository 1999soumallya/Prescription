from fpdf import FPDF

# FPDF.set_character_set('utf8')


def TexToPdf(filename):
    try:
        count = 0
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        f = open(filename, "r")
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='C')
        OtherPdfFile = pdf.output(f"Result.pdf")
        count += 1
        return OtherPdfFile
    except Exception as e:
        print(e)


TexToPdf('D:\\project\\Prescription\\NewFiles\\Soumallya Dey_Male_21_Pathology.txt')
