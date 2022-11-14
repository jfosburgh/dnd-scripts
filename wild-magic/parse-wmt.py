from PyPDF2 import PdfFileReader
import numpy


def extract_information(pdf_path):
    wmt = {}
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        for i in range(4, len(pdf.pages)):
            if i == 4:
                text = pdf.pages[i].extract_text().split("result.")[1][6:]
            else:
                text = pdf.pages[i].extract_text()[6:]
            # print(text)
            lines = text.split("\n")
            # print(lines)
            for line in lines:
                # print(line)
                args = line.split(" ")
                number = args[0]
                effect = " ".join(args[1:]).replace('\x92', "'")
                wmt[number] = effect

    return wmt


if __name__ == "__main__":
    pdf_path = "./NLRMEv2.pdf"
    wmt = extract_information(pdf_path)
    print(wmt["0001"])
    print(len(wmt))
    with open("./wmt.txt", 'w') as txt:
        for key in wmt.keys():
            txt.write("{} {}\n".format(key, wmt[key]))
