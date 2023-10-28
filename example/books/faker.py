from rest_framework_supertest import shortcuts

def faker_description(fake):
    return fake.sentence(30)

def faker_cover(fake):
    return fake.image(width=256, height=256)

BookFaker = {
    'title': shortcuts.unique_name,
    'description': faker_description,
    'cover': faker_cover,
}
