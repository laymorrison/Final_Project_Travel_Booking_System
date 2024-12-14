# Final_Project_Travel_Booking_System

* Laymoni Morrison
* Email: lamorrison@chapman.edu
* Student ID: 2420236
* Course: CPSC 408
* Link to demo video: https://youtu.be/Obnc9hQmzbk

## Files Included
1. **`app.py`**: Main Flask application.

### **Templates**
Located in the `templates/` folder:
1. **`base.html`**: Base layout for consistent styling across pages.
2. **`index.html`**: User management interface.
3. **`flights.html`**: Manage flights.
4. **`hotels.html`**: Manage hotels.
5. **`car_rentals.html`**: Manage car rentals.
6. **`bookings.html`**: Manage bookings.
7. **`payments.html`**: Manage payments.
8. **`search_all.html`**: Search functionality for flights, hotels, and car rentals.
9. **`view_cart.html`**: View selected items in the cart.
10. **`checkout_confirmation.html`**: Display a confirmation message after checkout.
11. **`most_booked_destinations.html`**: Report for most booked destinations.
12. **`revenue_by_airline.html`**: Report for revenue by airline.

### **Static Files**
Located in the `static/` folder:
1. **`static.css`**: Custom styles for the project.

### Database
4. Travel_Booking_Database_Final_Project.sql: SQL scripts for creating tables, views, and inserting sample data.

---

## How to Run
1. Requirements:
   - Install Python 3.x and MySQL.
   - Install required Python libraries using:
     pip install flask mysql-connector-python

2. Database Setup:
   - Create the database using Travel_Booking_Database_Final_Project.sql

3. Run the Application:
   - Start the Flask app:
     python app.py
   - Open http://localhost:5000 in your browser.

---

## Features
- CRUD Operations: Add, view, update, delete (soft delete for users).
- Reports:
  - Revenue by Airline: Aggregated revenue for confirmed bookings.
  - Most Booked Destinations: Popular destinations based on confirmed bookings.
- Dynamic Filters: Filter bookings and payments by status.
- CSV Export: Export data for all entities.
- Referential Integrity: Foreign key constraints across tables.

---

## Resources
- Class Lectures/Projects
- https://www.w3schools.com/html/html_attributes.asp
- https://www.w3schools.com/mysql/mysql_delete.asp
- https://python-adv-web-apps.readthedocs.io/en/latest/flask_db1.html

## Note
While some UI elements differ slightly from my original plan, the project fulfills all requirements, including views, joins, subqueries, and transaction management.
