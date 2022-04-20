from rest_framework import viewsets


from .models import Women
from .serialiazers import WomenSerializer


class WomenAPIView(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def list(self, request, *args, **kwargs):
        result = super().list(request, *args, **kwargs)
        return result


