# **Design a Parking Lot**

## **Background**
Parking lots have open spaces for vehicles to park in. Vehicles can be of different sizes, e.g., cars, limos, trucks, etc.

In some cases, parking spots can be numbered. For large venues, parking lots may have multiple levels, i.e., parking garages.

Sometimes parking is free, but in other cases, customers have to pay. So parking lots can have a payment system to keep track of parked vehicles.

---

## **Requirements**

### **Possible Questions to Ask**
- Will there be multiple levels in the parking lot?  
- What kinds of vehicles will be parked? Will their sizes differ?  
- Will there be special spots for certain vehicles?  
- Will the parking lot have a payment system? If so, how will it work?  
- Will parking spots be reserved, or can the driver choose any spot?  
- How much functionality will the driver have beyond parking and paying?  

---

### **Basics**
- The parking lot will have **multiple levels**.  
- Possible vehicle types: **car**, **limo**, **semi-truck**.  
- The parking lot will have a **payment system**, with a **single entrance and exit**.  
- Drivers will be **assigned a parking spot** after paying.  

---

### **Vehicles and Parking Spots**
- Vehicles can be of **different sizes**:  
  - **Car** = 1 spot  
  - **Limo** = 2 spots  
  - **Truck** = 3 spots  
- Each parking spot will have a size of **1 unit**.  
  - A vehicle must fully take up each spot assigned to it (no fractional spots).  
- Vehicles will **automatically be assigned** the next available parking spot on the lowest floor.  

---

### **Payment System**
- Drivers will **pay for parking** and be assigned the next available spot on the lowest floor.  
- Drivers can pay for a **variable number of hours**, and they are charged based on an **hourly rate** when they remove their vehicle.  
  - Vehicles can be parked for a **variable number of hours**.  
- If there is **no capacity**, the system should:  
  - **Not assign a spot**.  
  - **Notify the driver**.  

---

## **Design**

### **High-Level Overview**
1. **Vehicle Classes**:
   - A base `Vehicle` class.  
   - `Car`, `Limo`, and `Truck` classes will inherit from `Vehicle`.  
   - Each class will have a predefined **size**.  

2. **Driver Class**:
   - Each `Driver` object will:  
     - Have a vehicle associated with it.  
     - Track the **total payment due**.  

3. **Parking Garage**:
   - The `ParkingGarage` will be made up of multiple `ParkingFloor` objects.  

4. **Parking Floor**:
   - Each `ParkingFloor` will consist of multiple `ParkingSpot` objects.  
   - Represented as an **array** (`0 = empty`, `1 = occupied`).  

5. **Parking System**:
   - The `ParkingSystem` will serve as the main controller of the `ParkingGarage`.  
   - Responsibilities:  
     - Track parking hours.  
     - Charge drivers.  

---

## **Code Design**

### **Vehicle Class**
A base class for all vehicles, with a `size` attribute to determine the number of spots required.  

```python
class Vehicle:
    def __init__(self, size, license_plate):
        self.size = size  # 1 = car, 2 = limo, 3 = truck
        self.license_plate = license_plate

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(size=1, license_plate=license_plate)

class Limo(Vehicle):
    def __init__(self, license_plate):
        super().__init__(size=2, license_plate=license_plate)

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(size=3, license_plate=license_plate)
```

---

Would you like me to expand this further with detailed examples of the `ParkingSystem` or `Driver` implementation?