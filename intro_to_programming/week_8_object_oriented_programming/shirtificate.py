"""
In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2,
a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt's image should be centered horizontally.
The user's name should be on top of the shirt, in white text.
All other details we leave to you. You're even welcome to add borders, colors, and lines. Your shirtificate needn't match John Harvard's precisely.
And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2's tutorial to learn how to use it.
Then skim fpdf2's API (application programming interface) to see all of its functions and parameters therefor.

No need to submit any PDFs with your code.
But, if you would like, you're welcome (but not expected) to share a shirtificate with your name on it in any of CS50's communities!
"""
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
name = input("Name: ")
pdf.add_page()
pdf.set_font("helvetica", "B", 32)
pdf.cell(190, 30, "CS50 Shirtificate", 0, 1, 'C', 'NEXT')
pdf.image('shirtificate.png', 10, None, 190)
pdf.set_xy(10, 100)
pdf.set_text_color(255)
pdf.set_font("helvetica", "B", 26)
pdf.cell(190, 10, name, 0, 1, 'C', 'NEXT')
pdf.output("shirtificate.pdf")