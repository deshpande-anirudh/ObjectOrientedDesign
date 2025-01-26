---

### Problem Statement: Elevator Control System Design

You are tasked with designing a software system for managing an **elevator control system** for a multi-story building. The building has multiple elevators, and the software must efficiently control the movement and operation of these elevators. The system must account for the following requirements:

---

### Functional Requirements:

1. **Basic Elevator Operations**:
   - Each elevator can move **up**, **down**, or stay **idle**.
   - Each elevator has a defined **maximum capacity** in terms of the number of people or weight.

2. **User Interaction**:
   - Users can request an elevator from any floor by pressing **Up** or **Down** buttons on the floor.
   - Users inside the elevator can select a **destination floor** using a control panel.

3. **Request Handling**:
   - The system should assign the most appropriate elevator to a user request based on the current state of the elevators.
   - Requests should be queued if no elevator is available immediately.

4. **Emergency Handling**:
   - An **emergency button** inside the elevator stops it immediately and alerts maintenance.
   - Elevators must remain functional during a **power failure**, transitioning to a backup mode where only one elevator operates at a time.

5. **Maintenance Mode**:
   - Elevators can be put into a maintenance mode, during which they will not respond to requests.

---

### Non-Functional Requirements:

1. **Scalability**:
   - The system must support buildings with up to **100 floors** and **20 elevators**.

2. **Efficiency**:
   - Minimize wait times for users.
   - Optimize the number of stops an elevator makes during a trip.

3. **Reliability**:
   - The system should handle edge cases like simultaneous requests, overloaded elevators, and stalled elevators.

4. **Extensibility**:
   - Allow for future extensions like integration with mobile apps for calling elevators remotely.

---

### Deliverables:

- **Classes**: Design the classes with attributes and methods. Example entities to consider: `Elevator`, `Floor`, `Button`, `Request`, etc.
- **Relationships**: Define relationships between the classes (e.g., aggregation, inheritance).
- **Behaviors**: Specify how the system handles elevator assignment, state changes, and user requests.
- **Algorithms**: Outline the logic for selecting an elevator for a given request.

---

