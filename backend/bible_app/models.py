from django.db import models

class ScriptureVerse(models.Model):
    book_name = models.CharField(max_length=100, db_index=True)
    chapter_number = models.IntegerField()
    verse_number = models.IntegerField()
    verse_text = models.TextField()

    class Meta:
        unique_together = ('book_name', 'chapter_number', 'verse_number')

    def __str__(self):
        return f"{self.book_name} {self.chapter_number}:{self.verse_number}"
