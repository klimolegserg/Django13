from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from models import Advertisement
from serializers import AdvertisementSerializer
from permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_at']


class AdvertisementFilter(filters.FilterSet):
    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']

    def __init__(self, data=None, queryset=None):
        super().__init__(data, queryset)
        self.action = None

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
