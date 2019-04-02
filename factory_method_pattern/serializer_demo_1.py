import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format=format)
        return serializer(song)


def get_serializer(format):
    if format == "JSON":
        return _serialize_to_json
    elif format == "XML":
        return _serialize_to_xml
    else:
        raise ValueError(format)


def _serialize_to_json(song):
    song_info = {"id": song.song_id, "title": song.title, "artist": song.artist}
    return json.dumps(song_info)


def _serialize_to_xml(song):
    song_info = et.Element("song", attrib={"id": song.song_id})
    title = et.SubElement(song_info, "title")
    title.text = song.title
    artist = et.SubElement(song_info, "artist")
    artist.text = song.artist
    return et.tostring(song_info, encoding="unicode")
