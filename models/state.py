#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy imporrt Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Attribute that returns the list of city instances"""
        from models import storage
        from models.city import City
        city_instances = storage.all(City)
        return [city for city in city_instances.values() if city.state_id == self.id]
