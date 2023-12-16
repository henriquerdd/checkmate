
class Board:

    def __init__(self) -> None:
        self._state = Board._build_initial_state()
        pass

    def __str__(self) -> str:
        pass
    
    @classmethod
    def _build_initial_state() -> list:
        return [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]