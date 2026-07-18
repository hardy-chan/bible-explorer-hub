import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_core.settings')
django.setup()

from bible_app.models import ScriptureVerse

def run_text_ingestion():
    file_path = 'bible_data.json'
    if not os.path.exists(file_path):
        print(f"[ERROR] Source dataset file not found at {file_path}")
        return

    print("[INFO] Initiating data warehouse database ingestion streams...")

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        raw_data = json.load(file)
        
    verses_to_create = []
    
    # Process local multi-nested JSON array configurations
    for book in raw_data:
        book_name = book.get('name', 'Unknown')
        chapters = book.get('chapters', [])
        
        for chapter_idx, chapter in enumerate(chapters, start=1):
            for verse_idx, verse_text in enumerate(chapter, start=1):
                verses_to_create.append(
                    ScriptureVerse(
                        book_name=book_name,
                        chapter_number=chapter_idx,
                        verse_number=verse_idx,
                        verse_text=str(verse_text)
                    )
                )
        
    ScriptureVerse.objects.bulk_create(verses_to_create, ignore_conflicts=True)
    print(f"[SUCCESS] Successfully cataloged database text entries.")

if __name__ == '__main__':
    run_text_ingestion()
