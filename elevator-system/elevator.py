from enum import Enum, auto
from threading import Thread, Lock
import time


class Action(Enum):
    UP = auto()
    DOWN = auto()
    IDLE = auto()


class Elevator:
    def __init__(self, _id, num_floors=10):
        self.num_floors = num_floors
        self.at_floor = 8
        self.action = Action.IDLE
        self.id = _id
        self.lock = Lock()
        self.up_queue = []
        self.down_queue = []

    def request(self, floor):
        with self.lock:
            if floor > self.at_floor:
                self.up_queue.append(floor)
                self.up_queue.sort()
            elif floor < self.at_floor:
                self.down_queue.append(floor)
                self.down_queue.sort(reverse=True)
            else:
                print(f"Elevator: {self.id} is already at {self.at_floor}")


    def process_queue(self, queue):
        while queue:
            next_floor = queue.pop(0)
            if next_floor == self.at_floor:
                continue
            print(f"Elevator:{self.id} going from {self.at_floor} to {next_floor}")
            time.sleep(1)
            self.at_floor = next_floor
            print(f"Elevator:{self.id} door opening at: {self.at_floor}")
            time.sleep(1)
            print(f"Elevator:{self.id} door closing at: {self.at_floor}")
            time.sleep(1)

        print(f"Elevator:{self.id} completed one way trip")
        self.action = Action.IDLE

    def move(self):
        while True:
            with self.lock:
                if self.action == Action.UP:
                    if self.up_queue:
                        self.process_queue(self.up_queue)
                    else:
                        if self.down_queue:
                            self.action = Action.DOWN
                        else:
                            self.action = Action.IDLE

                elif self.action == Action.DOWN:
                    if self.down_queue:
                        self.process_queue(self.down_queue)
                    else:
                        if self.up_queue:
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

            time.sleep(0.1)


class ElevatorSystem:
    def __init__(self, num_elevators=1, num_floors=10):
        self.elevators = [
            Elevator(i, num_floors) for i in range(num_elevators)
        ]

        for elevator in self.elevators:
            thread = Thread(target=elevator.move, daemon=True)
            thread.start()

    def request(self, num_floor):
        # find the correct candidate
        candidates = [
            (abs(num_floor - e.at_floor), e)
            for e in self.elevators
            if e.action == Action.IDLE or
               (num_floor > e.at_floor and e.action == Action.UP) or
               (num_floor < e.at_floor and e.action == Action.DOWN)
        ]

        candidates.sort(key=lambda x: x[0])
        best_elevator = candidates[0][1]
        best_elevator.request(num_floor)


if __name__ == "__main__":
    elevator_system = ElevatorSystem(1, 30)
    threads = []

    for floor in [1, 5, 10, 15, 20, 25, 30, 27, 23, 3]:
        thread = Thread(target=elevator_system.request, args=(floor,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    while True:
        time.sleep(1)
