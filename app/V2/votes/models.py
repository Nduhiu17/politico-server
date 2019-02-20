cursor = Database.connect_to_db()


@dataclass
class Vote:
    """Class that models vote"""
    id: str
