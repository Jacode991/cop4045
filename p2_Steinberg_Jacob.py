# p2_Steinberg_Jacob.py
# Jacob Steinberg
# z23812823
# COP 4045 - Python Programming
# Homework 3 - Problem 2

class ParkingPermit:
    def __init__(
        self, owner: str, months: int, fee_schedule: dict[str, float]
    ) -> None:
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner must be a nonempty name.")
        if type(months) is not int or months <= 0:
            raise ValueError("Months must be a positive integer.")
        if not isinstance(fee_schedule, dict):
            raise TypeError("Fee schedule ,ust be a dictionary.")

        self.owner = owner
        self.months = months
        self.fee_schedule = fee_schedule.copy()

    def cost(self) -> float:
        raise NotImplementedError("Use a student of faculty permit.")

    def __str__(self) -> str:
        return f"Parking permit for {self.owner} ({self.months} months)"

    def __repr__(self) -> str:
        return (
            f"ParkingPermit({self.owner!r}, {self.months!r}, "
            f"{self.fee_schedule!r}
        )


class StudentPermit(ParkingPermit):
    def __init__(
        self,
        owner: str,
        months: int,
        fee_schedule: dict[str,float],
        vehicles: int,
    ) -> None:
        super().__init__(owner, months, fee_schedule)
        if type(vehicles) is not int or vehicles <= 0:
            raise ValueError("Vehicles must be a positive integer.")
        self.vehicles = vehicles
