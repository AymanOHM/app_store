# App Store Project

A web-based application store where users can browse, purchase, and review various applications. Developers can also add and manage their applications.
The project is built using Flask for the backend and Microsoft SQL Server for the database.

## Database Initialization

To initialize the database, execute the SQL code in [`sql_initialization`](sql_initialization/) directory using Microsoft SQL Server in the order:
1. [`DDL.sql`](sql_initialization/DDL.sql) : To create Database and Tables
2. [`DML.sql`](sql_initialization/DML.sql) :
   1. To fill the tables with some data (Optional)
   2. To create the stored procedures needed (Mandatory)

## Features

### As a User:
- User registration and authentication
- Application browsing and searching
- Purchasing Applications
- User reviews and ratings

### As a Developer:
- Add and Manage your apps on the appstore

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AymanOHM/app_store.git
    ```
2. Navigate to the project directory:
    ```sh
    cd app_store
    ```
3. Initialize the database by executing the provided SQL code in Microsoft SQL Server.

4. Modify contents of `get_db_connection' function in [methods/database.py](methods/database.py) with your database credentials.

5. Run [`app.py`](app.py)

6. Access the website using: [`https://127.0.0.1:5000`](https://127.0.0.1:5000)

## Usage

1. Register a new user account.
2. Browse the available applications.
3. Add your applications to the cart.
4. Access the cart and Checkout.
5. Leave reviews and ratings for the applications you have used.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
*or just treat it as it's yours* :)