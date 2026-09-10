from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs=[]

try:
    n=int(input("how many pdfs you want to merge ? : "))

    for i in range(n):
        name=input(f"enter the name of PDF {i+1} : ")
        if  not name.endswith(".pdf"):
            print("Only PDF files are allowed!")
            exit()

        pdfs.append(name)

    for pdf in pdfs:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print(f"File not found:{pdf}")
            exit()

    output = input("Enter output file name (with .pdf): ")


    merger.write("output")
    merger.close()

    print(f"✅ PDFs merged successfully into '{output}'")

except ValueError:
    print("❌ Please enter a valid number!")