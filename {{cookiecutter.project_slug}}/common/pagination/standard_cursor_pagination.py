from rest_framework.pagination import CursorPagination
from rest_framework.response import Response

class StandardCursorPagination(CursorPagination):
    page_size = 20
    ordering = ("-created_at", "-id")

    def get_paginated_response(self, data):
        return Response({
            "status": "success",
            "pagination": {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'results': data,
        })
