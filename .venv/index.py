import PyPDF2
from DBS import DBS
# from OCBC import *

reader = PyPDF2.PdfReader('statements/2.pdf')
raw_file_content = reader.pages[0].extract_text()
if "OCBC Bank" in raw_file_content:
    # OCBC()
    pass
elif "DBS/POSB" in raw_file_content:
    DBS(raw_file_content)
else:
    print("Invalid bank_statement")