import os
from fpdf import FPDF
import fpdf

# https://py-pdf.github.io/fpdf2/
#


def save_to_output_folder(
    pdf: FPDF,
    pdf_file_name: str,
):
    current_directory = os.getcwd()
    pdf_file_name: str = pdf_file_name  # "draw_an_hourglass_shape.pdf"
    output_folder_name: str = "outputs"
    file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)
    # pdf.output(file_path)
    try:
        pdf.output(
            name=file_path,
        )
        print(" ")
        print(f"completed saved here: {file_path}")
    except Exception as e:

        print(" ")
        print(f"exception: {e}")


##
pdf = FPDF()
pdf.add_page()
width: int = 290
height: int = 126
x_pos: int = 0
y_pos: int = 0
line_distance: int = 5
count: int = int(height / line_distance)
for i in range(count):
    pdf.rect(
        x=x_pos,
        y=y_pos,
        w=width,
        h=height,
        style=fpdf.enums.RenderStyle.D,
        # round_corners=True,
        # corner_radius=5,
    )
    height = height - line_distance
    y_pos = y_pos + line_distance
# pdf.output("draw_grid.pdf")
pdf_file_name: str = "draw_grid.pdf"
save_to_output_folder(
    pdf=pdf,
    pdf_file_name=pdf_file_name,
)
