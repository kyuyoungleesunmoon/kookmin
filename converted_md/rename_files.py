import os
import shutil

# Define the renaming maps
plane_files = [
    ("IEEE_DPF_Paper_Refinement_Plan_v2.md", "01_IEEE_DPF_Paper_Refinement_Plan_v2.md"),
    ("Image_Recovery_Plan.md", "02_Image_Recovery_Plan.md"),
    ("IEEE_DPF_Paper_Expansion_Plan.md", "03_IEEE_DPF_Paper_Expansion_Plan.md"),
    ("IEEE_DPF_Paper_Deepening_Plan_for_TII.md", "04_IEEE_DPF_Paper_Deepening_Plan_for_TII.md"),
    ("IEEE_DPF_Paper_Volume_Up_Plan.md", "05_IEEE_DPF_Paper_Volume_Up_Plan.md"),
    ("IEEE_DPF_Paper_Final_Expansion_Plan.md", "06_IEEE_DPF_Paper_Final_Expansion_Plan.md"),
    ("IEEE_Word_Conversion_Plan.md", "07_IEEE_Word_Conversion_Plan.md")
]

converted_files = [
    ("이규영_국민대_DPF_논문.md", "01_이규영_국민대_DPF_논문.md"),
    ("IEEE_DPF_Paper_Refined.md", "02_IEEE_DPF_Paper_Refined.md"),
    ("IEEE_DPF_Paper_TII_Draft.md", "03_IEEE_DPF_Paper_TII_Draft.md"),
    ("IEEE_DPF_Paper_Final_Extended.md", "04_IEEE_DPF_Paper_Final_Extended.md")
]

base_plane = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\plane"
base_converted = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md"

def rename_list(base_dir, file_list):
    print(f"--- Renaming in {base_dir} ---")
    for old, new in file_list:
        old_path = os.path.join(base_dir, old)
        new_path = os.path.join(base_dir, new)
        
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old} -> {new}")
            except Exception as e:
                print(f"Error renaming {old}: {e}")
        else:
            print(f"Skipped (not found): {old}")

if __name__ == "__main__":
    rename_list(base_plane, plane_files)
    rename_list(base_converted, converted_files)
