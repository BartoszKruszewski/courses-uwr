from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, validates
from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class Artist(db.Model):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    albums = relationship('Album', back_populates='artist')
    songs = relationship('Song', back_populates='artist')

    @validates("name")
    def validate_name(self, key, name):
        if len(name) < 2:
            raise ValueError("Name is too short!")
        return name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Album(db.Model):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.id'))
    artist = relationship('Artist', back_populates='albums')
    songs = relationship('Song', back_populates='album')

    @validates("date")
    def validate_date(self, key, new_date):
        if new_date > date.today():
            raise ValueError("Release date should be in the past!")
        return new_date

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': date.isoformat(self.date),
            'artist_id': self.artist_id
        }


class Song(db.Model):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    album_id = Column(Integer, ForeignKey('album.id'))
    album = relationship('Album', back_populates='songs')
    artist_id = Column(Integer, ForeignKey('artist.id'))
    artist = relationship('Artist', back_populates='songs')

    @validates("title")
    def validate_title(self, key, title):
        if len(title) > 200:
            raise ValueError("Title too long!")
        return title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist_id': self.artist_id,
            'album_id': self.album_id
        }


models = {
    'artist': Artist,
    'album': Album,
    'song': Song,
}
