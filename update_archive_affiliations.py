
import re
import os

file_path = r'c:\Users\efstk\OneDrive\Desktop\seminar-1\archive.html'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_affiliation(match):
        inner = match.group(1)
        # Wrap content in parentheses with span class="affiliation"
        # We avoid touching nested tags if possible, but simple parens are target.
        # Use a non-greedy match for content inside parens.
        # We assume the affiliation is at the end or cleanly separated.
        
        # This regex matches `(text)` where text doesn't contain `)` or `<` (to avoid breaking tags if any inside, unlikely)
        # Actually, just `\([^)]+\)` is usually safe for text content.
        
        new_inner = re.sub(r'(\([^)]+\))', r'<span class="affiliation">\1</span>', inner)
        return f'<div class="speaker">{new_inner}</div>'

    # Match the speaker div and its content.
    updated_content = re.sub(r'<div class="speaker">(.*?)</div>', replace_affiliation, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("Successfully updated archive.html")

except Exception as e:
    print(f"Error: {e}")
