import os
import urllib.parse

# Configuration
BASE_DIR = "screens/800x480"
OUTPUT_FILE = "GALLERY_800x480.md"
REPO_URL = "https://github.com/usetrmnl/tailor/raw/main"

def generate_gallery():
    # Adjusted title and back-link reference for the specific size
    markdown = [
        "# 🖼️ 800x480 Screen Gallery",
        "Browse and download splash and loading screens for TRMNL OG. All images are pre-validated to **800x480 PNG**.\n",
        "> **Tip:** Right-click 'Download' and select 'Save Link As...' to save directly to your device.\n"
    ]
    
    if not os.path.exists(BASE_DIR):
        print(f"Directory {BASE_DIR} not found. Skipping.")
        return

    # Table of Contents
    categories = sorted([d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))])
    markdown.append("### 📂 Categories")
    for cat in categories:
        markdown.append(f"- [{cat.replace('_', ' ').title()}](#{cat.lower()})")
    markdown.append("\n---\n")

    for category in categories:
        cat_name = category.replace('_', ' ').title()
        markdown.append(f"## <a name='{category.lower()}'></a>{cat_name}")
        markdown.append("| Type | Preview | Action |")
        markdown.append("| :--- | :--- | :--- |")
        
        cat_path = os.path.join(BASE_DIR, category)
        for sub in ["splash", "loading"]:
            sub_path = os.path.join(cat_path, sub)
            if os.path.exists(sub_path):
                files = sorted([f for f in os.listdir(sub_path) if f.lower().endswith('.png')])
                for f in files:
                    img_path = f"{sub_path}/{f}"
                    encoded_path = urllib.parse.quote(img_path)
                    download_url = f"{REPO_URL}/{encoded_path}"
                    
                    # Using HTML for controlled scaling in the Markdown table
                    preview = f'<img src="{img_path}" width="200" alt="{f}">'
                    download_link = f"**[💾 Download]({download_url})**"
                    
                    markdown.append(f"| {sub.capitalize()} | {preview} | {download_link}<br>`{f}` |")
        
        # Anchor link back to the specific 800x480 header
        markdown.append("\n[↑ Back to Top](#-800x480-screen-gallery)\n")
        markdown.append("---\n")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(markdown))
    print(f"Successfully generated {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_gallery()