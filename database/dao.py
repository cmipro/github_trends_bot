from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from database.models import Base, Project


class ProjectDAO:
    """DAO for Project Model."""

    def __init__(self, database_path):
        self.engine = create_engine(database_path, echo=False)
        Base.metadata.create_all(bind=self.engine)

    def check_project_exists(self, name: str) -> bool:
        """Checking that the project is already in the database."""
        with Session(autoflush=False, bind=self.engine) as db:
            instance = db.execute(
                select(Project)
                .where(Project.name == name)  # type: ignore
            ).first()
        return True if instance else False

    def add_project(self, name: str) -> Project:
        """Add project."""
        with Session(autoflush=False, bind=self.engine) as db:
            instance = Project(name=name)
            db.add(instance)
            db.commit()
            db.refresh(instance)
        return instance
