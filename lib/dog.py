from models import Dog

def create_table(base, engine):
    
    base.metadata.create_all(engine)

def save(session, dog):
    
    session.add(dog)
    session.commit()

def get_all(session):
    
    query = session.query(Dog)
    all_dogs = query.all()
    return all_dogs

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    dog = session.query(Dog).filter(Dog.id == id).first()
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()