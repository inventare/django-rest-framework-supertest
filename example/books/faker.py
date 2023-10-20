from rest_framework_supertest import shotcuts

def faker_description(fake):
    return fake.sentence(30)

def faker_cover(fake):
    return fake.image(width=256, height=256)

BookFaker = {
    'title': shotcuts.unique_name,
    'description': faker_description,
    'cover': faker_cover,
}
