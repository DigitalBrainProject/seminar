
import re

file_path = r'c:\Users\efstk\OneDrive\Desktop\seminar-1\archive.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find speaker divs and wrap content in parentheses with span class="affiliation"
# We match <div class="speaker"> ... </div> and then substitute inside it.
# This assumes no nested divs in speaker.

def replace_affiliation(match):
    inner_content = match.group(1)
    # Regex to find content in parentheses (including newlines if any, though less likely inside parens)
    # We want to match (Affiliation) but avoid matching attributes if any, though parens in attributes are rare here.
    # The text usually is Name (Affiliation).
    
    # Simple strategy: Replace any (Text) with <span class="affiliation">(Text)</span>
    # But watch out for JST in badges (handled by outer regex limiting to speaker div)
    
    new_inner = re.sub(r'(\([^)]+\))', r'<span class="affiliation">\1</span>', inner_content)
    return f'<div class="speaker">{new_inner}</div>'

# Regex for the speaker div
# DOTALL to match newlines if speaker div spans lines
updated_content = re.sub(r'<div class="speaker">(.*?)</div>', replace_affiliation, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(updated_content)
