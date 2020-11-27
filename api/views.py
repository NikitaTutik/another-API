from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LanguageSerializer
from .models import Language
from rest_framework.permissions import IsAuthenticated


class LanguageView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class DetailView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        language = Language.objects.get(id=id)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def put(self, request, id):
        language = Language.objects.get(id=id)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        language = Language.objects.get(id=id)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





