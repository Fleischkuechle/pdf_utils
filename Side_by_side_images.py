import os
from fpdf import FPDF
import fpdf

# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
# https://py-pdf.github.io/fpdf2/
imgA_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
imgB_path: str = r"D:\11\02\13\FPDF_tests\test_images\teset.png"
maring: float = 10
orientations: list[str] = [
    "landscape",
    "portrait",
]


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


pdf = FPDF(orientation=orientations[1])
pdf.set_margin(margin=maring)
pdf.add_page()
pdf.image(
    name=imgA_path,
    h=pdf.eph,
    w=pdf.epw / 2,
)  # full page height, half page width
pdf.set_y(0)
pdf.image(
    name=imgB_path,
    h=pdf.eph,
    w=pdf.epw / 2,
    x=pdf.epw / 2,
)  # full page height, half page width, right half of the page
# pdf.output("side-by-side.pdf")
current_directory = os.getcwd()
# pdf_file_name: str = "Side_by_side_images.pdf"
pdf_file_name: str = "Side_by_side_images.pdf"
save_to_output_folder(
    pdf=pdf,
    pdf_file_name=pdf_file_name,
)
# output_folder_name: str = "outputs"
# file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)
# # pdf.output(file_path)
# try:
#     pdf.output(
#         name=file_path,
#     )
#     print(" ")
#     print(f"completed saved here: {file_path}")
# except Exception as e:

#     print(" ")
#     print(f"exception: {e}")
