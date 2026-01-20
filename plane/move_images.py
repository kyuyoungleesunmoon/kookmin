import shutil
import os
import glob

src_dir = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\images_recovered"
dst_dir = r"c:\1.이규영개인폴더\09.##### SCHOOL #####\converted_md\images"

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

files = glob.glob(os.path.join(src_dir, "*.*"))
print(f"이동할 파일 수: {len(files)}")

for f in files:
    try:
        shutil.move(f, dst_dir)
        print(f"Moved: {os.path.basename(f)}")
    except Exception as e:
        print(f"Error moving {os.path.basename(f)}: {e}")
