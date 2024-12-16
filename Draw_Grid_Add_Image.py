import os
from fpdf import FPDF
from Draw_Grid_2 import Draw_Grid_2
from Add_Image import Add_Image


class Draw_Grid_Add_Image:
    # https://py-pdf.github.io/fpdf2/
    # A4 Metric: 210 x 297 mm
    def __init__(
        self,
        # line_distance: int = 5,
        # grid_height: int = 125,
        # grid_width: int = 209,
    ):
        # self.line_distance = line_distance
        # self.grid_height = grid_height
        # self.grid_width = grid_width
        # self.half_height: int = self.grid_height / 2
        self.grid_drawer: Draw_Grid_2 = Draw_Grid_2()
        self.image_adder: Add_Image = Add_Image()

    def save_to_output_folder(
        self,
        pdf: FPDF,
        pdf_file_name: str,
    ):
        # current_directory = os.getcwd()
        current_directory: str = os.path.dirname(__file__)
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

    def draw_grid_add_image(
        self,
        pdf: FPDF,
        grid_line_distance: int = 5,
        grid_height: int = 125,
        grid_width: int = 209,
        img_path: str = "",
        img_width: int = 50,
        img_height: int = 50,
        y: int = -1,
        orientation: str = "center",
    ):

        self.grid_drawer.draw_grid_01(
            pdf=pdf,
            line_distance=grid_line_distance,
            height=grid_height,
            width=grid_width,
        )
        self.image_adder.add_image(
            pdf=pdf,
            img_path=img_path,
            width=img_width,
            height=img_height,
            y=y,
            orientation=orientation,
        )

    def draw_grid(
        self,
        pdf: FPDF,
        grid_line_distance: int = 5,
        grid_height: int = 125,
        grid_width: int = 209,
        # img_path: str = "",
        # img_width: int = 50,
        # img_height: int = 50,
        # y: int = -1,
        # orientation: str = "center",
    ):
        self.grid_drawer.draw_grid_01(
            pdf=pdf,
            line_distance=grid_line_distance,
            height=grid_height,
            width=grid_width,
        )
        # self.image_adder.add_image(
        #     pdf=pdf,
        #     img_path=img_path,
        #     width=img_width,
        #     height=img_height,
        #     y=y,
        #     orientation=orientation,
        # )

    def add_image(
        self,
        pdf: FPDF,
        img_path: str = "",
        img_width: int = 50,
        img_height: int = 50,
        y: int = -1,
        orientation: str = "center",
    ):

        self.image_adder.add_image(
            pdf=pdf,
            img_path=img_path,
            width=img_width,
            height=img_height,
            y=y,
            orientation=orientation,
        )


def test_draw_grid_add_image_center():

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

    # initialize gird drawer
    draw_grid_add_image: Draw_Grid_Add_Image = Draw_Grid_Add_Image()
    # grid parameters
    grid_line_distance: int = 5
    grid_height: int = 125
    grid_width: int = 209

    # image parameters
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    img_width: int = 50
    img_height: int = img_width
    y: int = -1
    orientation: str = "center"

    draw_grid_add_image.draw_grid_add_image(
        pdf=pdf,
        grid_line_distance=grid_line_distance,
        grid_height=grid_height,
        grid_width=grid_width,
        img_path=img_path,
        img_width=img_width,
        img_height=img_height,
        y=y,
        orientation=orientation,
    )

    pdf_file_name: str = "Draw_Grid_Add_Image_center.pdf"
    draw_grid_add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_draw_grid_add_image_left():

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

    # initialize gird drawer
    draw_grid_add_image: Draw_Grid_Add_Image = Draw_Grid_Add_Image()
    # grid parameters
    grid_line_distance: int = 5
    grid_height: int = 125
    grid_width: int = 209
    # image parameters
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    img_width: int = 50
    img_height: int = img_width
    y: int = -1
    orientation: str = "left"

    draw_grid_add_image.draw_grid_add_image(
        pdf=pdf,
        grid_line_distance=grid_line_distance,
        grid_height=grid_height,
        grid_width=grid_width,
        img_path=img_path,
        img_width=img_width,
        img_height=img_height,
        y=y,
        orientation=orientation,
    )

    pdf_file_name: str = "Draw_Grid_Add_Image_left.pdf"
    draw_grid_add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_draw_grid_add_image_right():

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

    # initialize gird drawer
    draw_grid_add_image: Draw_Grid_Add_Image = Draw_Grid_Add_Image()
    # grid parameters
    grid_line_distance: int = 5
    grid_height: int = 125
    grid_width: int = 209
    # image parameters
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    img_width: int = 50
    img_height: int = img_width
    y: int = -1
    orientation: str = "right"

    draw_grid_add_image.draw_grid_add_image(
        pdf=pdf,
        grid_line_distance=grid_line_distance,
        grid_height=grid_height,
        grid_width=grid_width,
        img_path=img_path,
        img_width=img_width,
        img_height=img_height,
        y=y,
        orientation=orientation,
    )

    pdf_file_name: str = "Draw_Grid_Add_Image_right.pdf"
    draw_grid_add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_draw_grid_add_image_left_right_center(y: int = 10):

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

    # initialize gird drawer
    draw_grid_add_image: Draw_Grid_Add_Image = Draw_Grid_Add_Image()
    # grid parameters
    grid_line_distance: int = 5
    grid_height: int = 125
    grid_width: int = 209
    draw_grid_add_image.draw_grid(
        pdf=pdf,
        grid_line_distance=grid_line_distance,
        grid_height=grid_height,
        grid_width=grid_width,
    )
    # image parameters
    img_path: str = r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png"
    img_width: int = 50
    img_height: int = img_width

    orientation: str = "left"
    draw_grid_add_image.add_image(
        pdf=pdf,
        img_path=img_path,
        img_width=img_width,
        img_height=img_height,
        y=y,
        orientation=orientation,
    )
    orientation: str = "right"
    draw_grid_add_image.add_image(
        pdf=pdf,
        img_path=img_path,
        img_width=img_width,
        img_height=img_height,
        y=y,
        orientation=orientation,
    )
    orientation: str = "center"
    draw_grid_add_image.add_image(
        pdf=pdf,
        img_path=img_path,
        img_width=img_width,
        img_height=img_height,
        y=y,
        orientation=orientation,
    )

    pdf_file_name: str = "Draw_Grid_Add_Image_left_right_center.pdf"
    draw_grid_add_image.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


# Example usage:
if __name__ == "__main__":
    test_draw_grid_add_image_center()
    test_draw_grid_add_image_left()
    test_draw_grid_add_image_right()
    y: int = 10
    test_draw_grid_add_image_left_right_center(y=y)
