# Write your solution here:

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title   
        self.seasons = seasons
        self.genres = genres
        self.rates = ["no ratings"]
        self.avg_rate = 0

    def rate(self, rate: int):
        self.rates.append(rate)
        self.avg_rate = sum(self.rates[1:]) / (len(self.rates) -1)
        self.rates[0] = f"{len(self.rates)-1} ratings, average {self.avg_rate:.1f} points"
    
    def __str__(self) -> str:
        return (f"{self.title} ({self.seasons} seasons) \ngenres: {', '.join(self.genres)} \n{self.rates[0]}")


def minimum_grade(rating: float, series_list: list):
    min_grade_list = []

    for series in series_list:
        if series.avg_rate >= rating:
            min_grade_list.append(series)

    return min_grade_list


def includes_genre(genre: str, series_list: list):
    includes_genre_list = []

    for series in series_list:
        if genre in series.genres:
            includes_genre_list.append(series)
            
    return includes_genre_list






