from pdfminer.high_level import extract_text
import os

out_dir = r'C:\Users\39173\Desktop\笔记\myobsidan\Notes\MIT\MIT6.041'

for i in range(1, 5):
    pdf_path = os.path.join(out_dir, f'lecture{i:02d}.pdf')
    txt_path = os.path.join(out_dir, f'lecture{i:02d}_raw.txt')
    print(f'Extracting lecture {i}...')
    try:
        text = extract_text(pdf_path)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'  Extracted {len(text)} chars -> {txt_path}')
    except Exception as e:
        print(f'  Error: {e}')

print('Done!')