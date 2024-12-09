# You got it! Here's the description with code examples:

# Python itself doesn't have built-in functionality to directly interact with physical printers.
#  It's a high-level programming language designed for general-purpose tasks,
# not for low-level hardware control.

# To print to a printer, Python needs to rely on the operating
# system's (OS) API (Application Programming Interface). Here's why:

# * **Hardware Abstraction:** Printers are complex hardware devices with
# varying functionalities and protocols.
# The OS acts as a layer of abstraction,
# handling the communication between your program and the printer.
# * **Driver Compatibility:** Printers require specific drivers that translate your print requests into commands the printer understands. The OS manages these drivers and provides a consistent interface for applications to use.
# * **Security:** Directly accessing hardware can pose security risks.
# The OS provides a controlled environment for applications
# to interact with hardware, ensuring safety
# and preventing malicious actions.

# Therefore, Python libraries like `win32print` (for Windows)
# or `cups` (for macOS and Linux) are used to access the OS's printing functionality,
# allowing you to print documents and images from your Python programs.

# Here are some code examples:

# **Windows (using `win32print`)**

# ```python
# import win32print

# # Get the default printer name
# default_printer = win32print.GetDefaultPrinter()

# # Print a text file
# with open("my_document.txt", "r") as f:
#     data = f.read()
#     win32print.WritePrinter(default_printer, data.encode())
# ```

# **macOS and Linux (using `cups`)**

# ```python
# import cups

# # Connect to the CUPS server
# conn = cups.Connection()

# # Get the list of printers
# printers = conn.getPrinters()

# # Print a PDF file
# conn.printFile("my_printer", "my_document.pdf", "My Document", {})
# ```

# These examples demonstrate how Python libraries
# interact with the OS to achieve printing.
# Remember that you'll need to install
# the necessary libraries
# (e.g., `pywin32` for Windows, `python-cups` for macOS and Linux)
# before running these scripts.

# Android Printing:

# Print Manager: Android has a built-in Print Manager that handles communication with printers and print services.
# Print Services: These are applications (like Google Cloud Print, Samsung Print Service, etc.) that bridge the gap between Android apps and printers.
# Print Documents: Android apps create printable documents in a standardized format (usually PDF or a similar representation).
# Printing Process:
# The app sends the print document to the Print Manager.
# The Print Manager chooses a suitable Print Service based on the printer and document type.
# The Print Service converts the document into a format the printer understands and sends it to the printer.
# Python on Android:

# Python can interact with Android's printing system through libraries like Pyjnius.
# You can use Python to create printable documents (e.g., PDF files) and then use Android's Print Manager to send them to a printer.
# You'll need to use a third-party printing app or service to handle the actual printing process.
# Example (Conceptual):
# Using Pyjnius to interact with Android's Print Manager
# from jnius import autoclass

# # Create a PDF document (using a Python library like ReportLab)
# # ...

# from jnius import autoclass

# # Create a PDF document (using a Python library like ReportLab)
# from reportlab.pdfgen import canvas

# # Create a new PDF document
# pdf = canvas.Canvas("my_document.pdf")

# # Add content to the PDF document
# pdf.drawString(100, 700, "Hello, world!")

# # Save the PDF document
# pdf.save()

# # Get the Print Manager
# PrintManager = autoclass('android.print.PrintManager')
# print_manager = PrintManager(context)

# # Create a PrintDocumentAdapter
# PrintDocumentAdapter = autoclass('android.print.PrintDocumentAdapter')
# document_adapter = PrintDocumentAdapter()

# # Send the document to the Print Manager
# print_manager.print("My Document", document_adapter)
# Explanation:

# Import necessary libraries:

# jnius for interacting with Java classes.
# reportlab for creating PDF documents.
# Create a PDF document:

# Use reportlab to create a canvas object.
# Add content to the canvas using methods like drawString.
# Save the canvas as a PDF file.
# Get the Print Manager:

# Use autoclass to get the android.print.PrintManager class.
# Create a PrintManager object using the context (your Android application context).
# Create a PrintDocumentAdapter:

# Use autoclass to get the android.print.PrintDocumentAdapter class.
# Create a PrintDocumentAdapter object. This object will handle the printing process.
# Send the document to the Print Manager:

# Use print_manager.print() to send the document to the Print Manager.
# Pass the document name and the PrintDocumentAdapter object as arguments.
# Important Notes:

# This code assumes you have the necessary libraries installed.
# You need to implement the PrintDocumentAdapter class to handle the actual printing process, including layout, page size, and other printing options.
# The context variable should be your Android application context.
# This code is a basic example and may need to be adapted depending on your specific requirements.
# This code provides a starting point for printing a PDF document from your Android app using Python. You can customize the code to suit your needs by adding more content to the PDF, configuring the PrintDocumentAdapter, and handling printing errors.

from sys import flags
import win32print  # ignore
import win32ui
from PIL import Image as PIL_img
from PIL import ImageWin
import inspect


class ImagePrinter:
    """
    A class to print images to a specific printer using the win32print and win32ui libraries.

    Example usage:
    ```python
    printer = ImagePrinter("C:/Users/YourName/Pictures/my_image.jpg")
    printer.print_image()
    ```
    This will print the image "my_image.jpg" to the default printer.
    """

    def __init__(self, file_path: str = "") -> None:
        """
        Initializes the ImagePrinter object.

        Args:
            file_path: The full path to the image file to be printed. Defaults to "new.jpg".
        """
        self.file_path = file_path
        # taken form here https://learn.microsoft.com/en-us/windows/win32/printdocs/enumprinters
        self.printer_enums: list[str] = [
            "PRINTER_ENUM_LOCAL",
            "PRINTER_ENUM_NAME",
            "PRINTER_ENUM_SHARED",
            "PRINTER_ENUM_CONNECTIONS",
            "PRINTER_ENUM_NETWORK",
            "PRINTER_ENUM_REMOTE",
            "PRINTER_ENUM_CATEGORY_3D",
            "PRINTER_ENUM_CATEGORY_ALL",
        ]
        self.printer_name = win32print.GetDefaultPrinter()
        # Check if the file path is a valid image file
        if file_path == "":
            raise ValueError("Filepath is empty: " + self.file_path)
        if not self.is_image_file(self.file_path):
            raise ValueError("Invalid image file path: " + self.file_path)

    def print_image(self) -> None:
        """
        Prints the image to the default printer.
        """
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111

        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(self.printer_name)
        printer_size = hDC.GetDeviceCaps(PHYSICALWIDTH), hDC.GetDeviceCaps(
            PHYSICALHEIGHT
        )

        opend_image: PIL_img.Image = PIL_img.open(fp=self.file_path)
        if opend_image.size[0] < opend_image.size[1]:
            opend_image = opend_image.rotate(90)

        hDC.StartDoc(self.file_path)
        hDC.StartPage()

        dib = ImageWin.Dib(image=opend_image)
        dib.draw(hDC.GetHandleOutput(), (0, 0, printer_size[0], printer_size[1]))

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()

    def is_image_file(self, file_path: str) -> bool:
        """
        Checks if the given file path is a valid image file.

        Args:
            file_path: The full path to the file.

        Returns:
            True if the file path is a valid image file, False otherwise.
        """
        allowed_extensions = [
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".gif",
            ".pdf",
        ]  # Add more extensions as needed
        return file_path.lower().endswith(tuple(allowed_extensions))

    def print_printers(
        self,
    ):
        printers = win32print.EnumPrinters(2)  # 2 represents PRINTER_ENUM_LOCAL

        # Print the names of the printers
        print("Available printers:")
        for printer in printers:
            # Accessing elements of the printer tuple
            name = printer[2]  # Printer name
            server = printer[1]  # Server name
            # ... other elements can be accessed here if needed ...

            print(f" - {name} (on server: {server})")

    def print_printers_2(self, enum=-1):
        """Prints all values returned by win32print.EnumPrinters() for the given enum."""
        if enum is None or enum == -1:
            print("enum is None or -1, not printing anything.")
            return

        printers: tuple = win32print.EnumPrinters(enum)
        if len(printers) == 0:
            print(
                f"  ---nothing to print in: {enum} (maybe no acees rights to that information.)"
            )
            return
        # print(f"enum: {enum}")
        for idx, printer in enumerate(printers):
            print(f" - Printer:{idx}")
            for i, value in enumerate(printer):
                print(f"    - Element {i}: {value}")

    def print_printer_enums_old(
        self,
    ):
        """Prints all available printer enumeration flags."""
        print("Available Printer Enumeration Flags:")
        for name, value in inspect.getmembers(
            win32print,
        ):
            if name.startswith("PRINTER_ENUM_"):
                print(f"- {name}: {value}")

    def print_printer_enums(
        self,
    ):
        """Prints all available printer enumeration flags. that are in the self.printer_enums"""
        print("Available Printer Enumeration Flags:")
        for name, value in inspect.getmembers(win32print):
            if name in self.printer_enums:
                print(f" - {name}: {value}")
                self.print_printers_2(enum=value)
            else:
                pass
                # print(f"not a printer info: {name} index: {value}")

    def print_file(self, filepath: str = ""):
        # Print a text file
        # # Get the default printer name
        if filepath == "":
            filepath = self.file_path
        if filepath != "":
            self.file_path = filepath
        default_printer: str = win32print.GetDefaultPrinter()
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111

        # hDC = win32ui.CreateDC()
        # hDC.CreatePrinterDC(self.printer_name)
        # printer_size = hDC.GetDeviceCaps(PHYSICALWIDTH), hDC.GetDeviceCaps(
        #     PHYSICALHEIGHT
        # )
        with open(filepath, "r") as f:
            data = f.read()
            win32print.WritePrinter(default_printer, data)
        # hDC.StartDoc(filepath)
        # hDC.StartPage()

        # dib = ImageWin.Dib(image=filepath)
        # dib.draw(hDC.GetHandleOutput(), (0, 0, printer_size[0], printer_size[1]))

        # hDC.EndPage()
        # hDC.EndDoc()
        # hDC.DeleteDC()


if __name__ == "__main__":
    # Example usage:
    image_filepath: str = r"D:\11\02\13\FPDF_tests\test_images\teset.png"
    filepath: str = (
        r"D:\11\02\13\FPDF_tests\test_image_fit_in_rect_with_c_align_center_and_print.pdf"
    )

    # printer = ImagePrinter(file_path=image_filepath)
    # printer.print_image()

    printer = ImagePrinter(file_path=filepath)
    printer.print_file(filepath=filepath)

    # printer.print_printers()
    # printer.print_printer_enums()
