from rest_framework import generics
from django_filters import rest_framework as filters

from models import Advertisement
from serializers import AdvertisementSerializer


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']


class AdvertisementList(generics.ListAPIView):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
