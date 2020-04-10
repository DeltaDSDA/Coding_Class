from rest_framework import viewsets, serializers
from rest_framework.response import Response

from .models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'nickname', 'level', 'is_active', 'is_admin', 'is_superuser', 'is_staff')

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

'''
    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)
'''
