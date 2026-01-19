from docx import Document

template_path = r"C:\국민대프로젝트\IEEE_TII_Template\TII_Articles_Word_template_2025.docx"
doc = Document(template_path)

print("Available Styles:")
styles = [s.name for s in doc.styles if s.type.name == 'PARAGRAPH']
for s in sorted(styles):
    print(f"- {s}")
