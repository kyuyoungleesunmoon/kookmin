import win32com.client
import os
import time

def refine_paper():
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = True
    word.DisplayAlerts = False
    
    doc_path = r'C:\국민대프로젝트\IEEE_DPF_Paper_Korean_Final.docx'
    img_path = r'C:\국민대프로젝트\architecture_diagram_korean.png'
    
    try:
        doc = word.Documents.Open(doc_path)
        print(f"Opened {doc_path}")

        # 1. Update Tables
        wdBorderTop = -1
        wdBorderBottom = -3
        wdLineStyleDouble = 7
        wdLineStyleSingle = 1
        wdLineWidth050pt = 4
        
        print(f"Processing {doc.Tables.Count} tables...")
        for i in range(1, doc.Tables.Count + 1):
            try:
                tbl = doc.Tables(i)
                tbl.Borders.Enable = False 
                tbl.Borders(wdBorderTop).LineStyle = wdLineStyleDouble
                tbl.Borders(wdBorderTop).LineWidth = wdLineWidth050pt
                tbl.Borders(wdBorderBottom).LineStyle = wdLineStyleDouble
                tbl.Borders(wdBorderBottom).LineWidth = wdLineWidth050pt
                if tbl.Rows.Count > 1:
                    tbl.Rows(1).Borders(wdBorderBottom).LineStyle = wdLineStyleSingle
                    tbl.Rows(1).Borders(wdBorderBottom).LineWidth = wdLineWidth050pt
                tbl.Range.Font.Name = "Times New Roman"
                tbl.Range.Font.Size = 8
                tbl.AutoFitBehavior(1) 
            except Exception as e:
                print(f"Table {i} error: {e}")
            
        print("Tables updated.")

        # 2. Insert Diagram
        find = doc.Content.Find
        find.ClearFormatting()
        
        # 'III. 제안 방법' 찾기
        if find.Execute(FindText="III. 제안 방법"):
            # 해당 단락 끝으로 이동
            rng = find.Parent
            rng.Collapse(0) # Collapse End
            rng.InsertParagraphAfter()
            
            # 삽입할 위치: 방금 만든 문단
            # rng.End는 'III. 제안 방법' 직후. InsertParagraphAfter로 문단 생김.
            # 그 다음 문단으로 이동
            
            # 간단히: 문서의 그 다음 위치를 잡자.
            # rng.Next(Unit=4, Count=1) (wdParagraph)
            
            insert_rng = doc.Range(rng.End, rng.End)
            insert_rng.InsertParagraphAfter() # 빈 줄 하나 더
            
            pic_rng = doc.Range(insert_rng.End, insert_rng.End)
            inline_shape = pic_rng.InlineShapes.AddPicture(FileName=img_path, LinkToFile=False, SaveWithDocument=True)
            
            # Resize
            target_width = 3.4 * 72 
            if inline_shape.Width > target_width:
                aspect = inline_shape.Height / inline_shape.Width
                inline_shape.Width = target_width
                inline_shape.Height = target_width * aspect
                print("Resized diagram.")

            # Caption
            pic_rng.InsertParagraphAfter()
            cap_rng = doc.Range(pic_rng.End, pic_rng.End) # Move to very end
            cap_rng.InsertAfter("그림 1. 제안하는 도메인 브리지 전이학습 프레임워크")
            cap_rng.Paragraphs.Last.Alignment = 1
            cap_rng.Paragraphs.Last.Range.Font.Size = 8
            
        # 3. Resize all images
        for shp in doc.InlineShapes:
            if shp.Width > 3.5 * 72:
                aspect = shp.Height / shp.Width
                shp.Width = 3.4 * 72
                shp.Height = 3.4 * 72 * aspect
        
        doc.Save()
        print("Document saved.")
        doc.Close()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        word.Quit()

if __name__ == "__main__":
    refine_paper()
