class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message




def data_processing(**data: dict):
    first_cup = 1930
    last_cup = 2022
    data_first_cup = 0

    data_first_cup = int(data["first_cup"][:4])

    year_cups = data_first_cup - first_cup
    
    all_cups = (last_cup - data_first_cup) / 4

    if data["titles"] < 0:
        raise NegativeTitlesError(f"titles cannot be negative")

    if data_first_cup < first_cup or year_cups % 4 != 0:
         raise InvalidYearCupError("there was no world cup this year")

    if data["titles"] > all_cups:

        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
