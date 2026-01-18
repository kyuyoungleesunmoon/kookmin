import win32com.client
import os
import time

def finalize_paper():
    word = win32com.client.gencache.EnsureDispatch('Word.Application')
    word.Visible = True
    word.DisplayAlerts = False
    
    base_dir = r'C:\국민대프로젝트'
    source_path = os.path.join(base_dir, 'IEEE_DPF_논문_최종본.docx')
    target_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final_Rev4.docx')
    
    prev_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final_Rev2.docx')
    if not os.path.exists(prev_path):
         prev_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final.docx')
        
    import shutil
    try:
        shutil.copy(prev_path, target_path)
    except:
        pass
    
    try:
        source_doc = word.Documents.Open(source_path)
        target_doc = word.Documents.Open(target_path)
        
        print("Opened Docs")
        
        # 1. Cleanup
        print("Cleaning text...")
        rng = target_doc.Content
        find = rng.Find
        find.ClearFormatting()
        find.Replacement.ClearFormatting()
        find.Execute(FindText="✓", ReplaceWith="", Replace=2) 
        
        # 2. Font
        print("Fixing fonts...")
        target_doc.Content.Font.Size = 10
        target_doc.Content.Font.Name = "Times New Roman"
        
        # Title
        target_doc.Paragraphs(1).Range.Font.Size = 24
        target_doc.Paragraphs(1).Range.Font.Bold = True
        target_doc.Paragraphs(1).Alignment = 1
        
        # Author
        target_doc.Paragraphs(4).Range.Font.Size = 11
        
        # Headers
        romans = ["I. ", "II. ", "III. ", "IV. ", "V. ", "VI. ", "VII. "]
        for r in romans:
             # Just simple search
            find = target_doc.Content.Find
            find.ClearFormatting()
            while find.Execute(FindText=r):
                rng = find.Parent
                # Header usually start of para
                if rng.Start == rng.Paragraphs(1).Range.Start and len(rng.Paragraphs(1).Range.Text) < 80:
                    rng.Paragraphs(1).Range.Font.Bold = True
                    rng.Paragraphs(1).Range.Font.Size = 10
                    rng.Paragraphs(1).Range.Font.Name = "Times New Roman"

        # 3. Images
        print("Inserting images...")
        insert_point = target_doc.Content.End - 1
        
        find = target_doc.Content.Find
        find.ClearFormatting()
        # Ensure we search forward
        if find.Execute(FindText="VI. 토론"):
            insert_point = find.Parent.Start
        
        rng_insert = target_doc.Range(insert_point, insert_point)
        rng_insert.InsertParagraphAfter()
        rng_insert.Collapse(0) 
        
        cnt = source_doc.InlineShapes.Count
        print(f"Source images: {cnt}")
        
        for i in range(2, cnt + 1):
            try:
                print(f"Copying Image {i}...")
                source_doc.InlineShapes(i).Range.Copy()
                
                rng_insert.Paste()
                rng_insert.InsertParagraphAfter()
                rng_insert.Collapse(0)
                time.sleep(0.5)
            except Exception as e:
                print(f"Err {i}: {e}")
                
        # 4. Tables & Resize
        wdBorderTop = -1
        wdBorderBottom = -3
        wdLineStyleDouble = 7
        wdLineStyleSingle = 1
        
        for tbl in target_doc.Tables:
            try:
                tbl.Borders.Enable = False
                tbl.Borders(wdBorderTop).LineStyle = wdLineStyleDouble
                tbl.Borders(wdBorderTop).LineWidth = 4
                tbl.Borders(wdBorderBottom).LineStyle = wdLineStyleDouble
                tbl.Borders(wdBorderBottom).LineWidth = 4
                if tbl.Rows.Count > 1:
                    tbl.Rows(1).Borders(wdBorderBottom).LineStyle = wdLineStyleSingle
                    tbl.Rows(1).Borders(wdBorderBottom).LineWidth = 4
                tbl.Range.Font.Name = "Times New Roman"
                tbl.Range.Font.Size = 8 
                tbl.AutoFitBehavior(1) 
            except:
                pass
            
        target_width = 3.4 * 72 
        for shp in target_doc.InlineShapes:
            if shp.Width > target_width:
                 aspect = shp.Height / shp.Width
                 shp.Width = target_width
                 shp.Height = target_width * aspect
                 
        target_doc.Save()
        source_doc.Close(False)
        target_doc.Close(False)
        print("Done.")
        
    except Exception as e:
        print(f"Critical Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        word.Quit()

if __name__ == "__main__":
    finalize_paper()
