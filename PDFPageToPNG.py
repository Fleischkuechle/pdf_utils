import os
import fitz  # PyMuPDF


class PDFPageToPNG:
    """A class to extract and save individual pages from a PDF as PNG images."""

    def save_page_as_png(
        self,
        pdf_path: str,
        page_number: int,
        print_result: bool = False,
    ):
        """Saves a specific page of the PDF as a PNG image.

        Args:
            pdf_path (str): Path to the PDF file.
            page_number (int): The page number to extract (starting from 1).
        """

        doc: fitz.Document = fitz.open(pdf_path)  # Open the PDF document
        page: fitz.Page = doc[page_number - 1]  # Adjust for 0-based indexing

        # Create a Pixmap object from the page
        pix: fitz.Pixmap = page.get_pixmap(
            matrix=fitz.Matrix(1.0, 1.0)
        )  # Default matrix for 1:1 scaling
        # # Extracting the filename and extension
        # filename, extension = os.path.splitext(os.path.basename(pdf_path))

        # Generate output path based on PDF file name and page number
        output_path = f"{pdf_path[:-4]}_page_{page_number}.png"

        # Save the Pixmap as a PNG image
        pix.save(output_path)

        doc.close()  # Close the PDF document
        if print_result:
            pdf_name: str = os.path.basename(pdf_path)
            print("-" * 40)
            # print(f"completed ...")
            print(f"saved ({pdf_name}) (page {page_number}) as an image to here:")
            print(f"{output_path}")
            print("-" * 40)


if __name__ == "__main__":
    # Example usage
    my_folder_path: str = os.path.dirname(__file__)
    pdf_file_name: str = "test_pdf.pdf"
    pdf_folder_name: str = "test_images"
    pdf_path: str = os.path.join(
        my_folder_path,
        pdf_folder_name,
        pdf_file_name,
    )
    # pdf_path: str = "your_pdf_file.pdf"
    page_number: int = 1
    print_result: bool = True

    extractor: PDFPageToPNG = PDFPageToPNG()
    extractor.save_page_as_png(
        pdf_path=pdf_path,
        page_number=page_number,
        print_result=print_result,
    )
