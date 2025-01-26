from enum import Enum, auto
import time
from threading import Thread, Lock

class Action(Enum):
    UP = auto()
    DOWN = auto()
    IDLE = auto()

class Elevator:
    def __init__(self, id, num_floors):
        self.id = id
        self.num_floors = num_floors
        self.action = Action.IDLE
        self.at_floor = 1
        self.up_queue = []  # Floors above the current floor
        self.down_queue = []  # Floors below the current floor
        self.lock = Lock()

    def request(self, floor):
        if floor < 1 or floor > self.num_floors:
            print(f"Invalid floor {floor}. Must be between 1 and {self.num_floors}.")
            return

        with self.lock:
            if floor > self.at_floor:
                if floor not in self.up_queue:
                    self.up_queue.append(floor)
                    self.up_queue.sort()
            elif floor < self.at_floor:
                if floor not in self.down_queue:
                    self.down_queue.append(floor)
                    self.down_queue.sort(reverse=True)
            else:
                print(f"Elevator {self.id} is already at floor {floor}.")

    def process_queue(self, queue):
        if queue:
            next_floor = queue.pop(0)
            print(f"Elevator {self.id} moving {self.action.name} to floor {next_floor}.")
            self.at_floor = next_floor
            time.sleep(1)  # Simulate time taken to move between floors
            print(f"Elevator {self.id} arrived at floor {next_floor}.")

    def move(self):
        while True:
            with self.lock:
                if self.action == Action.UP:
                    if self.up_queue:
                        self.process_queue(self.up_queue)
                    elif self.down_queue:
                        self.action = Action.DOWN
                    else:
                        self.action = Action.IDLE
                elif self.action == Action.DOWN:
                    if self.down_queue:
                        self.process_queue(self.down_queue)
                    elif self.up_queue:
                        self.action = Action.UP
                    else:
                        self.action = Action.IDLE
                else:
                    if self.up_queue:
                        self.action = Action.UP
                    elif self.down_queue:
                        self.action = Action.DOWN
                    else:
                        print(f"Elevator {self.id} is idle at floor {self.at_floor}.")

            # Pause briefly to allow other threads to act
            time.sleep(0.1)

class ElevatorSystem:
    def __init__(self, num_elevators=5, num_floors=10):
        self.num_floors = num_floors
        self.elevators = [Elevator(i, num_floors) for i in range(num_elevators)]
        self.threads = []

        for elevator in self.elevators:
            thread = Thread(target=elevator.move, daemon=True)
            thread.start()
            self.threads.append(thread)

    def request(self, floor):
        # Find the best elevator to handle the request
        candidates = [
            (abs(e.at_floor - floor), e)
            for e in self.elevators
            if (e.action == Action.IDLE or
                (e.action == Action.UP and floor > e.at_floor) or
                (e.action == Action.DOWN and floor < e.at_floor))
        ]

        if not candidates:
            print(f"No available elevators for floor {floor}.")
            return

        # Assign the closest elevator
        candidates.sort(key=lambda x: x[0])
        best_elevator = candidates[0][1]
        print(f"Assigning floor {floor} to Elevator {best_elevator.id}.")
        best_elevator.request(floor)

# Example Usage
if __name__ == "__main__":
    # Initialize a system for a 30-floor building with 3 elevators
    elevator_system = ElevatorSystem(num_elevators=3, num_floors=30)

    # Simulate requests
    requests = [5, 15, 25, 10, 20, 30, 1]
    threads = []

    for floor in requests:
        thread = Thread(target=elevator_system.request, args=(floor,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Keep the system running
    while True:
        time.sleep(1)
