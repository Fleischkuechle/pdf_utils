import os
from click import style
from fpdf import FPDF
import fpdf


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


pdf = FPDF()
pdf.add_page()
for i in range(15):
    pdf.set_fill_color(255 - 15 * i)
    pdf.rect(
        x=5 + 5 * i,
        y=5 + 5 * i,
        w=200 - 10 * i,
        h=200 - 10 * i,
        # style="FD",
        style=fpdf.enums.RenderStyle.DF,
        round_corners=True,
        corner_radius=5,
    )
pdf_file_name: str = "draw_nested_squares.pdf"
save_to_output_folder(
    pdf=pdf,
    pdf_file_name=pdf_file_name,
)
# current_directory = os.getcwd()
# pdf_file_name: str = "draw_nested_squares.pdf"
# output_folder_name: str = "outputs"
# file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)
# # pdf.output(file_path)
# try:
#     pdf.output(name=file_path)
#     print(" ")
#     print(f"completed saved here: {file_path}")
# except Exception as e:

#     print(" ")
#     print(f"exception: {e}")
# # Example usage:
# if __name__ == "__main__":
#     test_print()
