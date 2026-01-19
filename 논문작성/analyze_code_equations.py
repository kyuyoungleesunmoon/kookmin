from docx import Document
import re

file_path = r"C:\국민대프로젝트\논문작성\IEEE_DPF_Paper_Final_v5.docx"
doc = Document(file_path)

code_patterns = [
    r'^\s*(def |class |import |from |if |for |while |try:|except:|return |print\()',
    r'^\s*#.*',  # Comments
    r'^\s*\w+\s*=\s*\{',  # Dict assignment
    r'^\s*\w+\s*=\s*\[',  # List assignment
    r"^\s*'[\w_]+'\s*:",  # Dict keys
    r'^\s*plt\.',  # matplotlib
    r'^\s*np\.',  # numpy
    r'^\s*torch\.',  # pytorch
    r'^\s*model\.',  # model calls
    r'^\s*├─|└─',  # Tree structure
]

equation_patterns = [
    r'\$\$',  # LaTeX block
    r'\\\[',  # LaTeX display
    r'\\tag\{',  # Equation tag
    r'\\begin\{',  # LaTeX environments
    r'\\frac\{',  # Fractions
    r'\\sum',  # Summations
    r'\\mathcal\{',  # Math calligraphy
]

code_paragraphs = []
equation_paragraphs = []

for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if not text:
        continue
    
    # Check for code patterns
    for pattern in code_patterns:
        if re.search(pattern, text):
            code_paragraphs.append((i, text[:60]))
            break
            
    # Check for equation patterns
    for pattern in equation_patterns:
        if re.search(pattern, text):
            equation_paragraphs.append((i, text[:60]))
            break

print(f"=== Code Blocks Found: {len(code_paragraphs)} ===")
for idx, (line, text) in enumerate(code_paragraphs[:20]):
    print(f"  [{line}] {text}...")

print(f"\n=== Equation Blocks Found: {len(equation_paragraphs)} ===")
for idx, (line, text) in enumerate(equation_paragraphs[:20]):
    print(f"  [{line}] {text}...")
