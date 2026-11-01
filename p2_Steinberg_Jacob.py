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

    def cost(self) -> float:
        monthly_fee = self.fee_schedule["student_monthly"]
        extra_vehicle_fee = self.fee_schedule["extra_vehicle"]
        return float(self.months * monthly_fee + (self.vehicles - 1) * extra_vehicle_fee)

    def __str__(self) -> str:
        return (
            f"Student: {self.owner} | Months: {self.months} | "
            f"Vehicles: {self.vehicles} | Cost: ${self.cost():.2f}"
        )

    def __repr__(self) -> str:
        return (
            f"StudentPermit({self.owner!r}, {self.months!r}, "
            f"{self.fee_schedule!r}, {self.vehicles!r})"
        )
