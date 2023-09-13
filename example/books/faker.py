def faker_name(fake):
    return fake.name()

def faker_description(fake):
    return fake.sentence(30)

def faker_cover(fake):
    return fake.image(width=256, height=256)

BookFaker = {
    'title': faker_name,
    'description': faker_description,
    'cover': faker_cover,
}
