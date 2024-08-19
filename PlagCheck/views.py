from django.shortcuts import render
from PlagCheck.algorithm import main
from docx import Document
from PyPDF2 import PdfReader
import io

# home
def home(request):
    return render(request, 'pc/index.html')

# web search(Text)
def test(request):
    print("Welcome and Testing ...")
    print(request.POST['q'])

    if request.POST['q']:
        percent, link = main.findSimilarity(request.POST['q'])
        percent = round(percent, 2)
    print("Percent PLAGIARIZED = ", percent, link)
    return render(request, 'pc/index.html', {'link': link, 'percent': percent})

# web search file(.txt, .docx, .pdf)
def filetest(request):
    value = ''
    print(request.FILES['docfile'])
    if str(request.FILES['docfile']).endswith(".txt"):
        value = str(request.FILES['docfile'].read())
    elif str(request.FILES['docfile']).endswith(".docx"):
        document = Document(request.FILES['docfile'])
        for para in document.paragraphs:
            value += para.text
    elif str(request.FILES['docfile']).endswith(".pdf"):
        # Read the PDF file content
        pdf_file = request.FILES['docfile'].read()
        pdfReader = PdfReader(io.BytesIO(pdf_file))

        # Extract text from PDF
        text = ""
        for page_num in range(len(pdfReader.pages)):
            page = pdfReader.pages[page_num]
            text += page.extract_text()

        value = text

    percent, link = main.findSimilarity(value)
    print("Percent PLAGIARIZED = ", percent, link)
    return render(request, 'pc/index.html', {'link': link, 'percent': percent})


