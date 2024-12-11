import os
from fpdf import FPDF
import fpdf


class Grid_Generator:
    # A4 Metric: 210 x 297 mm
    def __init__(
        self,
        l_r_margin: float = 5,
        top_margin: float = 5,
    ):
        self.height: int = 125
        self.half_height: int = self.height / 2
        self.width: int = 210
        self.line_distance: int = 5
        self.dash: float = 0.2
        self.gap: float = 1
        self.A4_width: int = 210
        self.l_r_margin: float = l_r_margin
        self.top_margin: float = top_margin

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

    def draw_half_height_line(self, pdf: FPDF, width: float):
        pdf.set_line_width(width=0.5)
        pdf.set_dash_pattern(dash=self.dash, gap=self.gap)
        pdf.set_draw_color(
            r=10,
        )

        x1: float = self.l_r_margin
        y1: float = self.top_margin + self.half_height
        x2: float = width + self.l_r_margin  # self.width  # + (self.line_distance / 2)
        y2: float = self.top_margin + self.half_height

        pdf.line(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
        )

    def draw_horizontal_lines(self, pdf: FPDF):
        pdf.set_line_width(0.05)
        # pdf.set_draw_color(r=255, g=128, b=0)
        # height: int = 125

        count: int = int(self.height / self.line_distance) + 1
        x1: float = self.l_r_margin
        y1: float = self.top_margin
        x2: float = self.width + self.l_r_margin
        y2: float = self.top_margin
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
        # pdf.set_draw_color(r=255, g=128, b=0)
        # width: int = self.width
        count: int = int(self.width / self.line_distance) + 1
        x1: float = self.l_r_margin
        y1: float = self.top_margin  # + self.half_height
        x2: float = self.l_r_margin
        y2: float = self.top_margin + self.height  # + (self.line_distance / 2)
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

    def fill_grid_background(
        self,
        width: float,
        pdf: FPDF,
        fill_color: int = 235,
    ):
        pdf.set_fill_color(r=fill_color)
        pdf.rect(
            x=self.l_r_margin,
            y=self.top_margin,
            w=width,
            h=self.height,  # + self.line_distance / 2
            # style="FD",
            style=fpdf.enums.RenderStyle.DF,
            round_corners=True,
            corner_radius=5,
        )

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

        # pdf.set_draw_color(r=255, g=128, b=0) #orange
        pdf.set_fill_color(180)
        self.draw_half_height_line(pdf=pdf, width=width)
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
        self.draw_half_height_line(pdf=pdf, width=width)

    def draw_grid_03(
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

        self.fill_grid_background(
            width=width,
            pdf=pdf,
        )

        self.draw_half_height_line(pdf=pdf, width=width)
        self.draw_horizontal_lines(pdf=pdf)
        self.draw_vertical_lines(pdf=pdf)


def test_01():
    height: int = 125
    width: int = 150
    line_distance: int = 5
    # current_directory = os.getcwd()
    # output_folder_name: str = "outputs"
    # file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)
    l_r_margin: float = 5
    top_margin: float = 5
    grid_generator: Grid_Generator = Grid_Generator(
        l_r_margin=l_r_margin,
        top_margin=top_margin,
    )
    pdf = FPDF()
    pdf.add_page()
    grid_generator.draw_grid_01(
        pdf=pdf,
        line_distance=line_distance,
        height=height,
        width=width,
    )

    pdf_file_name: str = "Grid_Generator_test_01.pdf"
    grid_generator.save_to_output_folder(
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
    width: int = 150
    line_distance: int = 5
    grid_generator: Grid_Generator = Grid_Generator()
    pdf = FPDF()
    pdf.add_page()
    grid_generator.draw_grid_02(
        pdf=pdf,
        line_distance=line_distance,
        height=height,
        width=width,
    )
    pdf_file_name: str = "Grid_Generator_test_02.pdf"
    grid_generator.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


def test_03():
    height: int = 100
    width: int = 180
    line_distance: int = 5
    pdf = FPDF()
    pdf.add_page()

    l_r_margin: float = 5
    top_margin: float = 5
    grid_generator: Grid_Generator = Grid_Generator(
        l_r_margin=l_r_margin,
        top_margin=top_margin,
    )
    grid_generator.draw_grid_03(
        pdf=pdf,
        line_distance=line_distance,
        height=height,
        width=width,
    )
    pdf_file_name: str = "Grid_Generator_test_03.pdf"
    grid_generator.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )


# Example usage:
if __name__ == "__main__":

    # test_01()
    # test_02()
    test_03()
