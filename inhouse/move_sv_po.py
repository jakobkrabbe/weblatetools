#!/usr/bin/python3

# After creating sv.po files and translating, all sv.po-files are located in the home catalogue.
# Then it's time to move them back to where they belong! :-)
# Thin is for all our inhouse created modules and third pary modules. 

import os
import shutil
import subprocess

base_folder = os.getcwd()
po_files = [f for f in os.listdir(base_folder) if f.endswith('.po')]

for po_file in po_files:
    if not po_file.endswith('-sv.po'):
        print(f"Hoppar över {po_file}, kan inte extrahera modulnamn")
        continue

    modname = po_file[:-6]  # ta bort -sv.po

    # Anropa locate för att hitta modulens sökväg
    try:
        locate_output = subprocess.check_output(['locate', modname], text=True).strip().split('\n')
        # Filtrera och ta första sökvägen som är katalog och verkar rimlig
        module_paths = [p for p in locate_output if os.path.isdir(p) and os.path.basename(p) == modname]
        if not module_paths:
            print(f"Modul '{modname}' hittades inte med locate")
            continue
        module_path = module_paths[0]
    except subprocess.CalledProcessError:
        print(f"Fel vid anrop av locate för modul '{modname}'")
        continue

    i18n_path = os.path.join(module_path, 'i18n')
    os.makedirs(i18n_path, exist_ok=True)

    src_file = os.path.join(base_folder, po_file)
    dst_file = os.path.join(i18n_path, 'sv.po')

    try:
        shutil.move(src_file, dst_file)
        print(f"Flyttade {po_file} till {dst_file}")
    except Exception as e:
        print(f"Fel vid flytt av {po_file}: {e}")
