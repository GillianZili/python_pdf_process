from PyPDF2 import PdfReader, PdfWriter
import os

path1 = input("please input path_origin: ")
path2 = input("please input path_insert: ")
pos = int(input("please input insert pos: "))

lst1 = os.listdir(path1)

file_set = set(os.listdir(path2))
for file in lst1:
    if file not in file_set:
        continue
    input1 = open(path1 + "\\" + file, "rb")
    input2 = open(path2 + "\\" + file, "rb")
    reader = PdfReader(path1 + "\\" + file)
    page = len(reader.pages)
    merger = PdfWriter()

    merger.append(fileobj=reader, pages=(0, pos - 1))
    merger.append(input2)
    merger.append(fileobj=reader, pages=(pos, page))
    output = open("./document-output" + file, "wb")
    merger.write(output)
    merger.close()
    output.close()
