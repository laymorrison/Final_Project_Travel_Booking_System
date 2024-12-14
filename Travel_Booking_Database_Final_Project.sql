-- Laymoni Morrison
-- Final Travel Booking Database

-- Create and use the TravelBooking database
CREATE DATABASE TravelBookingDatabase;
USE TravelBookingDatabase;

-- Create User table
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE
);

-- Create Flight table
CREATE TABLE Flight (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    airline_name VARCHAR(100) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Create Hotel table
CREATE TABLE Hotel (
    hotel_id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    available_rooms INT NOT NULL CHECK (available_rooms >= 0),
    price_per_night DECIMAL(10, 2) NOT NULL
);

-- Create CarRental table
CREATE TABLE CarRental (
    car_rental_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    car_type VARCHAR(50) NOT NULL,
    availability BOOLEAN DEFAULT TRUE,
    price_per_day DECIMAL(10, 2) NOT NULL
);

-- Create Booking table
CREATE TABLE Booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    flight_id INT DEFAULT NULL,
    hotel_id INT DEFAULT NULL,
    car_rental_id INT DEFAULT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('confirmed', 'canceled', 'pending') NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (flight_id) REFERENCES Flight(flight_id),
    FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id),
    FOREIGN KEY (car_rental_id) REFERENCES CarRental(car_rental_id)
);

-- Create Payment table
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('completed', 'refunded', 'pending') NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id) ON DELETE CASCADE
);

-- Manual Data
INSERT INTO User (name, email, phone_number, date_of_birth) VALUES
('Alice Johnson', 'alice.johnson@example.com', '555-123-4567', '1990-01-15'),
('Ben Carter', 'ben.carter@example.com', '555-234-5678', '1985-03-22'),
('Chloe Smith', 'chloe.smith@example.com', '555-345-6789', '1992-06-30'),
('Daniel Brown', 'daniel.brown@example.com', '555-456-7890', '1988-09-14'),
('Ella Green', 'ella.green@example.com', '555-567-8901', '1995-11-05'),
('Frank Harris', 'frank.harris@example.com', '555-678-9012', '1987-02-18'),
('Grace Miller', 'grace.miller@example.com', '555-789-0123', '1993-05-08'),
('Harry Wilson', 'harry.wilson@example.com', '555-890-1234', '1989-07-19'),
('Isla Moore', 'isla.moore@example.com', '555-901-2345', '1991-10-12'),
('Jack Taylor', 'jack.taylor@example.com', '555-012-3456', '1986-12-25');

INSERT INTO Flight (airline_name, departure_time, arrival_time, origin, destination, price) VALUES
('Delta', '2024-12-01 10:00:00', '2024-12-01 14:00:00', 'Seattle', 'Los Angeles', 200.00),
('United Airlines', '2024-12-02 11:00:00', '2024-12-02 15:00:00', 'New York', 'Chicago', 250.00),
('Southwest', '2024-12-03 12:00:00', '2024-12-03 16:00:00', 'Houston', 'Miami', 180.00),
('American Airlines', '2024-12-04 13:00:00', '2024-12-04 17:00:00', 'San Francisco', 'Las Vegas', 150.00),
('Alaska Airlines', '2024-12-05 14:00:00', '2024-12-05 18:00:00', 'Dallas', 'Denver', 220.00),
('JetBlue', '2024-12-06 15:00:00', '2024-12-06 19:00:00', 'Boston', 'Orlando', 190.00),
('Spirit Airlines', '2024-12-07 16:00:00', '2024-12-07 20:00:00', 'Phoenix', 'Salt Lake City', 130.00),
('Frontier', '2024-12-08 17:00:00', '2024-12-08 21:00:00', 'Atlanta', 'Nashville', 110.00),
('Delta', '2024-12-09 18:00:00', '2024-12-09 22:00:00', 'Seattle', 'San Diego', 210.00),
('United Airlines', '2024-12-10 19:00:00', '2024-12-10 23:00:00', 'Chicago', 'New York', 240.00);

INSERT INTO Hotel (hotel_name, location, available_rooms, price_per_night) VALUES
('Grand Plaza', 'Los Angeles', 25, 150.00),
('City Inn', 'Chicago', 15, 120.00),
('Beachside Resort', 'Miami', 20, 180.00),
('Mountain Lodge', 'Denver', 10, 200.00),
('Urban Suites', 'San Francisco', 12, 170.00),
('Luxury Stay', 'New York', 30, 250.00),
('Budget Hotel', 'Dallas', 50, 80.00),
('Family Inn', 'Orlando', 40, 100.00),
('Skyline Towers', 'Seattle', 18, 190.00),
('Desert Oasis', 'Phoenix', 22, 140.00);

INSERT INTO CarRental (company_name, car_type, availability, price_per_day) VALUES
('Hertz', 'Sedan', TRUE, 50.00),
('Enterprise', 'SUV', TRUE, 75.00),
('Avis', 'Compact', TRUE, 40.00),
('Budget', 'Luxury', TRUE, 100.00),
('National', 'Convertible', TRUE, 90.00),
('Alamo', 'Minivan', TRUE, 60.00),
('Dollar', 'Pickup Truck', TRUE, 70.00),
('Thrifty', 'Crossover', TRUE, 65.00),
('Sixt', 'Sports Car', TRUE, 120.00),
('Fox', 'Electric', TRUE, 80.00);

INSERT INTO Booking (user_id, flight_id, hotel_id, car_rental_id, status) VALUES
(1, 1, 1, 1, 'confirmed'),
(2, 2, 2, 2, 'pending'),
(3, 3, 3, NULL, 'confirmed'),
(4, 4, 4, 4, 'canceled'),
(5, 5, NULL, NULL, 'confirmed'),
(6, 6, 5, NULL, 'pending'),
(7, 7, NULL, 5, 'confirmed'),
(8, 8, NULL, 6, 'canceled'),
(9, 9, 6, NULL, 'confirmed'),
(10, 10, 7, 7, 'confirmed');

INSERT INTO Payment (booking_id, amount, status) VALUES
(1, 200.00, 'completed'),
(2, 250.00, 'pending'),
(3, 400.00, 'completed'),
(4, 50.00, 'refunded'),
(5, 300.00, 'completed'),
(6, 180.00, 'pending'),
(7, 190.00, 'completed'),
(8, 20.00, 'refunded'),
(9, 220.00, 'completed'),
(10, 450.00, 'completed');



-- Create a view for active users
CREATE VIEW ActiveUsers AS
SELECT user_id, name, email, phone_number
FROM User
WHERE is_deleted = FALSE;

-- Create a view for confirmed bookings
CREATE VIEW ConfirmedBookings AS
SELECT b.booking_id, u.name AS user_name, b.booking_date, b.status
FROM Booking b
INNER JOIN User u ON b.user_id = u.user_id
WHERE b.status = 'confirmed' AND b.is_deleted = FALSE;

-- Create a view for revenue by airline (aggregation query)
CREATE VIEW RevenueByAirline AS
SELECT f.airline_name, SUM(f.price) AS total_revenue
FROM Flight f
INNER JOIN Booking b ON f.flight_id = b.flight_id
WHERE b.status = 'confirmed'
GROUP BY f.airline_name;

-- Create a view for most booked destinations (subquery)
CREATE VIEW MostBookedDestinations AS
SELECT destination, COUNT(*) AS booking_count
FROM Flight
WHERE flight_id IN (SELECT flight_id FROM Booking WHERE status = 'confirmed')
GROUP BY destination
ORDER BY booking_count DESC;

-- Add transaction
DELIMITER //
CREATE PROCEDURE CreateBooking(IN user INT, IN flight INT, IN status ENUM('confirmed', 'canceled', 'pending'))
BEGIN
    START TRANSACTION;
    INSERT INTO Booking (user_id, flight_id, status) VALUES (user, flight, status);
    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;
END //
DELIMITER ;


USE TravelBookingDatabase;

-- List all tables
SHOW TABLES;

-- View table schema
DESCRIBE User;

-- View sample data
SELECT * FROM User;
SELECT * FROM Flight;
SELECT * FROM Hotel;
SELECT * FROM carrental;
SELECT * FROM Booking;
SELECT * FROM Payment;


INSERT INTO User (user_id, name, email, phone_number, date_of_birth, is_deleted)
VALUES (1, 'Default User', 'default@example.com', '0000000000', '2000-01-01', 0)
ON DUPLICATE KEY UPDATE is_deleted = 0;


-- Check for bookings referencing deleted users
SELECT *
FROM Booking b
LEFT JOIN User u ON b.user_id = u.user_id
WHERE u.user_id IS NULL;

-- Check for bookings referencing deleted flights
SELECT *
FROM Booking b
LEFT JOIN Flight f ON b.flight_id = f.flight_id
WHERE f.flight_id IS NULL;

-- Check for bookings referencing deleted hotels
SELECT *
FROM Booking b
LEFT JOIN Hotel h ON b.hotel_id = h.hotel_id
WHERE h.hotel_id IS NULL;

-- Check for bookings referencing deleted car rentals
SELECT *
FROM Booking b
LEFT JOIN CarRental c ON b.car_rental_id = c.car_rental_id
WHERE b.car_rental_id IS NOT NULL AND c.car_rental_id IS NULL;


SELECT destination, COUNT(*) AS booking_count
FROM Flight
WHERE flight_id IN (SELECT flight_id FROM Booking WHERE status = 'confirmed')
GROUP BY destination
ORDER BY booking_count DESC;










