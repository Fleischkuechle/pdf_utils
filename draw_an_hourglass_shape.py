import os
from fpdf import FPDF
import fpdf


def save_to_output_folder(pdf: FPDF, pdf_file_name: str):
    # current_directory = os.getcwd()
    current_directory: str = os.path.dirname(__file__)
    pdf_file_name: str = pdf_file_name  # "draw_an_hourglass_shape.pdf"
    output_folder_name: str = "outputs"
    file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)
    # pdf.output(file_path)
    try:
        pdf.output(
            name=file_path,
            dest="F",
        )
        print(" ")
        print(f"completed saved here: {file_path}")
    except Exception as e:

        print(" ")
        print(f"exception: {e}")


pdf = fpdf.FPDF(
    unit="mm",
    # format=(10, 10),
)
pdf.add_page()

with pdf.new_path() as path:
    path.move_to(2, 2)
    path.line_to(8, 8)
    path.horizontal_line_relative(-6)
    path.line_relative(6, -6)
    path.close()

pdf_file_name: str = "draw_an_hourglass_shape.pdf"
save_to_output_folder(pdf=pdf, pdf_file_name=pdf_file_name)
# # pdf.output("draw_an_hourglass_shape.pdf")
# current_directory = os.getcwd()
# pdf_file_name: str = "draw_an_hourglass_shape.pdf"
# output_folder_name: str = "outputs"
# file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)
# # pdf.output(file_path)
# try:
#     pdf.output(
#         name=file_path,
#         dest="F",
#     )
#     print(" ")
#     print(f"completed saved here: {file_path}")
# except Exception as e:

#     print(" ")
#     print(f"exception: {e}")
