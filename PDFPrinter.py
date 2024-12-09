import os
import win32api
import win32print


class PDFPrinter:
    """A class to print PDF files using the default Windows printer.
    A pdf reader like foxit reader must be installed on the windows
    system and be set as the standard for fdf opening."""

    def __init__(self):
        """Initializes the PDFPrinter class."""
        pass

    def print_pdf(self, pdf_path: str):
        """Prints a PDF file using the default Windows printer.

        Args:
            pdf_path (str): The path to the PDF file.
        """
        # Get the default printer
        printer_name = win32print.GetDefaultPrinter()
        # Use win32api to print the PDF
        try:
            # win32api.ShellExecute(0, "print", pdf_path, None, ".", 0)
            win32api.ShellExecute(0, "print", pdf_path, f'/d:"{printer_name}"', ".", 0)
            print(" ")
            print(f"printing: {pdf_path} on {printer_name} ")
        except Exception as e:
            print(f"error {e}  ")
            print(
                f"the error could be caused of not having a pdf reader installed on windows."
            )
            print(
                f"i had that issue too after some googeling i realized my only pdf reader i have,"
            )
            print(f"is the inbuild one in firefox.")
            print(
                "so i installed Foxit PDF Reader and (important open the foxit reader and make it to your standard for pdf.) "
            )
            print("then it worked for me.")
        #


def test_print():
    current_directory = os.getcwd()

    pdf_file_name: str = "test_image_fit_in_rect_with_c_align_center_and_print.pdf"
    pdf_path: str = os.path.join(current_directory, pdf_file_name)
    printer = PDFPrinter()
    printer.print_pdf(pdf_path=pdf_path)


# Example usage:
if __name__ == "__main__":
    test_print()
