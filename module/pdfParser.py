from pdftables.pdf_document import PDFDocument
from pdftables.pdftables import page_to_tables
from pdftables.display import to_string

# import pdftables

filepath = '/Users/Konan/Downloads/1203390399.PDF'
fileobj = open(filepath,'rb')
doc = PDFDocument.from_path(fileobj)
page = doc.get_page(3)
tables = page_to_tables(page)
for page_number, page in enumerate(doc.get_pages()):
  tables = page_to_tables(page)
for table in tables:
  print to_string(table.data)
