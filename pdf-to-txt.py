import PyPDF2
import logging

logging.basicConfig(filename='pdf-to-txt.log',
                    encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PdfToTxt:
    def __init__(self, pdf_file_path, txt_file_path):
        self.pfp = pdf_file_path
        self.tfp = txt_file_path
        self.__text = ''

    def __read_pdf(self):
        self.__pdfreader = PyPDF2.PdfReader(self.pfp)
        self.__pages = len(self.__pdfreader.pages)

        for i in range(self.__pages):
            self.__page = self.__pdfreader.pages[i]
            self.__text += self.__page.extract_text()

    def writeToTxt(self):
        if self.tfp.lower().endswith('.txt'):
            self.__read_pdf()
            with open(self.tfp, 'w') as self.__fp:
                self.__fp.writelines(self.__text)
        else:
            logger.error("file extension of the out file isn't 'txt'")


if __name__ == '__main__':
    convert_file = PdfToTxt("/Users/gauthamkolluru/code/python_training.pdf",
                            "/Users/gauthamkolluru/code/python_training.docx")
    convert_file.writeToTxt()
