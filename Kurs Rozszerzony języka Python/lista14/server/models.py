"""
Database Models

This module defines SQLAlchemy models for the Artist, Album, and Song entities.
Each model includes data validation using the @validates decorator.

Dependencies:
    - datetime: for handling date conversions
    - sqlalchemy: for database modeling
    - flask_sqlalchemy: for integrating SQLAlchemy with Flask

"""

import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, validates, Mapped
from flask_sqlalchemy import SQLAlchemy
from typing import Dict, Union, List

db = SQLAlchemy()


class Album(db.Model):
    """
    Album Model

    Represents an album in the database.

    Attributes:
        id (int): Primary key, autoincremented.
        title (str): Title of the album, not nullable.
        date (datetime.date): Release date of the album, not nullable.
        artist_id (int): Foreign key referencing the artist table.
        artist (List[Artist]): Relationship to the Artist model.
        songs (List[Song]): Relationship to the Song model.

    Methods:
        validate_date(self, key, new_date): Validation method for the date attribute.
        serialize(self): Converts the model instance to a dictionary for JSON serialization.

    """
    __tablename__ = 'album'

    id: Column[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Column[str] = Column(String, nullable=False)
    date: Column[datetime.date] = Column(Date, nullable=False)
    artist_id: Column[int] = Column(Integer, ForeignKey('artist.id'))
    artist: Mapped[List["Artist"]] = relationship(
        'Artist', back_populates='albums')
    songs: Mapped[List["Song"]] = relationship(
        'Song', back_populates='album')

    @validates("date")
    def validate_date(
            self, key: int, new_date: datetime.date) -> datetime.date:
        """
        Validate the date attribute to ensure it is not in the future.

        Args:
            key (int): Column key.
            new_date (datetime.date): New date value.

        Returns:
            datetime.date: Validated date value.

        Raises:
            ValueError: If the date is in the future.

        """
        if new_date > datetime.date.today():
            raise ValueError("Release date should be in the past!")
        return new_date

    def serialize(self) -> Dict[str, Union[Column[int], Column[str], str]]:
        """
        Convert the model instance to a dictionary for JSON serialization.

        Returns:
            Dict[str, Union[Column[int], Column[str], str]]: Serialized data.

        """
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date.isoformat(),
            'artist_id': self.artist_id
        }


class Song(db.Model):
    """
    Song Model

    Represents a song in the database.

    Attributes:
        id (int): Primary key, autoincremented.
        title (str): Title of the song, not nullable.
        album_id (int): Foreign key referencing the album table.
        album (List[Album]): Relationship to the Album model.
        artist_id (int): Foreign key referencing the artist table.
        artist (List[Artist]): Relationship to the Artist model.

    Methods:
        validate_title(self, key, title): Validation method for the title attribute.
        serialize(self): Converts the model instance to a dictionary for JSON serialization.

    """
    __tablename__ = 'song'

    id: Column[int] = Column(
        Integer, primary_key=True, autoincrement=True)
    title: Column[str] = Column(String, nullable=False)
    album_id: Column[int] = Column(Integer, ForeignKey('album.id'))
    album: Mapped[List[Album]] = relationship(
        'Album', back_populates='songs')
    artist_id: Column[int] = Column(Integer, ForeignKey('artist.id'))
    artist: Mapped[List["Artist"]] = relationship(
        'Artist', back_populates='songs')

    @validates("title")
    def validate_title(self, key: int, title: str) -> str:
        """
        Validate the title attribute to ensure it is not too long.

        Args:
            key (int): Column key.
            title (str): Title value.

        Returns:
            str: Validated title value.

        Raises:
            ValueError: If the title is too long.

        """
        if len(title) > 200:
            raise ValueError("Title too long!")
        return title

    def serialize(self) -> Dict[str, Union[Column[int], Column[str]]]:
        """
        Convert the model instance to a dictionary for JSON serialization.

        Returns:
            Dict[str, Union[Column[int], Column[str]]]: Serialized data.

        """
        return {
            'id': self.id,
            'title': self.title,
            'artist_id': self.artist_id,
            'album_id': self.album_id
        }


class Artist(db.Model):
    """
    Artist Model

    Represents an artist in the database.

    Attributes:
        id (int): Primary key, autoincremented.
        name (str): Name of the artist, not nullable.
        albums (List[Album]): Relationship to the Album model.
        songs (List[Song]): Relationship to the Song model.

    Methods:
        validate_name(self, key, name): Validation method for the name attribute.
        serialize(self): Converts the model instance to a dictionary for JSON serialization.

    """
    __tablename__ = 'artist'

    id: Column[int] = Column(
        Integer, primary_key=True, autoincrement=True)
    name: Column[str] = Column(String, nullable=False)
    albums: Mapped[List[Album]] = relationship(
        'Album', back_populates='artist')
    songs: Mapped[List[Song]] = relationship(
        'Song', back_populates='artist')

    @validates("name")
    def validate_name(self, key: int, name: str) -> str:
        """
        Validate the name attribute to ensure it is not too short.

        Args:
            key (int): Column key.
            name (str): Name value.

        Returns:
            str: Validated name value.

        Raises:
            ValueError: If the name is too short.

        """
        if len(name) < 2:
            raise ValueError("Name is too short!")
        return name

    def serialize(self) -> Dict[str, Union[Column[int], Column[str]]]:
        """
        Convert the model instance to a dictionary for JSON serialization.

        Returns:
            Dict[str, Union[Column[int], Column[str]]]: Serialized data.

        """
        return {
            'id': self.id,
            'name': self.name
        }


models: Dict[str, type] = {
    'artist': Artist,
    'album': Album,
    'song': Song,
}
