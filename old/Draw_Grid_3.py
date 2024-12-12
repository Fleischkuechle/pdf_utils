import os
from fpdf import FPDF
import fpdf


class Draw_Grid_3:
    # A4 Metric: 210 x 297 mm
    def __init__(self):
        self.height: int = 125
        self.half_height: int = self.height / 2
        self.width: int = 209
        self.line_distance: int = 5
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
        pdf.set_dash_pattern(dash=2, gap=3)
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


def test_grid():
    draw_grid_2: Draw_Grid_3 = Draw_Grid_3()
    pdf = FPDF()
    pdf.add_page()
    draw_grid_2.draw_horizontal_lines(pdf=pdf)
    draw_grid_2.draw_vertical_lines(pdf=pdf)
    draw_grid_2.draw_half_height_line(pdf=pdf)
    # file_path: str = "Draw_Grid_3.pdf"
    pdf_file_name: str = "Draw_Grid_3.pdf"
    draw_grid_2.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )
    # try:
    #     pdf.output(name=file_path)
    #     print(f"completed saved here {file_path}")
    # except Exception as e:
    #     print(f"exception: {e}")

    # current_directory = os.getcwd()
    # pdf_file_name: str = "draw_grid_2_test_02.pdf"
    # output_folder_name: str = "outputs"
    # file_path: str = os.path.join(current_directory, output_folder_name, pdf_file_name)


# Example usage:
if __name__ == "__main__":
    test_grid()
