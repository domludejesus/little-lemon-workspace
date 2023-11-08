# Little Lemon Restaurant

## Description

Little Lemon Restaurant is a Django-based web application that provides an API for managing restaurant menus and bookings. It allows users to view the menu, make bookings, and perform other restaurant-related operations.

## Technologies Used

- Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs.
- PostgreSQL: A powerful, open-source object-relational database system.

## API Endpoints

The following API endpoints are available:

- `GET /restaurant/menu/`: Returns a list of all menu items.
- `GET /restaurant/booking/tables`: Returns a list of all tables and their availability.

## Testing

To test the API, you can use a tool like Postman. Here's how you can include the authorization token in your GET request:

1. Open Postman and select the GET request you want to send.
2. Click on the "Headers" tab.
3. In the "Key" field, enter "Authorization".
4. In the "Value" field, enter "Token " followed by your authorization token.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.

