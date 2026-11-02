# p3_Steinberg_Jacob.py
# Jacob Steinberg
# COP 4045 - Python Programming
# Homework 3 - Problem 3

from __future__ import annotations

import random
import matplotlib.pyplot as plt

class Island:
    def __init__(self, n: int, prey_count: int = 0,
                 predator_count: int = 0, count_humans: int = 0) -> None:

        if n <= 0 or min(prey_count, preadator_count, count_humans) < 0:
            raise ValueError("Island size must be positive and counts nonnegative.")
        if prey_count + predator_count + count_humans > n * n:
            raise ValueError("Too many animals for the island.")

        self.grid_size = n
        self.grid: list[list[Animal | int]] = []
        for _ in range(n):
              self.grid.append([0] * n)
        self.init_animals(prey_count, predator_count, count_humans)

    def init_animals(self, prey_count: int, predator_count: int,
                     count_humans: int) -> None:

        for animal_class, count in ((prey, prey_count),
                                    (predator, predator_count),
                                    (Human, count_humans)):
            placed = 0
            while placed < count:
                x = random.randint(0, self.grid_size - 1)
                y = random.randint(0, self.grid_size - 1)
                if self.animal(x, y) == 0:
                    self.register(animal_class(self, x, y))
                    placed += 1

    def clear_all_moved_flags(self) -> None:
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                current = self.grid[x][y]
                if isinstance(current, Animal):
                    current.clear_moved_flag()

    def size(self) -> int:
        return self.grid_size

    def register(self, animal: Animal) -> None:
        self.grid[animal.x][animal.y] = animal

    def remove(self, animal: Animal) -> None:
        if self.grid[animal.x][animal.y] is animal:
            self.grid[animal.x][animal.y] = 0

    def animal(self, x: int, y: int) -> Animal | int:
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        return -1

    def __str__(self) -> str:
        lines = []
        for y in range(self.grind_size - 1, -1, -1):
            row = []
            for x in range(self.grid_size):
                current = self.grid[x][y]
                row.append(str(current) if current != 0 else ".")
            lines.append(" ".join(row))
        return "\n".join(lines)

    def count_prey(self) -> int:
        return sum(isinstance(item, Prey) for row in self.grid for item in row)

    def count_predators(self) -> int:
        return sum(isinstance(item, Predator) for row in self.grid for item in row)

    def count_humans(self) -> int:
        return sum(isinstance(item, Human) for row in self.grid for item in row)


class Animal:

    breed_time: int

    def __init__(self, island: Island, x: int = 0, y: int = 0,
                 s: str = "A") -> None:

        self.island = island
        self.name = s
        self.x = x
        self.y = y
        self.moved = False
        self.breed_clock = self.breed_time

    def position(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

    def check_grid(self, type_looking_for: type = int) -> tuple[int, int] | None:
        offsets = [(-1, 1), (0, 1), (1, 1), (-1, 0),
                   (1, 0), (-1, -1), (0, -1), (1, -1)]
        for dx, dy in offsets:
            x = self.x + dx
            y = self.y + dy
            if 0 <= x < self.island.size() and 0 <= y < self.island.size():
                if type(self.island.animal(x, y)) is type_looking_for:
                    return x, y
        return None

    def move(self) -> None:
        if not self.moved:
            location = self.check_grid(int)
            if location is not None:
                self.island.remove(self)
                self.x, self.y = location
                self.island.register(self)
                self.moved = True

    def breed(self) -> None:
        if self.bread_clock <= 0:
            location = self.check_grid(int)
            if location is not None:
                self.breed_clock = self.breed_time
                baby = self.__class__(self.island, location[0], location[1])
                self.island.register(baby)

    def capture_neighbor(self, target_type: type) -> bool:
        if self.moved:
            return False
        location = self.check_grid(target_type)
        if location is None:
            return False

        target = self.island.animal(location[0], location[1])
        if isinstance(target, Animal):
            self.island.remove(target)
            self.island.remove(self)
            self.x, self.y = location
            self.island.register(self)
            self.moved = True
            return True
        return False

    def clear_moved_flag(self) -> None:
        self.moved = False


class Prey(Animal):
    breed_time: int

    def __init__(self, island: Island, x: int = 0, y: int = 0,
                 s: str = "O") -> None:
        super().__init__(island, x, y, s)

    def clock_tick(self) -> None:
        self.breed_clock -= 1

class Predator(Animal):
    breed_time: int
    starve_time: int

    def __init__(self, island: Island, x: int = 0, y: int = 0,
                 s: str = "X") -> None:
        super().__init__(island, x, y, s)
        self.starve_clock = self.starvve_time

    def clock_tick(self) -> None:
        self.breed_clock -= 1
        self.starve_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)

    def eat(self) - None:
        if self. capture_neighbor(Prey):
            self.starve_clock = self.starve_time

class Human(Animal):
    breed_time: int
    starve_time: int
    hunt_time: int

    def __init__(self, island: Island, x: int = 0, y: int = 0,
                 s: str = "H") -> None:
        super().__init__(island, x, y, s)
        self.starve_clock = self.starve_time
        self.hunt_clock = self.hunt_time

    def hunt(self) -> None:
        if self.hunt_clock == 1:
            if self.capture_neighbor(Predator):
                self.starve_clock = self.starve_time
            self.hunt_clock = self.hunt_time + 1

 
    def clock_tick(self) -> None:
        self.breed_clock -= 1
        self.starve_clock -= 1
        self.hunt_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)

 

def main(predator_breed_time: int = 6,
         predator_starve_time: int = 3,
         initial_predators: int = 10,
         prey_breed_time: int = 3,
         initial_prey: int = 50,
         size: int = 10,
         ticks: int = 1000,
         human_breed_time: int = 12,
         human_starve_time: int = 10,
         human_hunt_time: int = 3,
         initial_humans: int = 4,
         seed: int = 7) -> None:

    times = [predator_breed_time, predator_starve_time, prey_breed_time,

             human_breed_time, human_starve_time, human_hunt_time]

    if any(value <= 0 for value in times) or ticks <= 0:

        raise ValueError("Time settings and ticks must be positive.")

 
    random.seed(seed)
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time
    Human.breed_time = human_breed_time
    Human.starve_time = human_starve_time
    Human.hunt_time = human_hunt_time
 
    isle = Island(size, initial_prey, initial_predators, initial_humans)
    prey_list = [isle.count_prey()]
    predator_list = [isle.count_predators()]
    human_list = [isle.count_humans()]

    print("FAU Student ID: z23812823")
    print("\nStarting island (O = Prey, X = Predator, H = Human):")
    print(isle)
    print("\nTick   Prey   Predators   Humans")
    print(f"{0:4d} {prey_list[-1]:6d} {predator_list[-1]:11d} {human_list[-1]:8d}")

    stable_ticks = 0

    for tick in range(1, min(ticks, 1000) + 1):
        isle.clear_all_moved_flags()

        animals = []
        for x in range(size):
            for y in range(size):
                current = isle.animal(x, y)
                if isinstance(current, Animal):
                    animals.append(current)
 
        for animal in animals:
            if isle.animal(animal.x, animal.y) is not animal:
                continue
            if isinstance(animal, Human):
                animal.hunt()
            elif isinstance(animal, Predator):
                animal.eat()
            animal.move()
            animal.breed()
            animal.clock_tick()
 
        prey_list.append(isle.count_prey())
        predator_list.append(isle.count_predators())
        human_list.append(isle.count_humans())
 
        if tick % 10 == 0:
            print(f"{tick:4d} {prey_list[-1]:6d} {predator_list[-1]:11d} {human_list[-1]:8d}")
 
        previous = (prey_list[-2], predator_list[-2], human_list[-2])
        current_counts = (prey_list[-1], predator_list[-1], human_list[-1])
        stable_ticks = stable_ticks + 1 if current_counts == previous else 0
        if stable_ticks >= 30:
            print(f"Populations have been constant for 30 ticks (tick {tick}).")
            break
 
    print("\nFinal island:")
    print(isle)
    print(f"\nFinal counts: Prey={prey_list[-1]}, "
          f"Predators={predator_list[-1]}, Humans={human_list[-1]}")
 
    plt.figure(figsize=(9, 5))
    plt.plot(prey_list, label="Prey")
    plt.plot(predator_list, label="Predators")
    plt.plot(human_list, label="Humans")
    plt.xlabel("Time (clock ticks)")
    plt.ylabel("Population")
    plt.title("Island Populations Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("p3_population_chart.png", dpi=160)
    plt.show()
 
 
if __name__ == "__main__":
    main(predator_breed_time=5, predator_starve_time=4,
         initial_predators=18, prey_breed_time=2, initial_prey=80,
         size=12, human_breed_time=6, human_starve_time=14,
         human_hunt_time=2, initial_humans=6, seed=12)
    
