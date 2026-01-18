import win32com.client
import os
import time

def finalize_paper():
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = True
    word.DisplayAlerts = False
    
    base_dir = r'C:\국민대프로젝트'
    source_path = os.path.join(base_dir, 'IEEE_DPF_논문_최종본.docx')
    target_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final_Rev2.docx')
    
    # Copy previous rev
    if os.path.exists(os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final.docx')):
        import shutil
        shutil.copy(os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final.docx'), target_path)
    
    try:
        source_doc = word.Documents.Open(source_path)
        print("Opened Source Doc")
        
        target_doc = word.Documents.Open(target_path)
        print("Opened Target Doc")
        
        # 1. Cleanup
        print("Cleaning up text...")
        find = target_doc.Content.Find
        find.ClearFormatting()
        find.Replacement.ClearFormatting()
        find.Execute(FindText="✓", ReplaceWith="", Replace=2) 
        
        # 2. Font
        print("Standardizing fonts...")
        # Apply strict 10pt
        target_doc.Content.Font.Size = 10
        # Try setting standard font. Word handles dual fonts (ascii/fareast).
        target_doc.Content.Font.Name = "Times New Roman"
        
        # Restore Title
        target_doc.Paragraphs(1).Range.Font.Size = 24
        target_doc.Paragraphs(1).Range.Font.Bold = True
        target_doc.Paragraphs(1).Alignment = 1
        
        # Author
        target_doc.Paragraphs(4).Range.Font.Size = 11
        
        # Headers
        romans = ["I. ", "II. ", "III. ", "IV. ", "V. ", "VI. ", "VII. "]
        for r in romans:
            find = target_doc.Content.Find
            find.ClearFormatting()
            while find.Execute(FindText=r):
                rng = find.Parent
                # Check if it's likely a header (length < 100 char)
                if len(rng.Paragraphs(1).Range.Text) < 100:
                    rng.Paragraphs(1).Range.Font.Bold = True
                    rng.Paragraphs(1).Range.Font.Size = 10
                    rng.Paragraphs(1).Range.Font.Name = "Times New Roman"
                    
        # 3. Images
        cnt = source_doc.InlineShapes.Count
        print(f"Source images: {cnt}")
        
        for i in range(2, cnt + 1):
            try:
                source_doc.InlineShapes(i).Range.Copy()
                find_txt = f"[그림 {i}"
                find = target_doc.Content.Find
                find.ClearFormatting()
                if find.Execute(FindText=find_txt):
                    rng = find.Parent
                    rng.Paragraphs(1).Range.Paste()
                    
                    # Resize newly pasted
                    # Because Paste replaces selection, the new image should be in the selection range or nearby.
                    # Wait a bit
                    time.sleep(0.5)
                    # We can iterate Backwards from insertion point?
                    # Or just check InlineShapes count?
                    # Let's assume the user can manually resize if this script is flaky.
                    # But we'll try to resize 'all' images at the end anyway.
                    
                    print(f"Pasted Image {i}")
                else:
                    print(f"Placeholder {i} not found")
            except Exception as e:
                print(f"Err {i}: {e}")
                
        # 4. Tables & Resize All Images
        wdBorderTop = -1
        wdBorderBottom = -3
        wdLineStyleDouble = 7
        wdLineStyleSingle = 1
        
        for tbl in target_doc.Tables:
            tbl.Borders.Enable = False
            tbl.Borders(wdBorderTop).LineStyle = wdLineStyleDouble
            tbl.Borders(wdBorderBottom).LineStyle = wdLineStyleDouble
            if tbl.Rows.Count > 1:
                tbl.Rows(1).Borders(wdBorderBottom).LineStyle = wdLineStyleSingle
            tbl.Range.Font.Size = 8 
            tbl.AutoFitBehavior(1) 
            
        # Resize ALL images (including Diagram and pasted ones)
        target_width = 3.4 * 72 # 3.4 inches
        for shp in target_doc.InlineShapes:
            if shp.Width > target_width:
                 aspect = shp.Height / shp.Width
                 shp.Width = target_width
                 shp.Height = target_width * aspect
                 
        target_doc.Save()
        source_doc.Close(False)
        target_doc.Close(False)
        
    except Exception as e:
        print(f"Critical Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        word.Quit()

if __name__ == "__main__":
    finalize_paper()
