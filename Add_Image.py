import os
from fpdf import FPDF
import fpdf


class Add_Image:
    # A4 Metric: 210 x 297 mm
    def __init__(
        self,
        height: int = 300,
        width: int = 300,
    ):
        self.height = height
        self.width = width
        self.half_height: int = self.height / 2

    def save_to_output_folder(
        self,
        pdf: FPDF,
        pdf_file_name: str,
    ):
        current_directory = os.getcwd()
        pdf_file_name: str = pdf_file_name  # "draw_an_hourglass_shape.pdf"
        output_folder_name: str = "outputs"
        file_path: str = os.path.join(
            current_directory, output_folder_name, pdf_file_name
        )
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

    def add_image(
        self,
        pdf: FPDF,
        img_path: str = "",
        width: int = 300,
        height: int = 300,
        y: int = -1,
        orientation: str = "center",
    ):
        X = fpdf.enums.Align.C
        if orientation == "left":
            X = fpdf.enums.Align.L
        if orientation == "right":
            X = fpdf.enums.Align.R
        self.width = width
        self.height = height
        if y == -1:
            y = None
        pdf.image(
            name=img_path,
            w=width,
            h=height,
            x=X,
            y=y,
            keep_aspect_ratio=True,
        )

    def add_image_to_pos(
        self,
        pdf: FPDF,
        img_path: str = "",
        width: int = 300,
        height: int = 300,
        x: int = 0,
        y: int = 0,
    ):

        self.width = width
        self.height = height
        pdf.image(
            name=img_path,
            w=width,
            h=height,
            x=x,
            y=y,
            keep_aspect_ratio=True,
        )

    def add_image_left(
        self,
        pdf: FPDF,
        img_path: str = "",
        width: int = 300,
        height: int = 300,
        y: int = -1,
    ):
        self.width = width
        self.height = height
        if y == -1:
            y = None
        self.add_image(
            pdf=pdf,
            img_path=img_path,
            width=width,
            height=height,
            y=y,
            orientation="left",
        )
        # pdf.image(
        #     name=img_path,
        #     w=width,
        #     h=height,
        #     x=fpdf.enums.Align.L,
        #     y=y,
        #     keep_aspect_ratio=True,
        # )

    def add_image_right(
        self,
        pdf: FPDF,
        img_path: str = "",
        width: int = 300,
        height: int = 300,
        y: int = -1,
    ):
        self.width = width
        self.height = height
        if y == -1:
            y = None
        self.add_image(
            pdf=pdf,
            img_path=img_path,
            width=width,
            height=height,
            y=y,
            orientation="right",
        )
        # pdf.image(
        #     name=img_path,
        #     w=width,
        #     h=height,
        #     x=fpdf.enums.Align.R,
        #     keep_aspect_ratio=True,
        # )

    def add_image_center(
        self,
        pdf: FPDF,
        img_path: str = "",
        width: int = 300,
        height: int = 300,
        y: int = -1,
    ):
        self.width = width
        self.height = height
        if y == -1:
            y = None
        self.add_image(
            pdf=pdf,
            img_path=img_path,
            width=width,
            height=height,
            y=y,
            orientation="center",
        )
        # pdf.image(
        #     name=img_path,
        #     w=width,
        #     h=height,
        #     x=fpdf.enums.Align.C,
        #     # y=fpdf.enums.Align.C,
        #     keep_aspect_ratio=True,
        # )


def test_left():
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    width: int = 50
    height: int = width

    add_image: Add_Image = Add_Image(
        height=height,
        width=width,
    )

    orientations: list[str] = [
        "landscape",
        "portrait",
    ]
    pdf_format: str = "a4"
    margin: float = 0
    pdf = FPDF()
    pdf.add_page(
        orientation=orientations[1],
        format=pdf_format,
    )
    pdf.set_margin(margin=margin)

    add_image.add_image_left(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
    )

    pdf_file_name: str = "Add_Image_test_left.pdf"
    add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_right():
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    width: int = 50
    height: int = width
    margin: float = 0
    orientations: list[str] = [
        "landscape",
        "portrait",
    ]
    pdf_format: str = "a4"

    add_image: Add_Image = Add_Image(
        height=height,
        width=width,
    )
    pdf = FPDF()
    pdf.add_page(
        orientation=orientations[1],
        format=pdf_format,
    )
    pdf.set_margin(margin=margin)
    add_image.add_image_right(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
    )

    pdf_file_name: str = "Add_Image_test_right.pdf"
    add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_center():
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    width: int = 50
    height: int = width
    margin: float = 0
    orientations: list[str] = [
        "landscape",
        "portrait",
    ]
    pdf_format: str = "a4"

    add_image: Add_Image = Add_Image(
        height=height,
        width=width,
    )
    pdf = FPDF()
    pdf.add_page(
        orientation=orientations[1],
        format=pdf_format,
    )
    pdf.set_margin(margin=margin)
    add_image.add_image_center(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
    )

    pdf_file_name: str = "Add_Image_test_center.pdf"
    add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_left_right_center():
    """y (float): optional vertical position where to put the image on the page.
    If not specified or equal to None, the current ordinate is used.
    After the call, the current ordinate is moved to the bottom of the image
    """
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    width: int = 50
    height: int = width
    margin: float = 0
    orientations: list[str] = [
        "landscape",
        "portrait",
    ]
    pdf_format: str = "a4"

    add_image: Add_Image = Add_Image(
        height=height,
        width=width,
    )
    pdf = FPDF()
    pdf.add_page(
        orientation=orientations[1],
        format=pdf_format,
    )
    pdf.set_margin(margin=margin)
    add_image.add_image_left(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
    )
    add_image.add_image_right(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
    )
    add_image.add_image_center(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
    )

    pdf_file_name: str = "Add_Image_test_left_right_center.pdf"
    add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_left_right_center_one_line(y: int = 50):
    """y (float): optional vertical position where to put the image on the page.
    If not specified or equal to None, the current ordinate is used.
    After the call, the current ordinate is moved to the bottom of the image
    """

    orientations: list[str] = [
        "landscape",
        "portrait",
    ]
    pdf_format: str = "a4"
    # y: int = 50

    pdf = FPDF()
    pdf.add_page(
        orientation=orientations[1],
        format=pdf_format,
    )
    pdf.set_margin(margin=margin)

    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    width: int = 50
    height: int = width
    margin: float = 0

    add_image: Add_Image = Add_Image(
        height=height,
        width=width,
    )
    add_image.add_image_left(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
        y=y,
    )
    add_image.add_image_right(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
        y=y,
    )
    add_image.add_image_center(
        pdf=pdf,
        img_path=img_path,
        width=width,
        height=height,
        y=y,
    )

    pdf_file_name: str = "Add_Image_test_left_right_center_one_line.pdf"
    add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


# Example usage:
if __name__ == "__main__":
    test_left()
    test_right()
    test_center()
    test_left_right_center()
    y: int = 0
    test_left_right_center_one_line(y=y)
