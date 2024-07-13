class Series:
    def __init__(self, number, series_type="standard"):
        """
        A series of masterchef
        :param number: the
        """
        self.number = number
        self.series_type = series_type


class Episode:
    def __init__(self, series: Series, number: int):
        """
        An episode of masterchef
        :param series: an associated Series
        :param number: the episode number
        """

        self.series = series
        self.number = number


class Cook:
    def __init__(self, round_type: str, elimination: bool):
        """
        A cooking challenge within an episode of MasterChef

        type
            signature, invention, guestjudges, unknown
        elimination
            were contestants eliminated after this round?
        """

        self.round_type = round_type
        self.elimination = elimination
