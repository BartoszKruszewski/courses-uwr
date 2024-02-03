import argparse
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models import Base, Artist, Song, Album
from datetime import date

parser = argparse.ArgumentParser(description='Artists and songs database.')
subparsers = parser.add_subparsers(dest='tables')

songs_parser = subparsers.add_parser('song')
songs_parser.add_argument('--add', action='store_true')
songs_parser.add_argument('--print', action='store_true')
songs_parser.add_argument('--update', action='store_true')
songs_parser.add_argument('--id')
songs_parser.add_argument('--title')
songs_parser.add_argument('--album')
songs_parser.add_argument('--date')
songs_parser.add_argument('--artist')

album_parser = subparsers.add_parser('album')
album_parser.add_argument('--add', action='store_true')
album_parser.add_argument('--print', action='store_true')
album_parser.add_argument('--update', action='store_true')
album_parser.add_argument('--id')
album_parser.add_argument('--title')
album_parser.add_argument('--date')
album_parser.add_argument('--artist')

artist_parser = subparsers.add_parser('artist')
artist_parser.add_argument('--add', action='store_true')
artist_parser.add_argument('--print', action='store_true')
artist_parser.add_argument('--update', action='store_true')
artist_parser.add_argument('--action', required=True)
artist_parser.add_argument('--id')
artist_parser.add_argument('--name')

args = parser.parse_args()

engine = create_engine('sqlite:///base.db', echo = False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if args.add:
    if args.tables == 'song':
        if args.title:
            if args.album:
                session.add(Song(
                    title = args.title,
                    album_id = session.query(Album)
                    .filter_by(title = args.album).first().id
                ))
            else:
                print('--album is required to add new song.')
        else:
            print('--title is required to add new song.')
    elif args.tables == 'album':
        if args.title:
            if args.date:
                if args.artist:
                    session.add(Album(
                        title = args.title,
                        date = date.fromisoformat(args.date),
                        artist_id = session.query(Artist)
                        .filter_by(name = args.artist).first().id
                    ))
                else:
                    print('--artist is required to add new album.')
            else:
                print('--date is required to add new album.')
        else:
            print('--title is required to add new album.')
    elif args.tables == 'artist':
        if args.name:
            session.add(Artist(name = args.name))
        else:
            print('--name is required to add new artist.')
elif args.update:
    if args.tables == 'song':
        song = session.query(Song).filter_by(id=args.id).first()
        if args.title:
            song.title = args.title
            print(f'Title has been modified to {args.title}')
        if args.album:
            song.album_id = session.query(Album).filter_by(title = args.album).first().id
            print(f'Album has been modified to {args.album}')
    if args.tables == 'album':
        song = session.query(Album).filter_by(id=args.id).first()
        if args.title:
            song.title = args.title
            print(f'Title has been modified to {args.title}')
        if args.date:
            song.date = args.date
            print(f'Date has been modified to {args.date}')
        if args.artist:
            song.artist = args.artist
            print(f'Artist has been modified to {args.artist}')
    elif args.tables == 'artist':
        song = session.query(Artist).filter_by(id=args.id).first()
        if args.name:
            song.name = args.name
            print(f'Name has been modified to {args.name}')
elif args.print:
    if args.tables == 'song':
        data = session.query(Song).all()
        if args.id:
            data = filter(lambda x: x.id == int(args.id), data)
        if args.title:
            data = filter(lambda x: x.title == args.title, data)
        if args.date:
            album = session.query(Album) \
            .filter_by(date = date.fromisoformat(args.date)).first()
            data = filter(lambda x: x.album == album, data)
        if args.album:
            album = session.query(Album) \
            .filter_by(title = args.album).first()
            data = filter(lambda x: x.album == args.album, data)
        if args.artist:
            albums = session.query(Album) \
            .filter_by(artist = args.artist)
            data = filter(lambda x: x.album in albums, data)
        for row in data:
            print(f'{row.album.artist.name} [{row.album.title}] - {row.title} : {row.album.date}')
    elif args.tables == 'album':
        data = session.query(Album).all()
        if args.id:
            data = filter(lambda x: x.id == int(args.id), data)
        if args.title:
            data = filter(lambda x: x.title == args.title, data)
        if args.date:
            data = filter(lambda x: x.date == args.date, data)
        if args.artist:
            artist = session.query(Artist) \
            .filter_by(name = args.artist).first()
            data = filter(lambda x: x.artist == artist, data)
        for row in data:
            print(f'{row.artist.name} - {row.title} : {row.date}')
    elif args.tables == 'artist':
        data = session.query(Artist).all()
        if args.id:
            data = filter(lambda x: x.id == int(args.id), data)
        for row in data:
            print(f'{row.name}')

session.commit()
