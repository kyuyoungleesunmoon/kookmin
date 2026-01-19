from docx import Document

file_path = r"C:\국민대프로젝트\논문작성\IEEE_DPF_Paper_Submission_Ready.docx"
doc = Document(file_path)

all_text = [p.text for p in doc.paragraphs if len(p.text) > 20]
seen = set()
duplicates = []

for text in all_text:
    if text in seen:
        duplicates.append(text)
    seen.add(text)

print(f"Total paragraphs with text > 20 chars: {len(all_text)}")
print(f"Unique paragraphs: {len(seen)}")
print(f"Duplicate count: {len(duplicates)}")

if len(duplicates) > 0:
    print("\nFirst 5 duplicates:")
    for d in duplicates[:5]:
        print(f"DUPE: {d[:50]}...")
