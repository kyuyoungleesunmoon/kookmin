import win32com.client
import os
import time

def finalize_paper():
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = True
    word.DisplayAlerts = False
    
    base_dir = r'C:\국민대프로젝트'
    source_path = os.path.join(base_dir, 'IEEE_DPF_논문_최종본.docx')
    target_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final_Rev3.docx')
    
    # Rev3 starts from Rev2 if exists, else Rev1
    prev_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final_Rev2.docx')
    if not os.path.exists(prev_path):
        prev_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final.docx')
        
    import shutil
    shutil.copy(prev_path, target_path)
    
    try:
        source_doc = word.Documents.Open(source_path)
        print("Opened Source Doc")
        
        target_doc = word.Documents.Open(target_path)
        print("Opened Target Doc")
        
        # 1. Cleanup
        find = target_doc.Content.Find
        find.ClearFormatting()
        find.Replacement.ClearFormatting()
        find.Execute(FindText="✓", ReplaceWith="", Replace=2) 
        
        # 2. Font
        target_doc.Content.Font.Size = 10
        target_doc.Content.Font.Name = "Times New Roman"
        
        target_doc.Paragraphs(1).Range.Font.Size = 24
        target_doc.Paragraphs(1).Range.Font.Bold = True
        target_doc.Paragraphs(1).Alignment = 1
        
        target_doc.Paragraphs(4).Range.Font.Size = 11
        
        romans = ["I. ", "II. ", "III. ", "IV. ", "V. ", "VI. ", "VII. "]
        for r in romans:
            find = target_doc.Content.Find
            find.ClearFormatting()
            while find.Execute(FindText=r):
                rng = find.Parent
                if len(rng.Paragraphs(1).Range.Text) < 100:
                    rng.Paragraphs(1).Range.Font.Bold = True
                    rng.Paragraphs(1).Range.Font.Size = 10
                    rng.Paragraphs(1).Range.Font.Name = "Times New Roman"

        # 3. Insert Missing Images (2 to End)
        # Find 'V. 실험 결과' section to dump images into (or 'VI. 토론' before)
        # Assuming most images belong to Results.
        
        insert_point = target_doc.Content.End - 1 # Default end
        
        find = target_doc.Content.Find
        find.ClearFormatting()
        if find.Execute(FindText="VI. 토론"): # Insert BEFORE Discussion
            insert_point = find.Parent.Start
        elif find.Execute(FindText="V. 실험 결과"): # Or after Results header
             # Move to end of results section? Hard to know where it ends.
             # Let's insert AT THE END of the doc if VI not found.
             pass
        
        # We will insert images at the identified point
        rng_insert = target_doc.Range(insert_point, insert_point)
        
        cnt = source_doc.InlineShapes.Count
        print(f"Source images: {cnt}")
        
        # Skip 1 (Diagram)
        for i in range(2, cnt + 1):
            try:
                print(f"Copying Image {i}...")
                source_doc.InlineShapes(i).Range.Copy()
                
                rng_insert.InsertParagraphAfter()
                rng_insert.Collapse(0) # End
                rng_insert.Paste()
                
                # Internal caption
                # rng_insert.InsertParagraphAfter()
                # rng_insert.Collapse(0)
                # rng_insert.InsertAfter(f"그림 {i} (원본에서 가져옴)")
                # rng_insert.Paragraphs.Last.Alignment = 1
                # rng_insert.Paragraphs.Last.Range.Font.Size = 8
                
                time.sleep(0.5)
            except Exception as e:
                print(f"Err {i}: {e}")
                
        # 4. Tables & Resize
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
            
        target_width = 3.4 * 72 
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
