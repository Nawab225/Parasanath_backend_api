from django.urls import path
from .views import *

urlpatterns = [
    # home folder________________________________________________________________________________________________________________

    path("hero/", HeroList.as_view()),
    path("about/", AboutList.as_view()),
    path("hist/",HisList.as_view()),
    # path("gallery/", GalleryList.as_view()),
    path("videos/", VideoGalleryList.as_view()),
    path("news/", NewsList.as_view()),
    path("event/", EventVedio.as_view()),
    # Gelllery folder________________________________________________________________________________________________________________
    path("photo/", All_Gellery_API.as_view()),
    path("vedio/",All_Vedio.as_view()), 

      # About =========================================================

    path('about_hill/', AboutHillList.as_view()),
    # path('about-hill/<int:pk>/', AboutHillDetail.as_view()),

    path('about_temple/', AboutTempleList.as_view()),
    # path('about-temple/<int:pk>/', AboutTempleDetail.as_view()),

    path('about_culture/', AboutCultureList.as_view()),
    # path('about-culture/<int:pk>/', AboutCultureDetail.as_view()),

    path('about_mission/', AboutMissionList.as_view()),
    # path('about-mission/<int:pk>/', AboutMissionDetail.as_view()),


    # History =========================================================

    path('history/', HistoryList.as_view()),
    # path('history/<int:pk>/', HistoryDetail.as_view()),


    # Religion =========================================================

    path('religion/', ReligionList.as_view()),
    path('santhal_jain/',Santhal_jainList.as_view()),
    # path('religion/<int:pk>/', ReligionDetail.as_view()),


    # Judicial =========================================================

    path('judicial/', JudicialList.as_view()),
    # path('judicial/<int:pk>/', JudicialDetail.as_view()),


    # Document =========================================================

    path('document/', DocumentList.as_view()),
    # path('document/<int:pk>/', DocumentDetail.as_view()),


    # Contact =========================================================

    path('contact/', ContactList.as_view()),
    # path('contact/<int:pk>/', ContactDetail.as_view()),

   
]