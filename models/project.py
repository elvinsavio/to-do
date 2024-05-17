


def delete_project(name: str | None = None): 
    """
        Deletes a project

        args:
            name: name of project to delete

    """
    if name is None or name == "":
        return ("err", "Could not delete project")
