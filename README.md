# E-commerce Web Application

This is an e-commerce web application built using Django, designed to showcase products and allow users to add items to their shopping cart for purchase.

## Features

- User registration and authentication
- Product listing with details and images
- Shopping cart functionality
- Checkout process with payment integration
- User profile management
- Order history tracking

## Installation

1. Clone the repository: `git clone https://github.com/Ketan692/ecommercewebsite.git`
2. Install the project dependencies: `pip install -r requirements.txt`
3. Configure the database settings in `settings.py`
4. Apply database migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage

1. Access the web application through your browser at `http://localhost:8000`
2. Create a new user account or log in with an existing account
3. Browse the product catalog and view individual product details
4. Add products to your shopping cart
5. Proceed to checkout to complete the purchase
6. View your order history and manage your user profile

## Configuration

- Database: The default configuration uses SQLite. You can change it to your preferred database system by updating the `DATABASES` setting in `settings.py`.
- Payment Integration: The project uses a dummy payment gateway by default. To integrate with a real payment gateway, update the relevant settings in `settings.py` and follow the payment gateway's documentation.

## Troubleshooting

- If you encounter any issues or errors, please refer to the project's issue tracker on GitHub to see if there are any reported solutions or open a new issue if needed.

## Contributing

- Contributions are welcome! If you find a bug or have an enhancement in mind, please submit a pull request or open an issue on GitHub.

## Contact

For any questions or inquiries, please contact ketancoder@yahoo.com(mailto:ketancoder@yahoo.com).

