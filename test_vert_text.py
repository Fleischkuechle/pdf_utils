from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("times")

a, x, y = 90, 10, 295  # left margin banner using .text():
with pdf.rotation(angle=a, x=x, y=y):
    banner = pdf.text(
        x=x,
        y=y,
        text="This text should start at left bottom of the page and continue upwards through its left margin",
    )
print(banner)

a, x, y = 270, 208, 5  # right margin banner using .set_xy(x,y) and .cell()
pdf.set_auto_page_break(False)
pdf.set_xy(x, y)
pdf.set_line_width(0.25)
with pdf.rotation(angle=a, x=x, y=y):
    pdf.cell(
        text="This text should start at right top of the page and continue downwards through its right margin",
        border=1,
        h=10,  # box height 10 mm
        # w=0 # I guess in rotation context this does not work as expected:
        # how can I extend text box downwards, far beyond text end, near to page bottom?
    )

pdf.output("test_vert_text.pdf")
