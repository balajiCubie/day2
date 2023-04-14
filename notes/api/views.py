# from  django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def  getRoutes(request):
        data=[
            {   
                "endpoint": "/notes",
                "method": "GET",
                "body": None,
                "description": "Returns a list of notes"
            },
            {
                "endpoint": "/notes/id",
                "method": "GET",
                "body": None,
                "description": "Returns a single note"
            },
            {
                "endpoint": "/notes/create",
                "method": "POST",
                "body": {"title": "String", "content": "String", "category": "String"},
                "description": "Create a new note"
            },
        ]
        return  Response(data)

