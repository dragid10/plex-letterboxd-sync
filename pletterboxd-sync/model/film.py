from dataclasses import dataclass


@dataclass
class Film:
    adult: bool
    clean_title: str  # /film/<title>[-<release_year>]
    id: int  # TMDB ID
    imdb_id: str  # IMDB ID
    release_year: str
    title: str
