def faker_name(fake):
    return fake.name()

def faker_description(fake):
    return fake.sentence(30)

BookFaker = {
    'title': faker_name,
    'description': faker_description,
}