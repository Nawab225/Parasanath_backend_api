from django.db import models
from ckeditor.fields import RichTextField

# Hero Section
class Hero(models.Model):
    image = models.ImageField(upload_to="hero/")

    def __str__(self):
        return f"Hero Image {self.id}"

# About Section
class About(models.Model):
    topTitle = models.CharField(max_length=100, default="About Us")
    title = models.CharField(max_length=200)
    description = models.TextField()
    subdescription = models.TextField(default="No description")
    

class AboutImages(models.Model):
    about = models.ForeignKey(
        About, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return f"{self.about.title} Image"


# History Section
class History(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="No description")
    description = models.TextField()
    subdescription = models.TextField(default="No description")
    image = models.ImageField(upload_to="Histye/",default="No description")


    def __str__(self):
        return self.title


# Video Gallery
class VideoGallery(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to="videos/")
    images=models.ImageField(upload_to='event_all/',default="No description")

    def __str__(self):
        return self.title


# News Section
class News(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="news_images/")
    youtube_link = models.URLField(unique=True, blank=True, null=True)
    news_link = models.URLField(default="No description")
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Event(models.Model):
    video = models.FileField(upload_to="videos/")
    
    def __str__(self):
        return f"Event video {self.id}"


# Gallery folder________________________________________________________________________________________________________________

class All_Gellery(models.Model):
    image = models.ImageField(upload_to="all_gellery_photo/")

    class Meta:
        verbose_name = "Gallery_Image"
        verbose_name_plural = "Gallery_Images"

    def __str__(self):
        return f"Gallery Image {self.id}"


class All_Video(models.Model):
    video = models.FileField(upload_to="all_video_video/")

    class Meta:
        verbose_name = "Gallery Video"
        verbose_name_plural = "Gallery Videos"

    def __str__(self):
        return f"Gallery Video {self.id}"
    

# About folder________________________________________________________________________________________________________________

class About_Hill(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField(default="No description")
    description2 = models.TextField(default="No description")
    description3 = models.TextField(default="No description")
    youtube_link = models.URLField(unique=True, blank=True, null=True)
    pdf = models.FileField(upload_to="about_pdf/")

    def __str__(self):
        return self.title

class About_Temple(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=True, null=True)
    
    # Yaha se unique=True hata diya hai taaki MySQL 1170 error na de
    description1 = models.TextField(
        default="No description",
        blank=True,
        null=True
    )

    description2 = models.TextField(
        default="No description",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="Temple/",
        unique=True,
        blank=True,
        null=True
    )

    # Multiple videos
    video1 = models.FileField(upload_to="Temple_videos/", blank=True, null=True)
    video2 = models.FileField(upload_to="Temple_videos/", blank=True, null=True)
    video3 = models.FileField(upload_to="Temple_videos/", blank=True, null=True)
    video4 = models.FileField(upload_to="Temple_videos/", blank=True, null=True)

    pdf = models.FileField(
        upload_to="about_pdf/",
        unique=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

class About_Culture(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField(default="No description")
    description2 = models.TextField(default="No description")
    description3 = models.TextField(default="No description")
    image = models.ImageField(upload_to="Culture/")
    pdf = models.FileField(upload_to="about_pdf/")

    def __str__(self):
        return self.title
    
class About_mission(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="Culture/")

    def __str__(self):
        return self.title
    

# History folder________________________________________________________________________________________________________________
    
class HistoryImage(models.Model):
    main_history = models.ForeignKey(
        'Main_History',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to="History/")

    def __str__(self):
        return self.main_history.title


class Main_History(models.Model):
    title = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField()
    paragraph4 = models.TextField()
    paragraph5 = models.TextField()
    pdf = models.FileField(upload_to="History_pdf/")

    def __str__(self):
        return self.title
    

# religion folder________________________________________________________________________________________________________________
    
class Religen(models.Model):
    title = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    image = models.ImageField(upload_to="religen/")
    
    def __str__(self):
        return self.title 
    

class Santhal_jain(models.Model):
    title = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField()
    paragraph3 = models.TextField()
    image = models.ImageField(upload_to="santhal_jain/")
    PDF = models.FileField(upload_to="santhal_jain/")
    
    def __str__(self):
        return self.title 
    
# court folder________________________________________________________________________________________________________________
    
class Judicial(models.Model):
    title = models.CharField(max_length=200, default="Judicial Title")
    paragraph1 = models.TextField(default="No description")
    PDF = models.FileField(upload_to="Judicial/")
    
    def __str__(self):
        return f"judicial {self.id}"
    

# Document folder________________________________________________________________________________________________________________
    
class Main_docoment(models.Model):
    title = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    pdf = models.FileField(upload_to="docoment_pdf/")

    def __str__(self):
        return self.title

# contact folder________________________________________________________________________________________________________________

class Contect(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default="Unknown")
    Email = models.EmailField(max_length=100)
    Address = models.CharField(max_length=200)
    dec = models.TextField()
   
    def __str__(self):
        return self.name