from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import ScriptureVerse

@registry.register_document
class ScriptureVerseDocument(Document):
    class Index:
        name = 'scriptures'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = ScriptureVerse
        fields = [
            'book_name',
            'chapter_number',
            'verse_number',
            'verse_text',
        ]
