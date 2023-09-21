#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ DBStorage class """

    __engine = None
    __session = None

    def __init__(self):
        """ initialize database """

        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict_cls = {}
        if cls is None:
            for class_name in [User, Place, State, City, Amenity, Review]:
                quey_on = self.__session.query(class_name)
                for obj in query_on:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    dict_cls[key] = obj
        else:
            if type(cls) == str:
                cls = eval(cls)
                quey_on = self.__session.query(cls)
                for obj in query_on:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    dict_cls[key] = obj
        return dict_cls

    def new(self, obj):
        """ add all obj of the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit or save all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create the current database sessio"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close_session(self):
        """close session"""
        self.__session.close()
