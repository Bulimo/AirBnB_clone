from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Public class attributes:
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        super().__init__(*args, **kwargs)
