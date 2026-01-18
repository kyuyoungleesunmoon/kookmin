import win32com.client
import os
import time

def fix_paper():
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = True
    word.DisplayAlerts = False 
    
    base_dir = r'C:\국민대프로젝트'
    source_path = os.path.join(base_dir, 'IEEE_DPF_논문_최종본.docx')
    template_path = os.path.join(base_dir, 'TII_Articles_Word_template_2025.doc')
    output_path = os.path.join(base_dir, 'IEEE_DPF_Paper_Korean_Final.docx')
    
    print("Starting Word automation...")
    
    try:
        source = word.Documents.Open(source_path)
        print("Opened Source")
        
        abstract_start = None
        body_start = None
        
        # Searching for 'Abstract'
        find = source.Content.Find
        find.ClearFormatting()
        if find.Execute(FindText="Abstract"):
            abstract_start = find.Parent.Start
            print(f"Found Abstract at {abstract_start}")
        
        # Searching for 'I. 서론' or '1. 서론'
        # Reset matching range
        search_rng = source.Content
        find = search_rng.Find
        find.ClearFormatting()
        if find.Execute(FindText="I. 서론"):
            body_start = find.Parent.Start
            print(f"Found Introduction (I. 서론) at {body_start}")
        else:
            search_rng = source.Content
            find = search_rng.Find
            find.ClearFormatting()
            if find.Execute(FindText="1. 서론"):
                body_start = find.Parent.Start
                print(f"Found Introduction (1. 서론) at {body_start}")

        if body_start is None:
            print("Could not find 'I. 서론'. Using heuristic (Para 28 approx).")
            # Try to find a paragraph with '서론'
            for i in range(1, source.Paragraphs.Count+1):
                if '서론' in source.Paragraphs(i).Range.Text:
                    body_start = source.Paragraphs(i).Range.Start
                    print(f"Found '서론' at Para {i}")
                    break
        
        template = word.Documents.Open(template_path)
        print("Opened Template")
        
        # --- TITLE ---
        try:
            # Copy first 2 paragraphs
            rng = source.Range(source.Paragraphs(1).Range.Start, source.Paragraphs(2).Range.End)
            rng.Copy()
            
            find = template.Content.Find
            find.ClearFormatting()
            if find.Execute(FindText="Paper Title"):
                find.Parent.Paste()
                print("Pasted Title")
        except Exception as e:
            print(f"Error copying title: {e}")

        # --- AUTHOR ---
        try:
            source.Paragraphs(4).Range.Copy()
            
            find = template.Content.Find
            find.ClearFormatting()
            if find.Execute(FindText="Author Name"):
                find.Parent.Paste()
                print("Pasted Author")
        except Exception as e:
             print(f"Error copying author: {e}")

        # --- ABSTRACT ---
        try:
            if abstract_start and body_start:
                # Abstract ends before body start? Or "Index Terms"?
                # Let's verify if "Index Terms" exists.
                index_terms_start = body_start
                rng_srch = source.Range(abstract_start, body_start)
                f2 = rng_srch.Find
                if f2.Execute(FindText="Index Terms"):
                    index_terms_start = f2.Parent.Start
                
                source.Range(abstract_start, index_terms_start).Copy()
                
                find = template.Content.Find
                find.ClearFormatting()
                if find.Execute(FindText="Abstract"):
                     find.Parent.Select() # Selecting 'Abstract' text
                     # Paste? It might wipe formatting.
                     # Better to paste AFTER 'Abstract'?
                     # Or replace.
                     find.Parent.Paste()
                     print("Pasted Abstract")
        except Exception as e:
            print(f"Error copying abstract: {e}")
            
        # --- BODY ---
        try:
            # Copy from Body Start to End
            # Check if Index Terms omitted? 
            # If we want Index Terms, we should include them somewhere.
            # Usually Index Terms are between Abstract and Intro.
            
            source.Range(body_start, source.Content.End).Copy()
            
            find = template.Content.Find
            find.ClearFormatting()
            if find.Execute(FindText="I. INTRODUCTION"):
                # Select from I. INTRODUCTION to End?
                start_rng = find.Parent.Start
                # We assume standard template has text after this.
                # Let's select current selection to document end?
                rng_target = template.Range(start_rng, template.Content.End)
                rng_target.Paste()
                print("Pasted Body over I. INTRODUCTION")
            else:
                 print("Could not find 'I. INTRODUCTION' in template. Searching just 'INTRODUCTION'...")
                 find = template.Content.Find
                 find.ClearFormatting()
                 if find.Execute(FindText="INTRODUCTION"):
                    rng_target = template.Range(find.Parent.Start, template.Content.End)
                    rng_target.Paste()
                    print("Pasted Body over INTRODUCTION")

        except Exception as e:
            print(f"Error copying body: {e}")

        # Save
        template.SaveAs(output_path, 16)
        print(f"Saved to {output_path}")

        source.Close(False)
        template.Close(False)
        
    except Exception as e:
        print(f"Critical Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        word.Quit()
        print("Done.")

if __name__ == "__main__":
    fix_paper()
