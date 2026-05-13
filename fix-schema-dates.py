import glob, os

# Resolve the base path via glob (handles Cyrillic username)
bases = glob.glob('C:/Users/*/Desktop/projects/lumo-ai-agency/services')
if not bases:
    print("ERROR: could not find services directory")
    exit(1)
base = bases[0]
print(f"Base: {base}")

def fix_file(filename, search_str, replacement_str):
    path = os.path.join(base, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    has_published = '"datePublished"' in content
    has_modified = '"dateModified"' in content
    has_search = search_str in content
    print(f"\n{filename}:")
    print(f"  search found: {has_search} | datePublished: {has_published} | dateModified: {has_modified}")
    if has_search and not has_modified:
        new_content = content.replace(search_str, replacement_str, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  FIXED")
    else:
        print(f"  no change needed")

# 1. ai-automations.html — has datePublished 2026-03-08, add dateModified after it
fix_file(
    'ai-automations.html',
    '"datePublished": "2026-03-08",',
    '"datePublished": "2026-03-08",\n        "dateModified": "2026-05-13",'
)

# 2-6. Pages with no datePublished — insert both after their service url line
pages = [
    ('google-ads.html',     '"url": "https://lumoaiagency.com/services/google-ads",'),
    ('meta-ads.html',       '"url": "https://lumoaiagency.com/services/meta-ads",'),
    ('ai-development.html', '"url": "https://lumoaiagency.com/services/ai-development",'),
    ('voice-ai.html',       '"url": "https://lumoaiagency.com/services/voice-ai",'),
    ('ai-outbound.html',    '"url": "https://lumoaiagency.com/services/ai-outbound",'),
]

for filename, search_str in pages:
    replacement_str = (
        search_str +
        '\n        "datePublished": "2026-03-01",' +
        '\n        "dateModified": "2026-05-13",'
    )
    fix_file(filename, search_str, replacement_str)

print("\nAll done.")
