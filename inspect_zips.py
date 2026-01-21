
import zipfile
import os

zip_files = [
    r"c:\1.이규영개인폴더\09.##### SCHOOL #####\zip\x ray defects.v5i.yolov5pytorch.zip",
    r"c:\1.이규영개인폴더\09.##### SCHOOL #####\zip\Casting defects.v1i.yolov8.zip",
    r"c:\1.이규영개인폴더\09.##### SCHOOL #####\zip\X-ray Weld Defect.v1i.yolov5pytorch.zip"
]

for zip_path in zip_files:
    if os.path.exists(zip_path):
        print(f"\n--- Output for {os.path.basename(zip_path)} ---")
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                print(f"Total files: {len(file_list)}")
                # Print first 10 files to guess structure
                for file in file_list[:10]:
                    print(file)
                
                # Check for yaml or typical dataset markers
                yaml_files = [f for f in file_list if f.endswith('.yaml')]
                if yaml_files:
                    print(f"YAML config found: {yaml_files}")
        except Exception as e:
            print(f"Error reading zip: {e}")
    else:
        print(f"File not found: {zip_path}")
