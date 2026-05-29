from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=5, max_length=15)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(gt=18, le=80)
    years_experience: int = Field(gt=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(gt=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(gt=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_id(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        else:
            return self

    @model_validator(mode="after")
    def validate_captain(self):
        for crew in self.crew:
            if crew.rank == "commander" or crew.rank == "captain":
                return self
        return ValueError('Must have at least one Commander or Captain')

    @model_validator(mode="after")
    def validate_experience(self):
        iterator = 0
        for crew in self.crew:
            if crew.years_experience > 5:
                iterator += 1
        if iterator >= len(self.crew) / 2:
            return self
        else:
            return ValueError("Long missions (> 365 days) need \
50% experienced crew (5+ years)")

    @model_validator(mode="after")
    def validate_state(self):
        for crew in self.crew:
            if not crew.is_active:
                return ValueError("All crew members must be active")
        return self


if __name__ == '__main__':
    valid = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }

    valid_input = SpaceMission(**valid)
    