from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(gt=0.0, le=10.0)
    duration_minutes: int = Field(gt=1, le=1440)
    witness_count: int = Field(gt=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_contact_id(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        else:
            return self

    @model_validator(mode="after")
    def validate_contact_type(self):
        if not isinstance(self.contact_type, ContactType):
            raise ValueError('Invalid Physical contact type')
        else:
            return self

    @model_validator(mode="after")
    def validate_telepathic(self):
        if self.witness_count < 3 and self.contact_type == \
                ContactType.telepathic:
            raise ValueError('Telepathic contact \
requires at least 3 witnesses')
        else:
            return self

    @model_validator(mode="after")
    def validate_signals(self):
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError('Strong signals (> 7.0) should include \
received messages')
        else:
            return self


if __name__ == '__main__':
    print("Alien Contact Log Validation")
    print("========================================")
    print("Valid contact report:")
    valid = {
        "contact_id": "AC_2024_001",
        "timestamp": '2006-06-29T23:45:32.300+00:00',
        "location": "rea 51, Nevada",
        "contact_type": ContactType.radio,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "'Greetings from Zeta Reticuli'"
    }
    data = AlienContact(**valid)
    print(f"ID: {data.contact_id}")
    print(f"Type: {data.contact_type.value}")
    print(f"Location: {data.location}")
    print(f"Signal: {data.signal_strength}/10")
    print(f"Duration: {data.duration_minutes} minutes")
    print(f"Witnesses: {data.witness_count}")
    print(f"Message: {data.message_received}")
    print("========================================")
    print("Valid contact report:")
    try:
        invalid = {
            "contact_id": "AC_2024_001",
            "timestamp": '2006-06-29T23:45:32.300+00:00',
            "location": "rea 51, Nevada",
            "contact_type": ContactType.telepathic,
            "signal_strength": 8.5,
            "duration_minutes": 45,
            "witness_count": 2,
            "message_received": "'Greetings from Zeta Reticuli'"
        }
        invalid_data = AlienContact(**invalid)
    except ValidationError as e:
        msg = e.errors()[0]["msg"].replace("Value error, ", "")
        print(msg)
