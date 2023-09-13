def faker_name(fake):
    return fake.name()

def faker_description(fake):
    return fake.sentence(30)

def faker_cover(fake):
    from io import BytesIO
    from PIL import Image
    from django.core.files.base import ContentFile

    image_file = BytesIO()
    image = Image.new("RGBA", size=(50, 50), color=(256, 0, 0))
    image.save(image_file, "png")
    image_file.seek(0)
    return ContentFile(image_file.read(), "test.png")

BookFaker = {
    'title': faker_name,
    'description': faker_description,
    'cover': faker_cover,
}
