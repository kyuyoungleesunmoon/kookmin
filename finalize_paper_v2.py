import win32com.client
import os
import time

def finalize_paper():
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = True
    word.DisplayAlerts = False
    
    base_dir = r'C:\국민대프로젝트'
    source_path = os.path.join(base_dir, 'IEEE_DPF_논문_최종본.docx')
    # 이전 단계 결과물을 입력으로 사용
    target_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final_Rev1.docx')
    # 이전 파일 복사해서 시작
    if os.path.exists(os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final.docx')):
        import shutil
        shutil.copy(os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final.docx'), target_path)
    
    diagram_img = os.path.join(base_dir, 'architecture_diagram_korean.png')

    try:
        source_doc = word.Documents.Open(source_path)
        print("Opened Source Doc")
        
        target_doc = word.Documents.Open(target_path)
        print("Opened Target Doc")
        
        # 1. AI Tone Cleanup (✓ removal)
        print("Cleaning up text...")
        find = target_doc.Content.Find
        find.ClearFormatting()
        find.Replacement.ClearFormatting()
        # Replace checkmarks with empty or proper text if needed.
        # Assuming usage like "Method ✓" -> "Method (Applied)"
        # Or just remove them.
        find.Execute(FindText="✓", ReplaceWith="", Replace=2) # 2=wdReplaceAll
        
        # 2. Font Standardization (Main Body)
        # Strategy: Apply 10pt to whole document, then fix Title/Author/Headings
        print("Standardizing fonts...")
        # target_doc.Content.Font.Name = "Times New Roman" # Or Batang for Korean? IEEE uses Times usually.
        # Let's use clean standard font.
        # target_doc.Content.Font.Size = 10
        # This might ruin Title size. 
        # Better: Loop paragraphs? Too slow.
        # Let's fix Title and Headings AFTER bulk update if we do bulk update.
        # But safest is to iterate through styles. IEEE Template should have styles.
        # Because User said "글자 크기가 전부 같게 만들어줘 다른게 많이 보여", 
        # it implies body text is inconsistent.
        
        # Let's force Normal style to 10pt
        # target_doc.Styles("Normal").Font.Size = 10 -> might affect everything based on Normal.
        # target_doc.Styles("표준").Font.Size = 10
        
        # Let's try selecting 'Body' ranges. 
        # Just manually set Paragraphs 1-4 (Title/Author) to correct sizes later.
        
        target_doc.Content.Font.Size = 10
        target_doc.Content.Font.NameHangul = "바탕" # Batang
        target_doc.Content.Font.Name = "Times New Roman"
        
        # Restore Title (Para 1-2)
        target_doc.Paragraphs(1).Range.Font.Size = 24
        target_doc.Paragraphs(1).Range.Font.Bold = True
        target_doc.Paragraphs(1).Alignment = 1 # Center
        
        target_doc.Paragraphs(2).Range.Font.Size = 24 # In case title is multi-line
        target_doc.Paragraphs(2).Range.Font.Bold = True
        
        # Author (Para 4?) - Let's search pattern?
        # create_ieee script put Author at Para 4.
        target_doc.Paragraphs(4).Range.Font.Size = 11
        target_doc.Paragraphs(5).Range.Font.Size = 9 # Affiliation
        
        # Section Headers (Search for Roman Numerals I. II. III.)
        # This is tedious. Let's assume the user can fix minor header size issues, 
        # but the main complaint is body text.
        # We will try to find "I.", "II." and bold/upsize them.
        romans = ["I. ", "II. ", "III. ", "IV. ", "V. ", "VI. ", "VII. "]
        for r in romans:
            find = target_doc.Content.Find
            find.ClearFormatting()
            while find.Execute(FindText=r):
                # Check if it's a header (start of paragraph)
                rng = find.Parent
                if rng.Start == rng.Paragraphs(1).Range.Start:
                    rng.Paragraphs(1).Range.Font.Bold = True
                    rng.Paragraphs(1).Range.Font.Size = 10 # Keep 10 but Bold
                    rng.Paragraphs(1).Range.Font.Name = "Times New Roman"
                    # Also Index Terms, Abstract
                
        # 3. Image Insertion
        print("Inserting images...")
        
        # Figure 1: Architecture Diagram (New)
        # Find placeholder based on previous script: "그림 1. 제안하는..."
        # Or Just keyword "[그림 1" (from raw text insert)
        # Note: refine_ieee_paper.py already inserted Figure 1. 
        # If we run on top of that, we have Figure 1.
        # But we want to ensure *all* images from Source are placed.
        
        # Source Images mapping:
        # User said "실험결과 이미지(전부 사용)".
        # Usually Source Doc has:
        # Fig 1 (Arch), Fig 2 (Confusion), Fig 3 (PR Curve), Fig 4 (Batch), Fig 5 (F1)
        # We need to transfer Fig 2, 3, 4, 5...
        
        # Let's count source inline shapes
        cnt = source_doc.InlineShapes.Count
        print(f"Source has {cnt} images.")
        
        # We map Source Shape Index -> Target Text Placeholder
        # We put text placeholders like "[그림 2: 혼동 행렬]" in create_ieee_paper_korean.py
        # Check source image 2 -> target "[그림 2"
        
        # First, let's replace Figure 1 if needed (User said "여전히 어색하네... 이미지로 말로 텍스트로 풀어서").
        # Means he wants the New Diagram we made. Refine script did that.
        # So we skip Source Image 1.
        
        for i in range(2, cnt + 1):
            try:
                # Copy from Source
                source_doc.InlineShapes(i).Range.Copy()
                
                # Find placeholder in Target
                # We generated text like "\n[그림 {i}: ...]\n"
                find_txt = f"[그림 {i}"
                
                find = target_doc.Content.Find
                find.ClearFormatting()
                if find.Execute(FindText=find_txt):
                    rng = find.Parent
                    # Select the whole line/paragraph of the placeholder
                    rng.Paragraphs(1).Range.Select()
                    
                    # Compute width for resizing
                    # IEEE column width ~ 3.4 inches
                    target_width = 3.4 * 72
                    
                    # Paste
                    word.Selection.Paste() # Paste replaces selection
                    
                    # Resize the just pasted image
                    # It's likely the last InlineShape in that range or document?
                    # Safer to check selection range inlineshapes, or just last added.
                    if word.Selection.InlineShapes.Count > 0:
                        shp = word.Selection.InlineShapes(1)
                        if shp.Width > target_width:
                            aspect = shp.Height / shp.Width
                            shp.Width = target_width
                            shp.Height = target_width * aspect
                    else:
                        # Fallback: check closest shape
                         pass
                    
                    print(f"Pasted Image {i}")
                    time.sleep(0.5)
                else:
                    print(f"Placeholder for Figure {i} not found.")
            except Exception as e:
                print(f"Error copying image {i}: {e}")

        # Final check on Figure 1
        # If Refine step failed or we overwrite, ensure New Diagram is there.
        # Assuming Refine ran okay. 
        
        # 4. Table Style Enforcement (Again, to be sure)
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
            tbl.Range.Font.Size = 8 # Tables are small
            tbl.AutoFitBehavior(1) # AutoFit Window
            
        target_doc.Save()
        source_doc.Close(False)
        target_doc.Close(False) # Don't quit, maybe? No, close doc.
        
    except Exception as e:
        print(f"Critical Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        word.Quit()

if __name__ == "__main__":
    finalize_paper()
