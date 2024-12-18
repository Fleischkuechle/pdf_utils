import datetime
import io
import os
from fpdf import FPDF
from fpdf.output import PDFPage
import fpdf
import fpdf.output
from .Grid_Generator import Grid_Generator
from .Add_Image import Add_Image

from PIL import Image as pil_img


class Draw_Wallet:
    # https://py-pdf.github.io/fpdf2/
    # A4 Metric: 210 x 297 mm
    def __init__(
        self,
        l_r_margin: float = 5,
        top_margin: float = 5,
    ):
        self.l_r_margin: float = l_r_margin
        self.top_margin: float = top_margin
        self.grid_line_distance: int = 5
        # self.current_directory:str = os.getcwd()

        self.current_directory: str = os.path.dirname(__file__)
        self.doge_logo_file_name: str = "dogecoin.png"  # "draw_an_hourglass_shape.pdf"
        self.logos_folder_name: str = "logos"
        self.doge_logo_path: str = os.path.join(
            self.current_directory,
            self.logos_folder_name,
            self.doge_logo_file_name,
        )
        self.doge_logo_file_name_2: str = "doge_alien.jpg"

        self.doge_logo_path_2: str = os.path.join(
            self.current_directory,
            self.logos_folder_name,
            self.doge_logo_file_name_2,
        )
        self.donate_folder_name: str = "donate"
        self.donate_Doge_qr_image_name: str = "D68GeLDEN2WiBZU7WtW8QtvWkS1ApEnTeN.png"
        self.donate_Doge_address: str = "D68GeLDEN2WiBZU7WtW8QtvWkS1ApEnTeN"

        self.donate_text: str = (
            "Donations are welcome this is the developers doge coin address."
        )
        self.donate_img_width: int = 80
        self.donate_img_height: int = self.donate_img_width
        self.donate_y_offset: float = self.donate_img_height / 2 + 20
        self.donate_Doge_qr_image_path: str = os.path.join(
            self.current_directory,
            self.donate_folder_name,
            self.donate_Doge_qr_image_name,
        )
        self.logo_width_1: int = 50
        self.logo_height_1: int = self.logo_width_1
        self.logo_width_2: int = 10
        self.logo_height_2: int = self.logo_width_2

        # A4 Metric: 210 x 297 mm
        self.A4_width: int = 210

        self.grid_width: int = self.A4_width - 2 * self.l_r_margin
        # self.A4_middle_width: int = self.A4_width / 2
        self.A4_middle_width: int = self.grid_width / 2
        self.columns_count = 3
        # self.column_width: int = self.A4_width / self.columns_count
        self.column_width: int = self.grid_width / self.columns_count
        self.column_1_border: int = self.l_r_margin + self.column_width
        self.column_2_border: int = (
            self.l_r_margin + self.column_width + self.column_width
        )
        self.column_3_border: int = (
            self.l_r_margin + self.column_width + self.column_width + self.column_width
        )

        self.column_1_mid: int = self.l_r_margin + self.column_width / 2
        self.column_2_mid: int = (
            self.l_r_margin + self.column_width + self.column_width / 2
        )
        self.column_3_mid: int = (
            self.l_r_margin
            + self.column_width
            + self.column_width
            + self.column_width / 2
        )

        self.credit_card_height_mm: float = 54
        self.row_height: float = (
            self.credit_card_height_mm
        )  # self.grid_height / self.rows_count
        self.rows_count: int = 2
        # self.grid_height: int = 125
        self.grid_height: int = self.rows_count * self.credit_card_height_mm
        self.half_height: int = self.grid_height / 2
        self.dash: float = 0.2
        self.gap: float = 1

        self.row_1_mid: int = self.top_margin + self.row_height / 2
        self.row_2_mid: int = self.top_margin + self.row_height + self.row_height / 2
        self.text_size_1: int = 15
        self.font_size_1: int = 15
        self.text_size_2: int = 10
        self.text_size_3: int = 13
        self.text_size_4: int = 20
        self.x_offset: int = 0

        self.img_width: int = 50
        self.img_height: int = self.img_width
        self.grid_generator: Grid_Generator = Grid_Generator(
            l_r_margin=self.l_r_margin,
            top_margin=self.top_margin,
        )
        self.image_adder: Add_Image = Add_Image()

    def draw_vert_fold_lines(self, pdf: FPDF):
        pdf.set_line_width(width=0.5)
        pdf.set_dash_pattern(dash=self.dash, gap=self.gap)
        pdf.set_draw_color(
            r=10,
        )

        pdf.line(
            x1=self.column_1_border,
            y1=self.top_margin,
            x2=self.column_1_border,
            y2=self.top_margin + self.grid_height,
        )
        pdf.line(
            x1=self.column_2_border,
            y1=self.top_margin,
            x2=self.column_2_border,
            y2=self.top_margin + self.grid_height,
        )
        # pdf.line(
        #     x1=self.column_3_border,
        #     y1=self.top_margin,
        #     x2=self.column_3_border,
        #     y2=self.top_margin + self.grid_height,
        # )

    def save_to_output_folder(
        self,
        pdf: FPDF,
        pdf_file_name: str,
    ) -> str:
        # current_directory = os.getcwd()
        current_directory: str = os.path.dirname(__file__)
        pdf_file_name: str = pdf_file_name  # "draw_an_hourglass_shape.pdf"
        output_folder_name: str = "outputs"
        file_path: str = os.path.join(
            current_directory, output_folder_name, pdf_file_name
        )
        # pdf.output(file_path)
        # some_page:fpdf.output.PDFPage=  PDF.pages[1]
        # some_page.
        # page: PDFPage = pdf.pages[1]

        try:
            pdf.output(
                name=file_path,
            )
            print(" ")
            print(f"saved pdf here: {file_path}")
            return file_path
        except Exception as e:

            print(" ")
            print(f"exception: {e}")

    def add_vertical_text_to_pos(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        x: int = 0,
        y: int = 0,
        angle: float = 90,
        text_size: int = 50,
    ):

        pdf.set_font("Times", size=text_size)
        with pdf.rotation(
            angle=angle,
            x=x,
            y=y,
        ):
            pdf.text(
                x=x,
                y=y,
                text=text,
            )

    def add_vertical_text_to_pos_2(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        x: int = 0,
        y: int = 0,
        angle: float = 90,
        text_size: int = 50,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        with pdf.rotation(
            angle=angle,
            # x=x,
            # y=y,
        ):
            pdf.cell(
                w=self.img_height,
                # x=x,
                # y=y,
                text=text,
                fill=True,
                align=fpdf.enums.Align.C,
            )

    def add_vertical_text_to_pos_3(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        # x: int = 0,
        # y: int = 0,
        angle: float = 90,
        text_size: int = 50,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        with pdf.rotation(
            angle=angle,
            # x=x,
            # y=y,
        ):
            # pdf.cell(
            #     w=self.img_height,
            #     # x=x,
            #     # y=y,
            #     text=text,
            #     # fill=True,
            #     align=fpdf.enums.Align.C,
            # )
            pdf.multi_cell(
                # w=self.img_height,
                w=self.row_height - 3,
                # x=x,
                # y=y,
                text=text,
                fill=True,
                align=fpdf.enums.Align.C,
            )

    def add_horizontal_text_to_pos_C(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        x: int = 0,
        y: int = 0,
        text_size: int = 50,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        pdf.set_xy(
            x=x,
            y=y,
        )
        pdf.multi_cell(
            text=text,
            w=self.column_width,
            # fill=True,
            align=fpdf.enums.Align.C,
        )

    def add_horizontal_text_to_pos_C_width(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        x: int = 0,
        y: int = 0,
        text_size: int = 50,
        text_witdth: float = 100,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        pdf.set_xy(
            x=x,
            y=y,
        )
        pdf.multi_cell(
            text=text,
            w=text_witdth,
            # fill=True,
            align=fpdf.enums.Align.C,
        )

    def add_horizontal_text_to_pos_C_fill(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        x: int = 0,
        y: int = 0,
        text_size: int = 50,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        self.font_size_1 = pdf.font_size
        pdf.set_xy(
            x=x,
            y=y,
        )
        pdf.multi_cell(
            text=text,
            w=self.img_width + pdf.font_size,
            fill=True,
            align=fpdf.enums.Align.C,
        )

    def add_horizontal_text_to_pos_L(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        x: int = 0,
        y: int = 0,
        text_size: int = 50,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        pdf.set_xy(
            x=x,
            y=y,
        )
        pdf.multi_cell(
            text=text,
            w=self.img_width + self.font_size_1,
            fill=True,
            align=fpdf.enums.Align.L,
        )

    def add_white_sqare_to_pos(
        self,
        pdf: FPDF,
        x: float = 0,
        y: float = 0,
        w: float = 100,
        h: float = 100,
    ):
        pdf.set_fill_color(255)
        pdf.rect(
            x=x,
            y=y,
            w=w,
            h=h,
            # style="FD",
            style=fpdf.enums.RenderStyle.F,
            round_corners=True,
            corner_radius=5,
        )

    def draw_wallet(
        self,
        pdf: FPDF,
        priv_key: str = "",
        priv_qr_img_path: str = "",
        pub_address: str = "",
        pub_qr_img_path: str = "",
    ):

        self.grid_generator.draw_grid_03(
            pdf=pdf,
            line_distance=self.grid_line_distance,
            height=self.grid_height,
            width=self.grid_width,
        )
        self.draw_vert_fold_lines(pdf=pdf)
        # public qr code to column3  and row 2
        pub_qr_x: int = self.column_3_mid - (self.img_width / 2) - self.x_offset
        pub_qr_y: int = self.row_2_mid - self.img_height / 2
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=pub_qr_img_path,
            width=self.img_width,
            height=self.img_height,
            x=pub_qr_x,
            y=pub_qr_y,
        )
        # private qr code to column 2(middle) row 1
        priv_qr_x: int = self.column_2_mid - (self.img_width / 2) - self.x_offset
        priv_qr_y: int = self.row_1_mid - self.img_height / 2
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=priv_qr_img_path,
            width=self.img_width,
            height=self.img_height,
            x=priv_qr_x,
            y=priv_qr_y,
        )
        # add logo to column 1 row 2
        logo_x: int = self.column_1_mid - (self.logo_width_1 / 2)  # - self.x_offset
        logo_y: int = self.row_2_mid - self.logo_height_1 / 2
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path_2,
            width=self.logo_width_1,
            height=self.logo_height_1,
            x=logo_x,
            y=logo_y,
        )

        pdf.set_fill_color(255, 0, 0)  # red
        text_1: str = "Private"
        # text_size: int = 25
        text_angle: float = 90
        pdf.set_xy(
            x=priv_qr_x - (self.text_size_1 / 3),
            y=priv_qr_y + self.img_height,
        )
        self.add_vertical_text_to_pos_2(
            pdf=pdf,
            text=text_1,
            angle=text_angle,
            text_size=self.text_size_1,
        )

        pdf.set_fill_color(0, 255, 0)  # green
        text_2: str = "Public"
        text_2_x: float = pub_qr_x - (self.text_size_1 / 3)
        text_2_y: float = pub_qr_y + self.img_height
        pdf.set_xy(
            x=text_2_x,
            y=text_2_y,
        )
        self.add_vertical_text_to_pos_2(
            pdf=pdf,
            text=text_2,
            angle=text_angle,
            text_size=self.text_size_1,
        )

        # priv_key
        pdf.set_xy(
            x=priv_qr_x + self.img_width - self.x_offset / 2,  # (self.text_size_1 / 3)
            y=priv_qr_y + self.img_height,
        )
        # column 1 row 1
        text_2_2_x: float = self.column_1_mid - (self.img_width / 2) - self.x_offset
        text_2_2_y: float = priv_qr_y + pdf.font_size
        self.add_horizontal_text_to_pos_C_fill(
            pdf=pdf,
            text=text_2,
            x=text_2_2_x,
            y=text_2_2_y,
            text_size=self.text_size_1,
        )

        pdf.set_fill_color(255, 255, 255)  # white
        text_2_3_y: float = text_2_2_y + pdf.font_size
        self.add_horizontal_text_to_pos_L(
            pdf=pdf,
            text=pub_address,
            x=text_2_2_x,
            y=text_2_3_y,
            text_size=self.text_size_1,
        )
        text_1_2_y: float = (
            text_2_2_y + self.font_size_1 + self.font_size_1 + self.font_size_1
        )
        pdf.set_fill_color(255, 0, 0)  # red
        self.add_horizontal_text_to_pos_C_fill(
            pdf=pdf,
            text=text_1,
            x=text_2_2_x,
            y=text_1_2_y,
            text_size=self.text_size_1,
        )
        pdf.set_fill_color(255, 255, 255)  # white
        text_1_3_y: float = text_1_2_y + pdf.font_size
        self.add_horizontal_text_to_pos_L(
            pdf=pdf,
            text=priv_key,
            x=text_2_2_x,
            y=text_1_3_y,
            text_size=self.text_size_1,
        )

        sqare_x: float = self.column_1_border + 2
        sqare_y: float = self.top_margin + self.half_height + 2
        sqare_w: float = self.column_width - 4
        sqare_h: float = self.row_height - 4
        self.add_white_sqare_to_pos(
            pdf=pdf,
            x=sqare_x,
            y=sqare_y,
            w=sqare_w,
            h=sqare_h,
        )
        date_x: int = self.column_1_border  # + (self.text_size_2 / 3)
        date_y: int = self.top_margin + self.half_height + 2  # + (self.text_size_2 / 4)
        # Get the current date and time
        now = datetime.datetime.now()

        # Format the date and time as a string
        date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")

        self.add_horizontal_text_to_pos_C(
            pdf=pdf,
            text=date_time_string,
            x=date_x,
            y=date_y,
            text_size=self.text_size_2,
        )
        logo_x = self.column_2_mid - (self.logo_width_2 / 2)  # - self.x_offset
        logo_y = self.row_2_mid - (self.logo_height_2 / 2)
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path,
            width=self.logo_width_2,
            height=self.logo_height_2,
            x=logo_x,
            y=logo_y,
        )
        # # #logo column 1 row 1
        # logo_x = self.column_1_mid - (self.logo_width_2 / 2)
        # logo_y = self.row_1_mid - (self.logo_height_2 / 2)
        # self.image_adder.add_image_to_pos(
        #     pdf=pdf,
        #     img_path=self.doge_logo_path,
        #     width=self.logo_width_2,
        #     height=self.logo_height_2,
        #     x=logo_x,
        #     y=logo_y,
        # )
        # logo column 3 row 1
        logo_x = self.column_3_mid - (self.logo_width_2 / 2)
        logo_y = self.row_1_mid - (self.logo_height_2 / 2)
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path,
            width=self.logo_width_2,
            height=self.logo_height_2,
            x=logo_x,
            y=logo_y,
        )

    def draw_wallet_return_bytes(
        self,
        # pdf: FPDF,
        priv_key: str = "",
        priv_qr_img_path: str = "",
        pub_address: str = "",
        pub_qr_img_path: str = "",
    ) -> bytes:

        # cerate a empty pdf
        pdf: FPDF = self.create_pdf()
        self.grid_generator.draw_grid_03(
            pdf=pdf,
            line_distance=self.grid_line_distance,
            height=self.grid_height,
            width=self.grid_width,
        )
        self.draw_vert_fold_lines(pdf=pdf)
        # public qr code to column3  and row 2
        pub_qr_x: int = self.column_3_mid - (self.img_width / 2) - self.x_offset
        pub_qr_y: int = self.row_2_mid - self.img_height / 2
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=pub_qr_img_path,
            width=self.img_width,
            height=self.img_height,
            x=pub_qr_x,
            y=pub_qr_y,
        )
        # private qr code to column 2(middle) row 1
        priv_qr_x: int = self.column_2_mid - (self.img_width / 2) - self.x_offset
        priv_qr_y: int = self.row_1_mid - self.img_height / 2
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=priv_qr_img_path,
            width=self.img_width,
            height=self.img_height,
            x=priv_qr_x,
            y=priv_qr_y,
        )
        # add logo to column 1 row 2
        logo_x: int = self.column_1_mid - (self.logo_width_1 / 2)  # - self.x_offset
        logo_y: int = self.row_2_mid - self.logo_height_1 / 2
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path_2,
            width=self.logo_width_1,
            height=self.logo_height_1,
            x=logo_x,
            y=logo_y,
        )

        pdf.set_fill_color(255, 0, 0)  # red
        text_1: str = "Private"
        # text_size: int = 25
        text_angle: float = 90
        pdf.set_xy(
            x=priv_qr_x - (self.text_size_1 / 3),
            y=priv_qr_y + self.img_height,
        )
        self.add_vertical_text_to_pos_2(
            pdf=pdf,
            text=text_1,
            angle=text_angle,
            text_size=self.text_size_1,
        )

        pdf.set_fill_color(0, 255, 0)  # green
        text_2: str = "Public"
        text_2_x: float = pub_qr_x - (self.text_size_1 / 3)
        text_2_y: float = pub_qr_y + self.img_height
        pdf.set_xy(
            x=text_2_x,
            y=text_2_y,
        )
        self.add_vertical_text_to_pos_2(
            pdf=pdf,
            text=text_2,
            angle=text_angle,
            text_size=self.text_size_1,
        )

        # priv_key
        pdf.set_xy(
            x=priv_qr_x + self.img_width - self.x_offset / 2,  # (self.text_size_1 / 3)
            y=priv_qr_y + self.img_height,
        )
        # column 1 row 1
        text_2_2_x: float = self.column_1_mid - (self.img_width / 2) - self.x_offset
        text_2_2_y: float = priv_qr_y + pdf.font_size
        self.add_horizontal_text_to_pos_C_fill(
            pdf=pdf,
            text=text_2,
            x=text_2_2_x,
            y=text_2_2_y,
            text_size=self.text_size_1,
        )

        pdf.set_fill_color(255, 255, 255)  # white
        text_2_3_y: float = text_2_2_y + pdf.font_size
        self.add_horizontal_text_to_pos_L(
            pdf=pdf,
            text=pub_address,
            x=text_2_2_x,
            y=text_2_3_y,
            text_size=self.text_size_1,
        )
        text_1_2_y: float = (
            text_2_2_y + self.font_size_1 + self.font_size_1 + self.font_size_1
        )
        pdf.set_fill_color(255, 0, 0)  # red
        self.add_horizontal_text_to_pos_C_fill(
            pdf=pdf,
            text=text_1,
            x=text_2_2_x,
            y=text_1_2_y,
            text_size=self.text_size_1,
        )
        pdf.set_fill_color(255, 255, 255)  # white
        text_1_3_y: float = text_1_2_y + pdf.font_size
        self.add_horizontal_text_to_pos_L(
            pdf=pdf,
            text=priv_key,
            x=text_2_2_x,
            y=text_1_3_y,
            text_size=self.text_size_1,
        )

        sqare_x: float = self.column_1_border + 2
        sqare_y: float = self.top_margin + self.half_height + 2
        sqare_w: float = self.column_width - 4
        sqare_h: float = self.row_height - 4
        self.add_white_sqare_to_pos(
            pdf=pdf,
            x=sqare_x,
            y=sqare_y,
            w=sqare_w,
            h=sqare_h,
        )
        date_x: int = self.column_1_border  # + (self.text_size_2 / 3)
        date_y: int = self.top_margin + self.half_height + 2  # + (self.text_size_2 / 4)
        # Get the current date and time
        now = datetime.datetime.now()

        # Format the date and time as a string
        date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")

        self.add_horizontal_text_to_pos_C(
            pdf=pdf,
            text=date_time_string,
            x=date_x,
            y=date_y,
            text_size=self.text_size_2,
        )
        logo_x = self.column_2_mid - (self.logo_width_2 / 2)  # - self.x_offset
        logo_y = self.row_2_mid - (self.logo_height_2 / 2)
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path,
            width=self.logo_width_2,
            height=self.logo_height_2,
            x=logo_x,
            y=logo_y,
        )
        # # #logo column 1 row 1
        # logo_x = self.column_1_mid - (self.logo_width_2 / 2)
        # logo_y = self.row_1_mid - (self.logo_height_2 / 2)
        # self.image_adder.add_image_to_pos(
        #     pdf=pdf,
        #     img_path=self.doge_logo_path,
        #     width=self.logo_width_2,
        #     height=self.logo_height_2,
        #     x=logo_x,
        #     y=logo_y,
        # )
        # logo column 3 row 1
        logo_x = self.column_3_mid - (self.logo_width_2 / 2)
        logo_y = self.row_1_mid - (self.logo_height_2 / 2)
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path,
            width=self.logo_width_2,
            height=self.logo_height_2,
            x=logo_x,
            y=logo_y,
        )
        # Save the PDF to a bytes buffer
        # pdf_output: io.BytesIO = io.BytesIO()
        # pdf.output(pdf_output)
        pdf_as_bytes: bytes = pdf.output()
        # pdf_output.seek(0)  # Move to the beginning of the BytesIO buffer
        # pdf_as_bytes: bytes = pdf_output.read()
        return pdf_as_bytes  # pdf_output.read()

    def draw_wallet_return_bytes_2(
        self,
        pub_address: str,
        pub_address_qr_img: pil_img.Image,
        privkey: str,
        privkey_qr_img: pil_img.Image,
    ) -> bytes:
        # cerate a empty pdf
        pdf: FPDF = self.create_pdf()
        self.draw_wallet_main(
            pdf=pdf,
            pub_address=pub_address,
            pub_address_qr_img=pub_address_qr_img,
            privkey=privkey,
            privkey_qr_img=privkey_qr_img,
        )

        pdf_as_bytes: bytes = pdf.output()
        return pdf_as_bytes

    def draw_wallet_main(
        self,
        pdf: FPDF,
        pub_address: str,
        pub_address_qr_img: pil_img.Image,
        privkey: str,
        privkey_qr_img: pil_img.Image,
    ) -> FPDF:

        self.grid_generator.draw_grid_03(
            pdf=pdf,
            line_distance=self.grid_line_distance,
            height=self.grid_height,
            width=self.grid_width,
        )
        self.draw_vert_fold_lines(pdf=pdf)
        # public qr code to column3  and row 2
        pub_qr_x: int = self.column_3_mid - (self.img_width / 2) - self.x_offset
        pub_qr_y: int = self.row_2_mid - self.img_height / 2
        self.image_adder.add_image_to_pos_from_pil_img(
            pdf=pdf,
            pil_img=pub_address_qr_img,
            width=self.img_width,
            height=self.img_height,
            x=pub_qr_x,
            y=pub_qr_y,
        )
        # private qr code to column 2(middle) row 1
        priv_qr_x: int = self.column_2_mid - (self.img_width / 2) - self.x_offset
        priv_qr_y: int = self.row_1_mid - self.img_height / 2
        self.image_adder.add_image_to_pos_from_pil_img(
            pdf=pdf,
            pil_img=privkey_qr_img,
            width=self.img_width,
            height=self.img_height,
            x=priv_qr_x,
            y=priv_qr_y,
        )
        # add logo to column 1 row 2
        logo_x: int = self.column_1_mid - (self.logo_width_1 / 2)  # - self.x_offset
        logo_y: int = self.row_2_mid - self.logo_height_1 / 2
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path_2,
            width=self.logo_width_1,
            height=self.logo_height_1,
            x=logo_x,
            y=logo_y,
        )

        pdf.set_fill_color(255, 0, 0)  # red
        text_1: str = "Private"
        # text_size: int = 25
        text_angle: float = 90
        pdf.set_xy(
            x=priv_qr_x - (self.text_size_1 / 3),
            y=priv_qr_y + self.img_height,
        )
        self.add_vertical_text_to_pos_2(
            pdf=pdf,
            text=text_1,
            angle=text_angle,
            text_size=self.text_size_1,
            # text_size=self.text_size_3,
        )

        pdf.set_fill_color(0, 255, 0)  # green
        text_2: str = "Public"
        text_2_x: float = pub_qr_x - (self.text_size_1 / 3)
        text_2_y: float = pub_qr_y + self.img_height
        pdf.set_xy(
            x=text_2_x,
            y=text_2_y,
        )
        self.add_vertical_text_to_pos_2(
            pdf=pdf,
            text=text_2,
            angle=text_angle,
            text_size=self.text_size_1,
            # text_size=self.text_size_3,
        )

        # priv_key
        pdf.set_xy(
            x=priv_qr_x + self.img_width - self.x_offset / 2,  # (self.text_size_1 / 3)
            y=priv_qr_y + self.img_height,
        )
        # column 1 row 1
        text_2_2_x: float = self.column_1_mid - (self.img_width / 2) - self.x_offset
        text_2_2_y: float = priv_qr_y + pdf.font_size
        self.add_horizontal_text_to_pos_C_fill(
            pdf=pdf,
            text=text_2,
            x=text_2_2_x,
            y=text_2_2_y,
            # text_size=self.text_size_1,
            text_size=self.text_size_3,
        )
        # adding public address
        pdf.set_fill_color(255, 255, 255)  # white
        text_2_3_y: float = text_2_2_y + pdf.font_size
        self.add_horizontal_text_to_pos_L(
            pdf=pdf,
            text=pub_address,
            x=text_2_2_x,
            y=text_2_3_y,
            # text_size=self.text_size_1,
            text_size=self.text_size_3,
        )
        text_1_2_y: float = (
            text_2_2_y + self.font_size_1 + self.font_size_1 + self.font_size_1
        )
        # adding private label
        pdf.set_fill_color(255, 0, 0)  # red
        self.add_horizontal_text_to_pos_C_fill(
            pdf=pdf,
            text=text_1,
            x=text_2_2_x,
            y=text_1_2_y,
            # text_size=self.text_size_1,
            text_size=self.text_size_3,
        )
        # adding private key
        pdf.set_fill_color(255, 255, 255)  # white
        text_1_3_y: float = text_1_2_y + pdf.font_size
        self.add_horizontal_text_to_pos_L(
            pdf=pdf,
            text=privkey,
            x=text_2_2_x,
            y=text_1_3_y,
            # text_size=self.text_size_1,
            text_size=self.text_size_3,
        )

        sqare_x: float = self.column_1_border + 2
        sqare_y: float = self.top_margin + self.half_height + 2
        sqare_w: float = self.column_width - 4
        sqare_h: float = self.row_height - 4
        self.add_white_sqare_to_pos(
            pdf=pdf,
            x=sqare_x,
            y=sqare_y,
            w=sqare_w,
            h=sqare_h,
        )
        date_x: int = self.column_1_border  # + (self.text_size_2 / 3)
        date_y: int = self.top_margin + self.half_height + 2  # + (self.text_size_2 / 4)
        # Get the current date and time
        now = datetime.datetime.now()

        # Format the date and time as a string
        date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")

        self.add_horizontal_text_to_pos_C(
            pdf=pdf,
            text=date_time_string,
            x=date_x,
            y=date_y,
            text_size=self.text_size_2,
        )
        logo_x = self.column_2_mid - (self.logo_width_2 / 2)  # - self.x_offset
        logo_y = self.row_2_mid - (self.logo_height_2 / 2)
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path,
            width=self.logo_width_2,
            height=self.logo_height_2,
            x=logo_x,
            y=logo_y,
        )
        # logo column 3 row 1
        logo_x = self.column_3_mid - (self.logo_width_2 / 2)
        logo_y = self.row_1_mid - (self.logo_height_2 / 2)
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.doge_logo_path,
            width=self.logo_width_2,
            height=self.logo_height_2,
            x=logo_x,
            y=logo_y,
        )

        # donate image
        donate_qr_image_x = self.column_2_mid - (self.donate_img_width / 2)
        donate_qr_image_y = (
            self.row_height
            + self.row_height
            - (self.donate_img_height / 2)
            + self.donate_y_offset
            + 10
        )
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=self.donate_Doge_qr_image_path,
            width=self.donate_img_width,
            height=self.donate_img_height,
            x=donate_qr_image_x,
            y=donate_qr_image_y,
        )
        # donate text
        donate_text_x = self.l_r_margin
        donate_text_y = (
            self.row_height
            + self.row_height
            - (self.donate_img_height / 2)
            + self.donate_y_offset
        )
        donate_text_width: float = self.column_width * self.columns_count
        self.add_horizontal_text_to_pos_C_width(
            pdf=pdf,
            text=self.donate_text,
            x=donate_text_x,
            y=donate_text_y,
            text_size=self.text_size_4,
            text_witdth=donate_text_width,
        )

        # donate address
        donate_address_x = self.l_r_margin
        donate_address_y = (
            self.row_height
            + self.row_height
            - (self.donate_img_height / 2)
            + self.donate_y_offset
            + self.donate_img_height
            + 10
        )
        donate_text_width: float = self.column_width * self.columns_count
        self.add_horizontal_text_to_pos_C_width(
            pdf=pdf,
            text=self.donate_Doge_address,
            x=donate_address_x,
            y=donate_address_y,
            text_size=self.text_size_4,
            text_witdth=donate_text_width,
        )
        # self.donate_img_width: int = 80
        # self.donate_img_height: int = self.donate_img_width

        return pdf

    def create_pdf(
        self,
    ) -> FPDF:
        orientations: list[str] = [
            "landscape",
            "portrait",
        ]

        pdf_format: str = "A4"
        margin: float = 0
        pdf: FPDF = FPDF()

        pdf.add_page(
            orientation=orientations[1],
            format=pdf_format,
        )
        pdf.set_margin(margin=margin)
        # pdf.set_margins(
        #     left=margin,
        #     top=margin,
        #     right=0,
        # )
        return pdf

    def get_test_images_folder_path(
        self,
    ) -> str:
        # current_directory: str = os.getcwd()
        current_directory: str = os.path.dirname(__file__)
        images_folder_name: str = "test_images"
        images_folder_path: str = os.path.join(
            current_directory,
            images_folder_name,
        )
        return images_folder_path


def test_draw_wallet() -> str:
    # init class
    l_r_margin: float = 5
    top_margin: float = 5
    draw_wallet: Draw_Wallet = Draw_Wallet(
        l_r_margin=l_r_margin,
        top_margin=top_margin,
    )
    test_images_folder_path: str = draw_wallet.get_test_images_folder_path()

    priv_key: str = "0e7f6b43ff9c134e0a295be2a0ccb6a6d2d32ec166b4dbcb4dda9e5a96c6eb71"
    priv_qr_img_name: str = "private_doge.png"
    priv_qr_img_path: str = os.path.join(
        test_images_folder_path,
        priv_qr_img_name,
    )

    pub_address: str = "D5FgLCifuP7ort5euG32K24YS23fT14x49"
    pub_qr_img_name: str = "public_doge.png"
    pub_qr_img_path: str = os.path.join(
        test_images_folder_path,
        pub_qr_img_name,
    )
    # cerate a empty pdf
    pdf: FPDF = draw_wallet.create_pdf()
    # draw wallet on the pdf
    draw_wallet.draw_wallet(
        pdf=pdf,
        priv_key=priv_key,
        priv_qr_img_path=priv_qr_img_path,
        pub_address=pub_address,
        pub_qr_img_path=pub_qr_img_path,
    )

    # saving the pdf
    pdf_file_name: str = "Draw_Wallet_test.pdf"
    file_path: str = draw_wallet.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )
    return file_path


def test_draw_wallet_2() -> bytes:

    # init class
    l_r_margin: float = 5
    top_margin: float = 5
    draw_wallet: Draw_Wallet = Draw_Wallet(
        l_r_margin=l_r_margin,
        top_margin=top_margin,
    )
    test_images_folder_path: str = draw_wallet.get_test_images_folder_path()

    priv_key: str = "0e7f6b43ff9c134e0a295be2a0ccb6a6d2d32ec166b4dbcb4dda9e5a96c6eb71"
    priv_qr_img_name: str = "private_doge.png"
    priv_qr_img_path: str = os.path.join(
        test_images_folder_path,
        priv_qr_img_name,
    )

    pub_address: str = "D5FgLCifuP7ort5euG32K24YS23fT14x49"
    pub_qr_img_name: str = "public_doge.png"
    pub_qr_img_path: str = os.path.join(
        test_images_folder_path,
        pub_qr_img_name,
    )
    # pdf_as_bytes: bytes = bytes()
    # draw wallet on the pdf
    pdf_data: bytes = draw_wallet.draw_wallet_return_bytes(
        # pdf=pdf,
        priv_key=priv_key,
        priv_qr_img_path=priv_qr_img_path,
        pub_address=pub_address,
        pub_qr_img_path=pub_qr_img_path,
    )

    # # saving the pdf
    # pdf_file_name: str = "Draw_Wallet_test.pdf"
    # file_path: str = draw_wallet.save_to_output_folder(
    #     pdf=pdf,
    #     pdf_file_name=pdf_file_name,
    # )
    return pdf_data


# Example usage:
if __name__ == "__main__":

    # file_path: str = test_draw_wallet()
    # from .PDFPrinter import PDFPrinter
    # printer: PDFPrinter = PDFPrinter()
    # printer.print_pdf(pdf_path=file_path)

    pdf_data: bytes = test_draw_wallet_2()
    from .ImagePrinter import ImagePrinter

    image_printer: ImagePrinter = ImagePrinter()
    image_printer.print_pdf_from_memory(pdf_data=pdf_data)
    print(" ")
    print("test completed..")
