from .serializers import PartnersSerializer
from ..models import Partners
from rest_framework import generics


class PartnersList(generics.ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
