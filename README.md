# Car Market - Car Buying and Selling Portal

Car Market is a web application built with Django that allows users to buy and sell cars. The platform provides a seamless experience for users to list their cars for sale and for buyers to browse and purchase cars directly from sellers.

## Features

### User Authentication
- User registration with Name, Email, and Password
- Secure login and logout using Django's authentication system
- Password reset functionality via email
- User profile management

### User Dashboard
- Personalized dashboard for users
- Options to buy cars, sell cars, view purchased cars, and manage listed cars
- Quick access to notifications and account settings

### Buy Car Portal
- Browse all available cars
- Search and filter cars by price range, location, condition, model, etc.
- Detailed car information including images, price, mileage, model, year, and seller details
- Reserve cars with direct UPI payment to sellers

### Sell Car Portal
- List cars for sale with details like model, year, condition, mileage, price, images, and location
- Manage car listings (edit or remove)
- Receive notifications when buyers make payments

### Payment Process
- Direct UPI payments between buyers and sellers
- Buyers upload payment details and screenshots
- Sellers verify and approve/reject payments
- In-app notifications for payment status updates

### Admin Panel
- User management
- Car listing management
- Transaction monitoring
- Platform oversight

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (default), can be configured for PostgreSQL
- **Authentication**: Django's built-in authentication system
- **File Storage**: Django's file storage for car images and payment screenshots
- **Notifications**: In-app notification system

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/carmarket.git
   cd carmarket
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Usage

### For Sellers
1. Register an account or log in
2. Navigate to the dashboard and select "Sell Car"
3. Fill in the car details, upload images, and provide your UPI ID
4. Submit the listing
5. Manage your listings and respond to payment requests

### For Buyers
1. Register an account or log in
2. Browse available cars or use search filters to find specific cars
3. View car details and seller information
4. Click "Reserve Car" to initiate the purchase process
5. Make payment to the seller's UPI ID
6. Upload payment details and wait for seller approval

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django framework
- Bootstrap for responsive UI
- Font Awesome for icons 