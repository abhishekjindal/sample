# -*- coding: utf-8 -*-
import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


"""
Converts input PDF to text string
:param fname: name of file
:param pages: List[Integer] of pages to process
:return: String
"""
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


"""
Searches text string for words
:param search_strings: List[String]
:return: List[Boolean]
"""

# search_strings = "This is a sample PDF ﬁle.\nThis is page 1. On this page, the patient’s DOB, and allergies" +\
# "should be listed.\n Their name is Billy Bob Jones.\n The patient is a 35 year old man of Australian nationality."+\
# "He was born in Brisbane on 2/2/1982.\n Filler text. More ﬁller text.\nThis is a sample PDF ﬁle.\n"+\
# "This is page 2. On this page, the patient’s medications are listed."+\
# "Their name is Billy Bob Jones."+\
# "Mr. Jones takes 2 tylenols daily. He does this because he suﬀers from a severe cough. Yesterday he took 4, which was a lot."+\
# "This is a sample PDF ﬁle."+\
# "This is page 3. On this page, the patient’s vitals are listed."+\
# "Their name is Billy Bob Jones."+\
# "Height"+\
# "Weight"+
# "BP"+
# "Temperature"+
# "Respiratory rate"+
# "5'8\""+
# "176 lb"+
# "130/78 mmHg"+
# "98.6 F"+
# "12 bpm"
search_strings = """This is a sample PDF ﬁle.

This is page 1. On this page, the patient’s DOB, and allergies
should be listed.

Their name is Billy Bob Jones.

The patient is a 35 year old man of Australian nationality.

He was born in Brisbane on 2/2/1982.

Filler text. More ﬁller text.




This is a sample PDF ﬁle.

This is page 2. On this page, the patient’s medications are listed.

Their name is Billy Bob Jones.

Mr. Jones takes 2 tylenols daily. He does this because he suﬀers
from a severe cough. Yesterday he took 4, which was a lot.



This is a sample PDF ﬁle.

This is page 3. On this page, the patient’s vitals are listed.

Their name is Billy Bob Jones.


Height
Weight
BP
Temperature
Respiratory rate

5’8”
176 lb
130/78 mmHg
98.6 F
12 bpm"""


# print search_strings
def search(search_strings):
    array = ['dob', 'medications', 'vitals']
    result = list()
    string = str.lower(search_strings)
    for j in xrange(len(array)):
        for i in xrange(len(string)):
            tofind = array[j]
            if(string[i]==tofind[0]):
                check = string[i:i+len(tofind)]
                if(check == tofind):
                    result.append(True)
                    break

    # Finish this function
    return result

print search(search_strings)
# pdf_text = convert('exercise/sample_medical_record.pdf')