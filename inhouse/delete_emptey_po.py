#!/usr/bin/env python3
import os

# Den katalog där skriptet körs (t.ex. skrivbordet)
base_folder = os.getcwd()

# Hitta alla .po-filer i katalogen
po_files = [f for f in os.listdir(base_folder) if f.endswith('.po')]

for po_file in po_files:
    file_path = os.path.join(base_folder, po_file)
    
    # Kontrollera om filen är tom (storlek 0)
    if os.path.getsize(file_path) == 0:
        print(f"Tar bort tom fil: {po_file}")
        os.remove(file_path)
