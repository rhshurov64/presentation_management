from django.db import models
from django.core.exceptions import ValidationError


class PresentationFile(models.Model):
    """This model is responsible to store the presentation files"""

    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to="presentation_files/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Presentation File"
        verbose_name_plural = "Presentation Files"

    def save(self, *args, **kwargs):
        ppt_extensions = ["ppt", "pptx", "pot", "potx", "pps", "ppsx"]
        file_ext = self.file.name.split(".")[-1]
        if file_ext not in ppt_extensions:
            raise ValidationError("This Field Only Support PPT File!")
        super().save(*args, **kwargs)
