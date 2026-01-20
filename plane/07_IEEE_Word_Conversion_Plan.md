# IEEE 포맷 Word 자동 변환 계획 (IEEE Format Conversion Plan)

**목표:** `IEEE_DPF_Paper_Final_Extended.md` (국문) 파일을 IEEE 표준 2단 포맷의 Word(.docx) 파일로 자동 변환.  
**핵심 요구사항:** 수식/표/이미지 깨짐 방지, 2문단 구조(Two-column) 적용, 넘버링 규칙 준수.

---

## 1. IEEE 논문 포맷 분석 및 적용 규칙

| 항목 | IEEE 표준 규격 | 변환 전략 |
|:---:|:---|:---|
| **페이지 레이아웃** | A4 용지, 상하좌우 여백 0.6~0.7인치 | `python-docx` Section 속성 제어 |
| **단(Column) 구조** | **제목/저자/초록:** 1단(One-column) <br> **본문:** 2단(Two-column), 단 간격 0.2인치 | Section Break (Continuous)를 사용하여 구역 분리 |
| **폰트 (Font)** | 본문: Times New Roman, 10pt <br> 제목: 24pt, 소제목: 10pt (Small Caps/Italic) | 스타일(Style) 객체 생성 및 적용 |
| **헤더 (Heading)** | **I. INTRODUCTION** (로마자 대문자) <br> **A. Subsection** (알파벳 이탤릭) | 정규식(Regex)으로 MD 헤더 파싱 후 자동 치환 |
| **수식 (Equation)** | 수식 번호 우측 정렬: $ a+b=c \quad (1) $ | LaTeX 수식을 Matplotlib로 고해상도 이미지 렌더링 후 삽입 (호환성 보장) |
| **그림/표** | **그림:** 하단 캡션 (Fig. 1.) <br> **표:** 상단 캡션 (Table I.) | 캡션 위치 자동 조정 및 단(Column) 폭에 맞춰 리사이징 |

---

## 2. 변환 프로세스 (Python Script Logic)

### **Step 1: Markdown 파싱 (Parsing)**
*   파일을 읽어 섹션(Header), 텍스트(Paragraph), 수식(Equation), 이미지(Image), 표(Table) 블록으로 분리.
*   **전처리:** 
    *   MD 헤더(`## 1. 서론`) $\to$ IEEE 스타일(`I. 서론`)로 텍스트 변환.
    *   참고문헌(`[1]`) 자동 넘버링 체크.

### **Step 2: 문서 구조 생성 (Document Setup)**
1.  **초기화:** `Document()` 객체 생성 및 기본 스타일(Times New Roman) 설정.
2.  **1단 영역 (Title Area):**
    *   논문 제목 (Center, 24pt, Bold)
    *   저자 및 소속 (Center, 10pt)
    *   **Abstract & Keywords:** 굵은 글씨로 시작 (Bold "Abstract—", "Keywords—").
3.  **2단 영역 (Body Area):**
    *   `Section Break` 삽입 후, 해당 섹션의 속성을 `cols=2`로 설정 (OXML 직접 제어 필요).

### **Step 3: 콘텐츠 삽입 및 스타일링**
*   **본문 텍스트:** 양쪽 정렬(Justify) 적용.
*   **수식 처리 (Critical):**
    *   Markdown의 `$$ ... $$` 블록을 감지.
    *   `matplotlib.pyplot.text`를 사용하여 수식을 투명 배경의 고해상도 PNG로 렌더링.
    *   Word 문서에 이미지로 삽입 (너비 조정). $\to$ **"깨지지 않음" 보장.**
*   **이미지 처리:**
    *   기존 이미지 경로(`images/`)를 추적하여 삽입.
    *   가로 폭을 단 너비(약 8.5cm)에 맞게 자동 리사이징.
    *   캡션 스타일: `Fig. N.` (Bold) + 설명.
*   **표 처리:**
    *   Markdown Table을 파싱하여 Word Table 객체 생성.
    *   스타일: 테두리 최소화 (상단/하단 이중선 등 IEEE 스타일 흉내).

### **Step 4: 저장 및 검증**
*   파일명: `IEEE_DPF_Paper_Final_Submission.docx`
*   사용자에게 다운로드 및 육안 검토 요청.

---

## 3. 예상 실행 스크립트 구조

```python
# Pseudo-code
def main():
    doc = Document()
    setup_ieee_styles(doc)
    
    # 1. Title & Abstract
    add_title_section(doc, md_content)
    
    # 2. Body (2-Column)
    start_two_column_section(doc)
    
    blocks = parse_markdown(md_path)
    for block in blocks:
        if block.type == 'HEADER':
            add_ieee_heading(doc, block.text)
        elif block.type == 'EQUATION':
            img_path = render_latex_to_image(block.content)
            doc.add_picture(img_path)
        elif block.type == 'TABLE':
            create_word_table(doc, block.content)
        # ... (이미지, 텍스트 처리)
        
    doc.save('IEEE_DPF_Final.docx')
```

이 계획은 **"내용의 완벽한 보존"**과 **"형식의 호환성"**을 최우선으로 합니다. 승인해주시면 바로 스크립트 작성에 착수하겠습니다.
