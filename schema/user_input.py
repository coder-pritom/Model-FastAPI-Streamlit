from pydantic import BaseModel,Field,computed_field
from typing import Annotated


class Student(BaseModel):
    name: Annotated[str, Field(...,description="Name",example = "Pritom")]
    cls: Annotated[int,Field(...,description="Class", example= 8)]
    study_hours: Annotated[float,Field(...,description="Studying hours", example= 6.5)]
    playing_hours: Annotated[float,Field(...,description="Playing hours", example= 3.2)]

    @computed_field
    @property
    def type(self) -> str:
        diff = abs(self.study_hours-self.playing_hours)
        if  diff>3:
            return "Excellent"
        elif diff >1:
            return "Average"
        else:
            return "Back Bencher"