from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)

import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | EOFError:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"