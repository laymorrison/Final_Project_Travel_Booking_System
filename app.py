from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import mysql.connector

app = Flask(__name__)

# In-memory cart
cart = []

# Database connection function
def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="CPSC408!",
            database="TravelBookingDatabase",
            auth_plugin='mysql_native_password'
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Utility: Get cart count
def get_cart_count():
    return len(cart)

# Users Management
@app.route('/')
def index():
    connection = get_db_connection()
    if not connection:
        return "Database connection error!", 500

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM User WHERE is_deleted = 0")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', title="Users", users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    dob = request.form['dob']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO User (name, email, phone_number, date_of_birth) VALUES (%s, %s, %s, %s)", 
                   (name, email, phone, dob))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE User SET is_deleted = 1 WHERE user_id = %s", (user_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

# Flights Management
@app.route('/flights')
def flights():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Flight")
    flights = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('flights.html', title="Flights", flights=flights)

@app.route('/add_flight', methods=['POST'])
def add_flight():
    airline_name = request.form['airline_name']
    departure_time = request.form['departure_time']
    arrival_time = request.form['arrival_time']
    origin = request.form['origin']
    destination = request.form['destination']
    price = request.form['price']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Flight (airline_name, departure_time, arrival_time, origin, destination, price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (airline_name, departure_time, arrival_time, origin, destination, price))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('flights'))

# Hotels Managment
@app.route('/hotels')
def hotels():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Hotel")
    hotels = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('hotels.html', title="Hotels", hotels=hotels)

@app.route('/add_hotel', methods=['POST'])
def add_hotel():
    hotel_name = request.form['hotel_name']
    location = request.form['location']
    available_rooms = request.form['available_rooms']
    price_per_night = request.form['price_per_night']

    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO Hotel (hotel_name, location, available_rooms, price_per_night)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (hotel_name, location, available_rooms, price_per_night))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('hotels'))

# Car_rentals Management
@app.route('/car_rentals')
def car_rentals():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CarRental")
    car_rentals = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('car_rentals.html', title="Car Rentals", car_rentals=car_rentals)

@app.route('/add_car_rental', methods=['POST'])
def add_car_rental():
    company_name = request.form['company_name']
    car_type = request.form['car_type']
    price_per_day = request.form['price_per_day']
    availability = request.form['availability']

    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO CarRental (company_name, car_type, price_per_day, availability)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (company_name, car_type, price_per_day, availability))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('car_rentals'))

# Search ALL
@app.route('/search_all', methods=['GET', 'POST'])
def search_all():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    flights = []
    car_rentals = []
    hotels = []

    if request.method == 'POST':
        origin = request.form.get('origin', '').strip()
        destination = request.form.get('destination', '').strip()
        min_price = request.form.get('min_price', '').strip()
        max_price = request.form.get('max_price', '').strip()

        # Handle empty fields
        min_price = float(min_price) if min_price else 0
        max_price = float(max_price) if max_price else 100000

        # Search Flights
        flight_query = """
            SELECT * FROM Flight
            WHERE (origin LIKE %s OR destination LIKE %s)
            AND price BETWEEN %s AND %s
        """
        cursor.execute(flight_query, (f"%{origin}%", f"%{destination}%", min_price, max_price))
        flights = cursor.fetchall()

        # Search Car Rentals
        car_rental_query = """
            SELECT * FROM CarRental
            WHERE company_name LIKE %s OR car_type LIKE %s
        """
        cursor.execute(car_rental_query, (f"%{destination}%", f"%{origin}%"))
        car_rentals = cursor.fetchall()

        # Search Hotels
        hotel_query = """
            SELECT * FROM Hotel
            WHERE location LIKE %s
        """
        cursor.execute(hotel_query, (f"%{destination}%",))
        hotels = cursor.fetchall()

    cursor.close()
    connection.close()
    return render_template(
        'search_all.html',
        title="Search All",
        flights=flights,
        car_rentals=car_rentals,
        hotels=hotels
    )

# View Cart Management
@app.route('/view_cart')
def view_cart():
    total_price = sum(item['price'] for item in cart) if cart else 0  # Calculate total price
    return render_template(
        'view_cart.html',
        title="View Cart",
        cart=cart,
        total_price=total_price,
        cart_count=get_cart_count()
    )

# Checkout Management
@app.route('/checkout', methods=['POST'])
def checkout():
    global cart

    user_id = 1  # Use the default user

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Clear the cart
    cart.clear()

    cursor.close()
    connection.close()

    # Redirect to the cart page with a success flag
    return redirect(url_for('view_cart', success=1))



@app.route('/bookings', methods=['GET'])
def bookings():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Get filter status from query parameters, default to 'all'
    status = request.args.get('status', 'all')

    # Query for bookings, filtering by status
    if status == 'all':
        cursor.execute("""
            SELECT b.booking_id, u.name AS user_name, f.airline_name AS flight_name, h.hotel_name AS hotel_name,
                   c.company_name AS car_rental_name, b.status
            FROM Booking b
            INNER JOIN User u ON b.user_id = u.user_id
            LEFT JOIN Flight f ON b.flight_id = f.flight_id
            LEFT JOIN Hotel h ON b.hotel_id = h.hotel_id
            LEFT JOIN CarRental c ON b.car_rental_id = c.car_rental_id
            WHERE u.is_deleted = 0
        """)
    else:
        cursor.execute("""
            SELECT b.booking_id, u.name AS user_name, f.airline_name AS flight_name, h.hotel_name AS hotel_name,
                   c.company_name AS car_rental_name, b.status
            FROM Booking b
            INNER JOIN User u ON b.user_id = u.user_id
            LEFT JOIN Flight f ON b.flight_id = f.flight_id
            LEFT JOIN Hotel h ON b.hotel_id = h.hotel_id
            LEFT JOIN CarRental c ON b.car_rental_id = c.car_rental_id
            WHERE u.is_deleted = 0 AND b.status = %s
        """, (status,))

    bookings = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('bookings.html', title="Bookings", bookings=bookings)


# Add Booking
@app.route('/add_booking', methods=['POST'])
def add_booking():
    user_id = request.form['user_id']
    flight_id = request.form['flight_id']
    status = request.form['status']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Booking (user_id, flight_id, status) VALUES (%s, %s, %s)", 
                   (user_id, flight_id, status))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('bookings'))

# Payments Management
@app.route('/payments', methods=['GET'])
def payments():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.payment_id, p.booking_id, p.amount, p.status, b.status AS booking_status
        FROM Payment p
        LEFT JOIN Booking b ON p.booking_id = b.booking_id
    """)
    payments = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('payments.html', title="Payments", payments=payments)

@app.route('/add_payment', methods=['POST'])
def add_payment():
    booking_id = request.form['booking_id']
    amount = request.form['amount']
    status = request.form['status']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Payment (booking_id, amount, status) VALUES (%s, %s, %s)", 
                   (booking_id, amount, status))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('payments'))

# CVS Management
@app.route('/download_csv/<string:table_name>')
def download_csv(table_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    valid_tables = ['User', 'Flight', 'CarRental', 'Hotel', 'Booking', 'Payment']

    if table_name not in valid_tables:
        return "Invalid table name!", 400

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    def generate():
        if rows:
            yield ','.join(rows[0].keys()) + '\n'
        for row in rows:
            yield ','.join([str(value) for value in row.values()]) + '\n'

    response = Response(generate(), mimetype='text/csv')
    response.headers['Content-Disposition'] = f'attachment; filename={table_name.lower()}.csv'
    return response

# Add to Cart Management
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_type = request.form['item_type']  # e.g., Flight, Hotel, Car Rental
    item_id = int(request.form['item_id'])  # ID of the item
    item_name = request.form['item_name']  # Name of the item
    item_price = float(request.form['item_price'])  # Price of the item

    # Add the item to the in-memory cart
    cart.append({
        'type': item_type,
        'id': item_id,
        'name': item_name,
        'price': item_price
    })

    return redirect(url_for('view_cart'))

# Update Booking
@app.route('/update_booking/<int:booking_id>', methods=['POST'])
def update_booking(booking_id):
    new_status = request.form.get('status')  # Retrieve the updated status from the form

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Update the status in the Booking table
        cursor.execute(
            "UPDATE Booking SET status = %s WHERE booking_id = %s",
            (new_status, booking_id)
        )
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Error updating booking: {e}")
    finally:
        cursor.close()
        connection.close()

    # Redirect back to the bookings page after the update
    return redirect('/bookings')

@app.route('/update_payment/<int:payment_id>', methods=['POST'])
def update_payment(payment_id):
    # Get the new status from the form
    new_status = request.form.get('status')

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Update the status in the Payment table
        cursor.execute(
            "UPDATE Payment SET status = %s WHERE payment_id = %s",
            (new_status, payment_id)
        )
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Error updating payment: {e}")
    finally:
        cursor.close()
        connection.close()

    # Redirect back to the payments page after updating
    return redirect('/payments')

@app.route('/revenue_by_airline', methods=['GET'])
def revenue_by_airline():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Query the RevenueByAirline view
    cursor.execute("SELECT * FROM RevenueByAirline")
    revenue_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('revenue_by_airline.html', title="Revenue by Airline", revenue_data=revenue_data)

@app.route('/most_booked_destinations')
def most_booked_destinations():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Fetch data from the view
    cursor.execute("SELECT * FROM MostBookedDestinations")
    destinations = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('most_booked_destinations.html', title="Most Booked Destinations", destinations=destinations)


if __name__ == '__main__':
    app.run(debug=True)
