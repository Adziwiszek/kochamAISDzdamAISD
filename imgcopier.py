import os
import re
import shutil

# KONFIGURACJA
md_folder = "listy/"           # folder z plikami markdown
source_img_folder = "/mnt/c/bleeh/"  # folder, gdzie są przechowywane obrazy
dest_img_folder = "listy/"      # folder, do którego kopiujesz obrazy

# REGEX do znajdywania obrazków w formacie Obsidian i Markdown
image_patterns = [
    re.compile(r'!\[\[(.*?)\]\]'),            # ![[obraz.png]]
    re.compile(r'!\[.*?\]\((.*?)\)'),         # ![](ścieżka/obraz.png)
]

# Upewnij się, że folder docelowy istnieje
os.makedirs(dest_img_folder, exist_ok=True)

# Przejdź przez wszystkie pliki markdown
for filename in os.listdir(md_folder):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(md_folder, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Zbierz wszystkie ścieżki obrazów
    images = set()
    for pattern in image_patterns:
        matches = pattern.findall(content)
        images.update(matches)

    # Kopiuj obrazy, jeśli istnieją w źródle i nie ma ich w miejscu docelowym
    for img in images:
        img_name = os.path.basename(img)  # tylko nazwa pliku
        src_path = os.path.join(source_img_folder, img_name)
        dest_path = os.path.join(dest_img_folder, img_name)

        if os.path.exists(src_path):
            if not os.path.exists(dest_path):
                shutil.copy2(src_path, dest_path)
                print(f"Skopiowano: {img_name}")
            else:
                print(f"Już istnieje: {img_name}")
        else:
            print(f"Nie znaleziono źródła: {img_name}")

