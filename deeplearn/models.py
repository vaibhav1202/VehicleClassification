from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_img(upload): 
      ext = upload.name[-4:]
      if not ext in ['.jpg', ".png", "jpeg"]:
        raise ValidationError(u'File type not supported!')    
      if upload.size > 1024*1024*2:
        raise ValidationError(u'File too big!')    

class deep(models.Model):
    img = models.ImageField(upload_to = "images\\", validators=[validate_img], null=True)
    class_names=models.CharField(max_length=100)
    def to_dict(self):
        return{
             "img":self.img
            }