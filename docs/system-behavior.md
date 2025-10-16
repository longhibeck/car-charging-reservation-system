# System Behavior (Use Cases)

## Use Case Diagram

![Use Case Diagram](images/use-case-diagram.png)

Primary Actors:
- Employees
- Facility Admin

Use Cases:
- Create Reservation
- Cancel Reservation
- View Reservation Details
- Register Car
- Deregister Car
- View Car Details
- Add Charging Point
- Remove Charging Point
- View Charging Point Details

Secondary Actors:
- System Clock

## Use Case Narrative: Create Reservation

### Use Case Name
Create Reservation

### Primary Actor
Employee

### Goal
The employee successfully reserves a charging point for a timeframe.

### Preconditions
- The employee is registered and logged into the system.
- The employee has at least one car registered.
- The charging points are registered and available.

### Main Success Scenario
1. The employee selects the date, estimated time of arrival and car.
2. The system tells which charging points are available.
3. The employee selects the charging point by its ID.
4. The system calculates maximum reservation time according to selected car details.
5. The system identifies possible time collisions.
6. The system creates the reservation.
7. The system provides a reservation creation confirmation to the employee.

### Extensions (Alternative Flows)
- 1a. No car is registered:
    - The system notifies the user to register a car.
- 2a. No available charging points:
    - The system notifies the customer and suggests a new time slot.
- 5a. Collision found:
    - The system notifies the customer and suggests sticking or switching to another time slot or charging point.

### Postconditions
- The reservation is created and stored in the system.
- The customer receives a reservation confirmation.

## Use Case Narrative: Cancel Reservation

### Use Case Name
Cancel Reservation

### Primary Actor
Employee

### Goal
The employee successfully cancels a reservation.

### Preconditions
- The employee is registered and logged into the system.
- The employee has a future reservation.

### Main Success Scenario
1. The employee selects the given reservation from the history.
2. The system displays the reservation details.
3. The employee cancels the reservation.
4. The system prompts the user for confirmation.
5. The system provides a reservation cancellation confirmation to the employee.

### Extensions (Alternative Flows)
- 1a. Reservation has already expired.
    - The system does not allow the user to cancel the reservation.

### Postconditions
- The reservation is canceled and removed from the system.
- The customer receives a cancellation confirmation.

## Use Case Narrative: View Reservation Details

### Use Case Name
View Reservation Details

### Primary Actor
Employee

### Goal
The employee successfully views details of their reservations.

### Preconditions
- The employee is registered and logged into the system.
- The employee has at least one reservation (past or future).

### Main Success Scenario
1. The employee requests to view their reservations.
2. The system displays a list of all reservations (past and future).
3. The employee selects a specific reservation.
4. The system displays detailed information about the selected reservation (date, time, car, charging point, status).

### Extensions (Alternative Flows)
- 2a. No reservations found:
    - The system notifies the user that no reservations exist.

### Postconditions
- The reservation details are displayed to the employee.

## Use Case Narrative: Register Car

### Use Case Name
Register Car

### Primary Actor
Employee

### Goal
The employee successfully registers a car.

### Preconditions
- The employee is registered and logged into the system.

### Main Success Scenario
1. The employee registers a car with mandatory details.
2. The system displays the details and prompts the user for confirmation.
3. The system registers the car.
4. The system provides a car registration confirmation to the employee.

### Extensions (Alternative Flows)
- 1a. Missing mandatory details.
    - The system does not allow the user to register the car.

### Postconditions
- The car is registered and stored in the system.
- The employee receives a car registration confirmation.

## Use Case Narrative: Deregister Car

### Use Case Name
Deregister Car

### Primary Actor
Employee

### Goal
The employee successfully deregisters a car.

### Preconditions
- The employee is registered and logged into the system.
- The employee has at least one registered car.

### Main Success Scenario
1. The employee selects a registered car.
2. The system displays the details.
3. The employee deregisters the car.
4. The system prompts the user for confirmation.
5. The system deregisters the car.
6. The system provides a car deregistration confirmation to the employee.

### Extensions (Alternative Flows)
- 1a. No registered cars available:
    - The system notifies the user that no cars are registered.

### Postconditions
- The car is deregistered and removed from the system.
- The employee receives a car deregistration confirmation.

## Use Case Narrative: View Car Details

### Use Case Name
View Car Details

### Primary Actor
Employee

### Goal
The employee successfully views details of their registered cars.

### Preconditions
- The employee is registered and logged into the system.
- The employee has at least one registered car.

### Main Success Scenario
1. The employee requests to view their registered cars.
2. The system displays a list of all registered cars.
3. The employee selects a specific car.
4. The system displays detailed information about the selected car (make, model, license plate, battery capacity, charging specifications).

### Extensions (Alternative Flows)
- 2a. No cars registered:
    - The system notifies the user that no cars are registered.

### Postconditions
- The car details are displayed to the employee.

## Use Case Narrative: Add Charging Point

### Use Case Name
Add Charging Point

### Primary Actor
Facility Admin

### Goal
The Facility Admin successfully adds a Charging Point

### Preconditions
- The Facility Admin is registered and logged into the system.

### Main Success Scenario
1. The Facility Admin enters the Charging Point details (ID, location, power type, maximum power output).
2. The system validates the details and checks for duplicate IDs.
3. The system displays the details and prompts the user for confirmation.
4. The system registers the Charging Point.
5. The system provides a Charging Point registration confirmation to the Facility Admin.

### Extensions (Alternative Flows)
- 1a. Missing mandatory details:
    - The system does not allow the user to add a Charging Point.
- 2a. Duplicate Charging Point ID:
    - The system notifies the user that the ID already exists and requests a different ID.

### Postconditions
- The Charging Point is registered and stored in the system.
- The Facility Admin receives a Charging Point registration confirmation.


## Use Case Narrative: Remove Charging Point

### Use Case Name
Remove Charging Point

### Primary Actor
Facility Admin

### Goal
The Facility Admin successfully removes a Charging Point from the system.

### Preconditions
- The Facility Admin is registered and logged into the system.
- At least one Charging Point exists in the system.

### Main Success Scenario
1. The Facility Admin requests to view all Charging Points.
2. The system displays a list of all registered Charging Points.
3. The Facility Admin selects a Charging Point to remove.
4. The system checks if the Charging Point has any active reservations.
5. The system displays the Charging Point details and prompts for confirmation.
6. The Facility Admin confirms the removal.
7. The system removes the Charging Point.
8. The system provides a Charging Point removal confirmation to the Facility Admin.

### Extensions (Alternative Flows)
- 2a. No Charging Points available:
    - The system notifies the user that no Charging Points are registered.
- 4a. Active reservations exist:
    - The system notifies the user that the Charging Point cannot be removed due to active reservations and suggests canceling them first.

### Postconditions
- The Charging Point is removed from the system.
- The Facility Admin receives a Charging Point removal confirmation.

## Use Case Narrative: View Charging Point Details

### Use Case Name
View Charging Point Details

### Primary Actor
Facility Admin

### Goal
The Facility Admin successfully views details of Charging Points in the system.

### Preconditions
- The Facility Admin is registered and logged into the system.
- At least one Charging Point exists in the system.

### Main Success Scenario
1. The Facility Admin requests to view all Charging Points.
2. The system displays a list of all registered Charging Points.
3. The Facility Admin selects a specific Charging Point.
4. The system displays detailed information about the selected Charging Point (ID, location, power type, maximum power output, current status, reservation schedule).

### Extensions (Alternative Flows)
- 2a. No Charging Points available:
    - The system notifies the user that no Charging Points are registered.

### Postconditions
- The Charging Point details are displayed to the Facility Admin.
