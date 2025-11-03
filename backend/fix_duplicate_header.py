import shutil
import os

src = r"c:\Users\Raghav\OneDrive\Desktop\Sentiment_Analysis_on_Social_Media\data\tweets.csv"
bak = src + ".bak"
tmp = src + ".tmp"

# Create backup
shutil.copy2(src, bak)

# Read first line (header) and skip duplicate header
header = None
lines_to_write = []

with open(src, "r", encoding="utf-8", errors="replace") as f:
    header = f.readline().strip()
    second_line = f.readline().strip()
    
    # If second line is also a header, skip it
    if second_line != header:
        lines_to_write.append(second_line)
    
    # Copy rest of the file
    for line in f:
        lines_to_write.append(line.rstrip("\r\n"))

# Write corrected file
with open(tmp, "w", encoding="utf-8", newline='') as f:
    f.write(header + "\n")  # Write the header first
    for line in lines_to_write:
        f.write(line + "\n")

# Replace original with corrected version
os.replace(tmp, src)

# Verify result - print first 5 lines
print("=== First 5 lines after fix ===")
with open(src, "r", encoding="utf-8") as f:
    for _ in range(5):
        print(f.readline().rstrip())