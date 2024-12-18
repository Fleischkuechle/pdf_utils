import os
from fpdf import FPDF
import fpdf
import fpdf.output
from PIL import Image as pil_img


try:
    from Grid_Generator import Grid_Generator
    from Add_Image import Add_Image
except:
    from .Grid_Generator import Grid_Generator
    from .Add_Image import Add_Image


class Draw_Helper:
    # https://py-pdf.github.io/fpdf2/
    # A4 Metric: 210 x 297 mm
    def __init__(
        self,
        l_r_margin: float = 5,
        top_margin: float = 5,
    ):
        self.l_r_margin: float = l_r_margin
        self.top_margin: float = top_margin

        self.grid_generator: Grid_Generator = Grid_Generator(
            l_r_margin=self.l_r_margin,
            top_margin=self.top_margin,
        )
        self.image_adder: Add_Image = Add_Image()

    def draw_grid(
        self,
        pdf: FPDF,
        line_distance: int,
        height: int,
        width: int,
    ):
        self.grid_generator.draw_grid_03(
            pdf=pdf,
            line_distance=line_distance,
            height=height,
            width=width,
        )

    def add_image_to_pos_from_pil_img(
        self,
        pdf: FPDF,
        pil_img: pil_img.Image,
        width: int = 300,
        height: int = 300,
        x: int = 0,
        y: int = 0,
    ):
        self.image_adder.add_image_to_pos_from_pil_img(
            pdf=pdf,
            pil_img=pil_img,
            width=width,
            height=height,
            x=x,
            y=y,
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
        self.image_adder.add_image_to_pos(
            pdf=pdf,
            img_path=img_path,
            width=width,
            height=height,
            x=x,
            y=y,
        )

    def add_image(
        self,
        pdf: FPDF,
        img_path: str = "",
        width: int = 300,
        height: int = 300,
        y: int = -1,
        orientation: str = "center",
    ):
        self.image_adder.add_image(
            pdf=pdf,
            img_path=img_path,
            width=width,
            height=height,
            y=y,
            orientation=orientation,
        )

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
        width: float = 100,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        with pdf.rotation(
            angle=angle,
        ):
            pdf.cell(
                w=width,
                text=text,
                fill=True,
                align=fpdf.enums.Align.C,
            )

    def add_vertical_text_to_pos_3(
        self,
        pdf: FPDF,
        text: str = "please enter text.",
        angle: float = 90,
        text_size: int = 50,
        width: float = 100,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        with pdf.rotation(
            angle=angle,
        ):
            pdf.multi_cell(
                w=width,
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
        width: float = 100,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        pdf.set_xy(
            x=x,
            y=y,
        )
        pdf.multi_cell(
            text=text,
            w=width,
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
        width: float = 100,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        pdf.set_xy(
            x=x,
            y=y,
        )
        pdf.multi_cell(
            text=text,
            w=width,
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
        width: float = 100,
    ):
        pdf.set_auto_page_break(False)
        pdf.set_font("Helvetica", size=text_size)
        pdf.set_xy(
            x=x,
            y=y,
        )
        pdf.multi_cell(
            text=text,
            w=width,
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
    draw_wallet: Draw_Helper = Draw_Helper(
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


def test():
    print("Todo")


# Example usage:
if __name__ == "__main__":
    test()
