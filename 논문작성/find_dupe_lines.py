file_path = r"C:\국민대프로젝트\converted_md\이규영_국민대_DPF_논문.md"
target = "제출 목표"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0
for i, line in enumerate(lines):
    if target in line:
        print(f"Found at line {i+1}: {line.strip()}")
        count += 1
print(f"Total count: {count}")
