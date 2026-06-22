from app.database.base import Base
from app.database.session import engine

# Import models so SQLAlchemy knows they exist
from app.models.employee import Employee

Base.metadata.drop_all(bind= engine)
Base.metadata.create_all(bind=engine)