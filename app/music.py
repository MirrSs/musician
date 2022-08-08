from dataclasses import dataclass
from pydub import AudioSegment
from dataclasses import dataclass

@dataclass
class Music:
    song:AudioSegment
    files:list