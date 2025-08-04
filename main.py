import pdfplumber
import pandas as pd

def pdf_to_excel(pdf_path, output_path="output.xlsx"):
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                data.extend(table)

    if data:
        df = pd.DataFrame(data[1:], columns=data[0])
        df.to_excel(output_path, index=False)
        print(f"[✓] Excel saved to: {output_path}")
    else:
        print("[!] No table found in the PDF.")

if __name__ == "__main__":
    pdf_path = input("Enter path to your PDF file: ")
    output_path = input("Enter desired output Excel filename (or press enter for 'output.xlsx'): ")
    if not output_path.strip():
        output_path = "output.xlsx"
    pdf_to_excel(pdf_path, output_path)
