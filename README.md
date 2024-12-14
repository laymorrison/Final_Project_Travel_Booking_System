# Final_Project_Travel_Booking_System

* Laymoni Morrison
* Email: lamorrison@chapman.edu
* Course: CPSC_408
* Link to demo video: 

## Files Included
1. **`app.py`**: Main Flask application.
2. **`templates/`**: HTML templates for the UI.
   - `base.html`: Base layout.
   - `index.html`: Users management.
   - `flights.html`, `hotels.html`, `car_rentals.html`: Manage flights, hotels, and car rentals.
   - `bookings.html`, `payments.html`: Manage bookings and payments.
   - `most_booked_destinations.html`, `revenue_by_airline.html`: Report pages.
3. **`static/`**: CSS and JavaScript files (if applicable).
4. **`database_setup.sql`**: SQL scripts for creating tables, views, and inserting sample data.

---

## How to Run
1. **Requirements**:
   - Install Python 3.x and MySQL.
   - Install required Python libraries using:
     ```bash
     pip install flask mysql-connector-python
     ```

2. **Database Setup**:
   - Create the database using `database_setup.sql`:
     ```bash
     mysql -u [username] -p < database_setup.sql
     ```
   - Replace `[username]` with your MySQL username.

3. **Run the Application**:
   - Start the Flask app:
     ```bash
     python app.py
     ```
   - Open `http://localhost:5000` in your browser.

---

## Features
- **CRUD Operations**: Add, view, update, delete (soft delete for users).
- **Reports**:
  - **Revenue by Airline**: Aggregated revenue for confirmed bookings.
  - **Most Booked Destinations**: Popular destinations based on confirmed bookings.
- **Dynamic Filters**: Filter bookings and payments by status.
- **CSV Export**: Export data for all entities.
- **Referential Integrity**: Foreign key constraints across tables.

---

## Note
While some UI elements differ slightly from the original plan, the project fulfills all requirements, including views, joins, subqueries, and transaction management.
