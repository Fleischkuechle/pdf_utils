import os
from fpdf import FPDF


class PDF(FPDF):
    # https://py-pdf.github.io/fpdf2/
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

    def header(self):
        # Logo
        self.image(
            name=r"D:\11\02\13\FPDF_tests\test_images\Nerd123Logo.png",
            x=10,
            y=8,
            w=33,
        )
        # Arial bold 15
        self.set_font(
            family="Arial",
            style="B",
            size=15,
        )
        # Move to the right
        self.cell(w=80)
        # Title
        self.cell(
            w=30,
            h=10,
            text="Title",
            border=1,
            ln=0,
            align="C",
        )
        # Line break
        self.ln(h=20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(y=-15)
        # Arial italic 8
        self.set_font(
            family="Arial",
            style="I",
            size=8,
        )
        # Page number
        self.cell(0, 10, "Page " + str(self.page_no()) + "/{nb}", 0, 0, "C")


# Example usage:
if __name__ == "__main__":
    # Instantiation of inherited class
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font(family="Times", style="", size=12)
    for i in range(1, 41):
        pdf.cell(
            w=0,
            h=10,
            text="Printing line number " + str(i),
            border=0,
            ln=1,
        )
    # pdf.output(
    #     name="Header_footer_page_break_and_image_example.pdf",
    #     dest="F",
    # )
    pdf_file_name: str = "Header_footer_page_break_and_image_example.pdf"
    pdf.save_to_output_folder(
        pdf=pdf,
        pdf_file_name=pdf_file_name,
    )
    # current_directory = os.getcwd()
    # pdf_file_name: str = "Header_footer_page_break_and_image_example.pdf"
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
