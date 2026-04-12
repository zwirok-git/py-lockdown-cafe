import datetime


from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def success_message(self) -> str:
        return f"Welcome to {self.__name}"

    def visit_cafe(self, visitor: dict) -> None:
        vaccine_date = visitor.get("vaccine")

        if vaccine_date is None:
            raise NotVaccinatedError("Should be vaccinated")
        if vaccine_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError("Should be wearing a mask")

        print(self.success_message)
