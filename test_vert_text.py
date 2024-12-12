import os
from fpdf import FPDF


def save_to_output_folder(
    pdf: FPDF,
    pdf_file_name: str,
):
    current_directory = os.getcwd()
    pdf_file_name: str = pdf_file_name  # "draw_an_hourglass_shape.pdf"
    output_folder_name: str = "outputs"
    file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)
    try:
        pdf.output(
            name=file_path,
        )
        print(" ")
        print(f"completed saved here: {file_path}")
    except Exception as e:

        print(" ")
        print(f"exception: {e}")


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
pdf_file_name: str = "test_vert_text.pdf"
# pdf.output("test_vert_text.pdf")
save_to_output_folder(pdf=pdf, pdf_file_name=pdf_file_name)
