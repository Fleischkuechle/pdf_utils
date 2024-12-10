from fpdf import FPDF
from pathlib import Path

# from fpdf import FPDF
import fpdf

# https://py-pdf.github.io/fpdf2/

imgA_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
imgB_path: str = r"D:\11\02\13\FPDF_tests\test_images\teset.png"
maring: float = 10
orientations: list[str] = [
    "landscape",
    "portrait",
]


def test_image_fit_in_rect_with_c_align_center():
    pdf = fpdf.FPDF()

    pdf.add_page()
    pdf.image(
        name=imgA_path,
        # w=72,
        # h=102,
        x=fpdf.enums.Align.C,
        keep_aspect_ratio=True,
    )
    # assert_pdf_equal(pdf, HERE / "image_fit_in_rect_with_c_align_center.pdf", tmp_path)
    pdf.output("test_image_fit_in_rect_with_c_align_center.pdf")
    # pdf.


# test_image_fit_in_rect_with_c_align_center()

import win32api
import win32print
import os

current_directory = os.getcwd()


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


def print_pdf(pdf_path: str):
    printer_name = win32print.GetDefaultPrinter()
    try:
        win32api.ShellExecute(0, "print", pdf_path, None, ".", 0)
    except Exception as e:
        print(f"exeption happend at {print_pdf.__name__}{e}")


def test_image_fit_in_rect_with_c_align_center_and_print():
    pdf = fpdf.FPDF()

    pdf.add_page()
    pdf.image(
        name=imgA_path,
        w=72,
        h=102,
        x=fpdf.enums.Align.C,
        keep_aspect_ratio=True,
    )

    pdf_file_name: str = "Image_Fit_In_Rect_With_C_Align.pdf"
    save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )
    # print_pdf(pdf_path=pdf_file_path)


test_image_fit_in_rect_with_c_align_center_and_print()
