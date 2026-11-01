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
            f"{self.fee_schedule!r})"
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


class FacultyPermint(ParkingPermit):
    def __init__(
        self,
        owner: str,
        months: int,
        fee_schedule: dict[str, float],
        garage_access: bool,
    ) -> None:
        super().__init__(owner, months, fee_schedule)
        if not isinstance(garage_access, bool):
            raise TypeError("Garage access must be True or False.")
        self.garage_access = garage_access

    def cost(self) -> float:
        monthly_fee = self.fee_schedule["faculty_monthly"]
        garage_fee = self.fee_schedle["garage_monthly"] if self.garage_access else 0
        return float(self.months * (monthly_fee + garage_fee))

    def __str__(self) -> str:
        garage = "Yes" if self.garage_access else "No"
        return (
            f"FacultyPermit({self.owner!r}, {self.months!r}, "
            f"{self.fee_schedule!r}, {self.garage_access!r})"
        )

def summarize_list(permits: list[ParkingPermit]) -> float:
    """Print the owner and cost of every permit; return total revenue.

    Parameter: permits is a list containing student and faculty permits.
    Postcondition: each permit is printed using its __str__ method.
    """
    total = 0.0
    for permit in permits:
        print(permit)
        total += permit.cost()
    return total


def main() -> None:
    """Demonstrate the classes, their representations, and revenue totals."""
    # Prices are supplied through this dictionary, not inside cost methods.
    fees = {
        "student_monthly": 25.0,
        "extra_vehicle": 10.0,
        "faculty_monthly": 40.0,
        "garage_monthly": 15.0,
    }

    permits: list[ParkingPermit] = [
        StudentPermit("Alex Carter", 4, fees, 2),
        StudentPermit("Taylor Lee", 2, fees, 1),
        FacultyPermit("Dr. Morgan", 3, fees, True),
        FacultyPermit("Prof. Rivera", 1, fees, False),
    ]

    student_id = input("Enter your FAU student ID for the screenshot: ").strip()
    print(f"\nFAU Student ID: {student_id or '[not entered]'}")

    print("\nObject representations (__repr__):")
    for permit in permits:
        print(repr(permit))

    print("\nParking permits and calculated costs (__str__):")
    revenue = summarize_list(permits)
    print(f"\nTotal revenue: ${revenue:.2f}")


if __name__ == "__main__":
    main()
