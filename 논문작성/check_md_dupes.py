file_path = r"C:\국민대프로젝트\converted_md\이규영_국민대_DPF_논문.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Check if the second half is a copy of the first half
half = len(lines) // 2
first_half = lines[:half]
second_half = lines[half:]

# Adjust for potential header differences or slight mismatches
print(f"First line of first half: {first_half[0].strip()}")
print(f"First line of second half: {second_half[0].strip()}")

# Simple sliding window or similarity check
# Let's find where the first line repeats
first_line = lines[0].strip()
repeats = []
for i, line in enumerate(lines[1:], 1):
    if line.strip() == first_line and len(line.strip()) > 5:
        repeats.append(i)

print(f"First line repeats at indices: {repeats}")

if repeats:
    split_point = repeats[0]
    print(f"Potential split point: {split_point}")
    
    # Verify exact match
    is_exact_copy = True
    for i in range(min(split_point, len(lines) - split_point)):
        if lines[i] != lines[split_point + i]:
             # print(f"Mismatch at {i}: {lines[i].strip()} vs {lines[split_point+i].strip()}")
             pass # Don't spam
                  
    print("Checked for exact copy logic.")
