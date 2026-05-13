

from docx import Document
import pandas as pd
import re
# add doc file location
doc = Document("") 

chapters = []
sections = []
hadiths = []

chapter_id = 1
section_id = 1
hadith_id = 1

current_hadith = ""

for para in doc.paragraphs:
    text = para.text.strip()

    if not text:
        continue

    if text.startswith(""):
        name = text.replace(":", "").strip()
        chapters.append({
            "id": chapter_id,
            "name": name
        })
        chapter_id += 1
        continue

  
    is_bold = any(run.bold for run in para.runs if run.text.strip())

    if is_bold and not re.match(r"^\[", text):
        sections.append({
            "id": section_id,
            "name": text
        })
        section_id += 1
        continue

   
    if re.match(r"^\[[০-৯0-9]+\]", text):

   
        if current_hadith:
            clean_text = re.sub(r"^\[[০-৯0-9]+\]\s*", "", current_hadith.strip())
            clean_text = re.sub(r"\s+", " ", clean_text)

            hadiths.append({
                "id": hadith_id,
                "name": clean_text
            })
            hadith_id += 1

        current_hadith = text

    else:
        current_hadith += " " + text


if current_hadith:
    clean_text = re.sub(r"^\[[০-৯0-9]+\]\s*", "", current_hadith.strip())
    clean_text = re.sub(r"\s+", " ", clean_text)

    hadiths.append({
        "id": hadith_id,
        "name": clean_text
    })

df_chapter = pd.DataFrame(chapters)
df_section = pd.DataFrame(sections)
df_hadith = pd.DataFrame(hadiths)


with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    df_chapter.to_excel(writer, sheet_name="chapter", index=False)
    df_section.to_excel(writer, sheet_name="section", index=False)
    df_hadith.to_excel(writer, sheet_name="hadith", index=False)


print("Excel file created successfully!")
