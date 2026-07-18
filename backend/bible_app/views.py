from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .documents import ScriptureVerseDocument

class CleanSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"error": "Missing target query value"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Execute query matching operations across text inverted files
        search_results = ScriptureVerseDocument.search().query("match", verse_text=query)
        
        data = [
            {
                "book": hit.book_name,
                "chapter": hit.chapter_number,
                "verse": hit.verse_number,
                "text": hit.verse_text
            } for hit in search_results
        ]
        return Response(data, status=status.HTTP_200_OK)
