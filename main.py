import shutil
from compare import compare
from gulagcleaner.extract import clean_pdf

return_msg = clean_pdf("file.pdf")
# Define the paths to the two folders
og_cleaned_folder = "og_cleaned"
new_cleaned_folder = "new_cleaned"



#for each pdf in new dirty folder, run clean_pdf, the pdfs are called 1.pdf, 2.pdf 3.pdf ... 10.pdf
for i in range(1, 11):
    clean_pdf("new_dirty/"f"{i}.pdf")
    #rename the file 1_clean to 1.pdf

for i in range(1, 11):
    #move each file from new_dirty to new_cleaned
    shutil.move("new_dirty/"f"{i}_clean.pdf", "new_cleaned/"f"{i}.pdf")

# Run the compare.py script
estado = compare(og_cleaned_folder, new_cleaned_folder)

print(estado)

