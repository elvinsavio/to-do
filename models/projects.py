

def create_new_project(name: str, description: str = None):
    from application import master_database
    master_database.create_project(name=name, description=description)


