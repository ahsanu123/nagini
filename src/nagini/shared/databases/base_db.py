from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class BaseDb(DeclarativeBase, MappedAsDataclass):
    pass
