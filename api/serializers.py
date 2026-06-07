from rest_framework import serializers
from .models import *

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"


class AboutImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutImages
        fields=['image']

class AboutSerializer(serializers.ModelSerializer):
    images=AboutImagesSerializer(many=True)
    class Meta:
        model = About
        fields = "__all__"








class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


# class GallerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gallery
#         fields = "__all__"


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields= "__all__"


# Gelllery folder________________________________________________________________________________________________________________
class All_gellerySerilizer(serializers.ModelSerializer):
    class Meta:
        model=All_Gellery
        fields = "__all__"

class All_VedioSerilizer(serializers.ModelSerializer):
    class Meta:
        model=All_Video
        fields = "__all__"



# About folder________________________________________________________________________________________________________________

class About_hill_Serilizer(serializers.ModelSerializer):
     class Meta:
        model=About_Hill
        fields = "__all__"


class About_Temple_Serilizer(serializers.ModelSerializer):
     class Meta:
        model=About_Temple
        fields = "__all__"


class About_Culture_Serilizer(serializers.ModelSerializer):
     class Meta:
        model=About_Culture
        fields = "__all__"

class About_Mission_Serilizer(serializers.ModelSerializer):
     class Meta:
        model=About_mission
        fields = "__all__"


    
# History folder________________________________________________________________________________________________________________
  

# serializers.py

class HistoryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoryImage
        fields = ['image']


class Histroy_Serilizer(serializers.ModelSerializer):

    images = HistoryImageSerializer(many=True)

    class Meta:
        model = Main_History
        fields = '__all__'
# religen folder________________________________________________________________________________________________________________

class Religen_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Religen
        fields = "__all__"


class Santhal_jain_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Santhal_jain
        fields="__all__"

# court folder________________________________________________________________________________________________________________

class Judicial_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Judicial
        fields = "__all__"


# Docoment folder________________________________________________________________________________________________________________

class main_docoment_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Main_docoment
        fields = "__all__"

class Contect_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Contect
        fields = "__all__"
