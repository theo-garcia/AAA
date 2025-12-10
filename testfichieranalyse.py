import os

folder = input("Path of the folder to be analyzed : ")

extension = [
    '.txt', '.py', '.pdf', '.jpg', '.png', '.docx', '.xlsx',
    '.zip', '.mp4', '.mp3', '.iso', '.json', '.html', '.css', '.js'
]

def count_exts(folder):
    counts = {ext: 0 for ext in extension}

    for root, dirs, files in os.walk(folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in counts:
                counts[ext] += 1

    total = sum(counts.values())
    return counts, total

def get_ext_distribution(count, total):
    if total == 0:
        return "0%"
    return f"({count * 100 / total:.2f}%)"

counts, total = count_exts(folder)

for ext in extension:
    print(f"File {ext:<5} :", counts[ext], get_ext_distribution(counts[ext], total))

print("Total files analyzed :", total)


