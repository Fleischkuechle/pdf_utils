import os
from turtle import pd
from fpdf import FPDF
import fpdf


class Draw_Grid_2:
    # A4 Metric: 210 x 297 mm
    def __init__(self):
        self.height: int = 125
        self.half_height: int = self.height / 2
        self.width: int = 209
        self.line_distance: int = 5
        self.dash: float = 0.2
        self.gap: float = 1

        pass

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

    def draw_half_height_line(self, pdf: FPDF):
        pdf.set_line_width(width=0.5)
        pdf.set_dash_pattern(dash=self.dash, gap=self.gap)
        pdf.set_draw_color(
            r=10,
            # g=-1,
            # b=-1,
        )
        # pdf.set_draw_color(r=0, g=128, b=255)
        # height: int = 125

        x1: float = 1
        y1: float = self.half_height
        x2: float = self.width  # + (self.line_distance / 2)
        y2: float = self.half_height

        pdf.line(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
        )

    def draw_horizontal_lines(self, pdf: FPDF):
        pdf.set_line_width(0.05)
        pdf.set_draw_color(r=255, g=128, b=0)
        # height: int = 125

        count: int = int(self.height / self.line_distance) + 1
        x1: float = 1
        y1: float = 1
        x2: float = self.width  # + (self.line_distance / 2)
        y2: float = 1
        y_line_distance: int = 1
        for i in range(count):
            pdf.line(
                x1=x1,
                y1=y1,
                x2=x2,
                y2=y2,
            )
            y1 = y1 + self.line_distance
            y2 = y2 + self.line_distance

    def draw_vertical_lines(self, pdf: FPDF):
        pdf.set_line_width(0.05)
        pdf.set_draw_color(r=255, g=128, b=0)
        # width: int = self.width
        count: int = int(self.width / self.line_distance) + 1
        x1: float = 1
        y1: float = 1
        x2: float = 1
        y2: float = self.height + (self.line_distance / 2)
        # x_line_distance: int = 1
        for i in range(count):
            pdf.line(
                x1=x1,
                y1=y1,
                x2=x2,
                y2=y2,
            )
            x1 = x1 + self.line_distance
            x2 = x2 + self.line_distance

    def draw_grid_01(
        self,
        pdf: FPDF,
        line_distance: int,
        height: int,
        width: int,
    ):
        self.line_distance = line_distance
        self.height = height
        self.width = width
        self.half_height: int = self.height / 2
        self.draw_half_height_line(pdf=pdf)
        self.draw_horizontal_lines(pdf=pdf)
        self.draw_vertical_lines(pdf=pdf)

    def draw_grid_02(
        self,
        pdf: FPDF,
        line_distance: int,
        height: int,
        width: int,
    ):
        self.line_distance = line_distance
        self.height = height
        self.width = width
        self.half_height: int = self.height / 2
        self.draw_horizontal_lines(pdf=pdf)
        self.draw_vertical_lines(pdf=pdf)
        self.draw_half_height_line(pdf=pdf)


def test_01():
    height: int = 125
    width: int = 209
    line_distance: int = 5
    # current_directory = os.getcwd()
    # output_folder_name: str = "outputs"
    # file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)

    draw_grid_2: Draw_Grid_2 = Draw_Grid_2()
    pdf = FPDF()
    pdf.add_page()
    draw_grid_2.draw_grid_01(
        pdf=pdf,
        line_distance=line_distance,
        height=height,
        width=width,
    )

    pdf_file_name: str = "draw_grid_2_test_01.pdf"
    draw_grid_2.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )
    # try:
    #     pdf.output(name=file_path)
    #     print(" ")
    #     print(f"completed saved here: {file_path}")

    # except Exception as e:
    #     print(" ")
    #     print(f"exception: {e}")


def test_02():
    height: int = 125
    width: int = 209
    line_distance: int = 5
    # current_directory = os.getcwd()
    # pdf_file_name: str = "draw_grid_2_test_02.pdf"
    # output_folder_name: str = "outputs"
    # file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)

    draw_grid_2: Draw_Grid_2 = Draw_Grid_2()
    pdf = FPDF()
    pdf.add_page()
    draw_grid_2.draw_grid_02(
        pdf=pdf,
        line_distance=line_distance,
        height=height,
        width=width,
    )
    pdf_file_name: str = "draw_grid_2_test_02.pdf"
    draw_grid_2.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )
    # try:
    #     pdf.output(name=file_path)
    #     print(" ")
    #     print(f"completed saved here: {file_path}")
    # except Exception as e:

    #     print(" ")
    #     print(f"exception: {e}")


# Example usage:
if __name__ == "__main__":

    test_01()
    # test_02()
