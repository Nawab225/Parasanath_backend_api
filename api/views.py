from rest_framework import generics
from .models import *
from .serializers import *

class HeroList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class HisList(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


# class GalleryList(generics.ListAPIView):
#     queryset = Gallery.objects.all()
#     serializer_class = GallerySerializer


class VideoGalleryList(generics.ListAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class EventVedio(generics.ListAPIView):
    serializer_class =EventSerializer
    
    def get_queryset(self):
        limit=self.request.GET.get('limit')
        queryset = Event.objects.all()
        if limit:
            queryset=queryset[:int(limit)]
        return queryset



# Gelllery folder________________________________________________________________________________________________________________
class All_Gellery_API(generics.ListAPIView):
    serializer_class = All_gellerySerilizer

    def get_queryset(self):
        limit = self.request.GET.get("limit")

        queryset = All_Gellery.objects.all()

        if limit:
            queryset = queryset[:int(limit)]

        return queryset

class All_Vedio(generics.ListAPIView):
    serializer_class = All_VedioSerilizer

    def get_queryset(self):
        limit = self.request.GET.get("limit")

        queryset = All_Video.objects.all()

        if limit:
            queryset = queryset[:int(limit)]

        return queryset

# About Folder =====================================================================

class AboutHillList(generics.ListCreateAPIView):
    queryset = About_Hill.objects.all()
    serializer_class = About_hill_Serilizer


# class AboutHillDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = About_Hill.objects.all()
#     serializer_class = About_hill_Serilizer


class AboutTempleList(generics.ListCreateAPIView):
    queryset = About_Temple.objects.all()
    serializer_class = About_Temple_Serilizer


# class AboutTempleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = About_Temple.objects.all()
#     serializer_class = About_Temple_Serilizer


class AboutCultureList(generics.ListCreateAPIView):
    queryset = About_Culture.objects.all()
    serializer_class = About_Culture_Serilizer


# class AboutCultureDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = About_Culture.objects.all()
#     serializer_class = About_Culture_Serilizer


class AboutMissionList(generics.ListCreateAPIView):
    queryset = About_mission.objects.all()
    serializer_class = About_Mission_Serilizer


# class AboutMissionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = About_mission.objects.all()
#     serializer_class = About_Mission_Serilizer


# History Folder =====================================================================

class HistoryList(generics.ListCreateAPIView):
    queryset = Main_History.objects.all()
    serializer_class = Histroy_Serilizer


# class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Main_History.objects.all()
#     serializer_class = Histroy_Serilizer


# Religion Folder =====================================================================

class ReligionList(generics.ListCreateAPIView):
    queryset = Religen.objects.all()
    serializer_class = Religen_Serilizer


class Santhal_jainList(generics.ListCreateAPIView):
    queryset = Santhal_jain.objects.all()
    serializer_class = Santhal_jain_Serilizer



# class ReligionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Religen.objects.all()
#     serializer_class = Religen_Serilizer


# Court Folder =====================================================================

class JudicialList(generics.ListCreateAPIView):
    queryset = Judicial.objects.all()
    serializer_class = Judicial_Serilizer


# class JudicialDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Judicial.objects.all()
#     serializer_class = Judicial_Serilizer


# Document Folder =====================================================================

class DocumentList(generics.ListCreateAPIView):
    queryset = Main_docoment.objects.all()
    serializer_class = main_docoment_Serilizer


# class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Main_docoment.objects.all()
#     serializer_class = main_docoment_Serilizer


# Contact Folder =====================================================================

class ContactList(generics.ListCreateAPIView):
    queryset = Contect.objects.all()
    serializer_class = Contect_Serilizer


# class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Contect.objects.all()
#     serializer_class = Contect_Serilizer