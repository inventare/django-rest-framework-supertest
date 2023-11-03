from django.db import models


class ImageModel(models.Model):
    """Define a Model to test setting image field."""

    field = models.ImageField()

    def __str__(self):
        """Return a representation string of the model."""
        return str(self.field)

class FileModel(models.Model):
    """Define a Model to test setting file field."""

    field = models.FileField()

    def __str__(self):
        """Return a representation string of the model."""
        return str(self.field)
