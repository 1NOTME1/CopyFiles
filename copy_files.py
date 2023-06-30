#KOPIOWANIE PLIKOW DO INNEGO FOLDERU Z PLIKU .TXT
import os
import shutil

input_file_path = r"C:\Users\USER_NAME\Desktop\kopiowanie_pdf\pdf_do_kopiowania.txt"

output_folder_path = r"C:\Users\USER_NAME\Desktop\kopiowanie_pdf\pdf"

with open(input_file_path, "r", encoding='utf-8') as file:
    pdf_paths = file.readlines()

pdf_paths = [path.strip() for path in pdf_paths]

for pdf_path in pdf_paths:
    pdf_name = os.path.basename(pdf_path)
    output_path = os.path.join(output_folder_path, pdf_name)
    shutil.copy(pdf_path, output_path)

print("Skopiowano pliki PDF do folderu:", output_folder_path)
