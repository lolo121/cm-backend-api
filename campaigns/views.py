from django.shortcuts import render
from rest_framework import generics, response
from .models import Campaign
from .serializers import CampaignSerializer,SubscriberSerializer
# Create your views here.


class CampaignListAPIView(generics.ListAPIView):
    serializer_class=CampaignSerializer
    def get_queryset(self):
        return Campaign.objects.all()


class CampaignDetailAPIView(generics.GenericAPIView):
    serializer_class=CampaignSerializer
    def get(self, request, slug):
        query_set = Campaign.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)


class SubscribeToCampaignAPIView(generics.CreateAPIView):
    serializer_class=SubscriberSerializer
    def get_queryset(self):
        return Subcriber.objects.all()