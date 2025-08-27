import os
import shutil
import subprocess

base_folder = os.getcwd()
po_files = [f for f in os.listdir(base_folder) if f.endswith('.po')]

for po_file in po_files:
    file_path = os.path.join(base_folder, po_file)
    
    # Kontrollera om filen är tom, ta bort den i så fall
    if os.path.getsize(file_path) == 0:
        print(f"Tar bort tom fil: {po_file}")
        os.remove(file_path)
        continue
    
    if not po_file.endswith('-sv.po'):
        print(f"Hoppar över {po_file}, kan inte extrahera modulnamn")
        continue
    
    modname = po_file[:-6]  # ta bort -sv.po
    
    try:
        locate_output = subprocess.check_output(['locate', modname], text=True).strip().split('\n')
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
    
    dst_file = os.path.join(i18n_path, 'sv.po')
    
    try:
        shutil.move(file_path, dst_file)
        print(f"Flyttade {po_file} till {dst_file}")
    except Exception as e:
        print(f"Fel vid flytt av {po_file}: {e}")
