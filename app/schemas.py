from datetime import date
from typing import Literal
from pydantic import BaseModel


# Schema 1: Validation layer for State License extraction
class StateLicenseSchema(BaseModel):
    license_number: str
    issuing_state: Literal["CA", "TX", "NY"]
    expiration_date: date


# Schema 2: Validation layer for DEA Certificate extraction
class FullDeaCertificateSchema(BaseModel):
    dea_number: str
    registrant_name: str
    business_activity: Literal["PRACTITIONER", "MID-LEVEL PRACTITIONER"]
    schedules: list[Literal["I", "II", "III", "IV", "V"]]
    expiration_date: date