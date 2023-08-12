from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Public class attributes:
        state_id: string - empty string (State.id)
        name: string - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        super().__init__(*args, **kwargs)
    