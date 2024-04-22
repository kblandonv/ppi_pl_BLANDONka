# Simple Chat App using Django

This is a simple chat application built using Django framework. It allows users to join chat rooms and exchange messages in real-time.

## Features

- **User Authentication:** Users can register, log in, and log out.
- **Chat Rooms:** Users can create chat rooms or join existing ones.
- **Real-Time Messaging:** Messages are delivered instantly using WebSocket technology.
- **User Permissions:** Chat room creators can set permissions for who can join and send messages.

## Technologies Used

- **Django:** Backend framework for handling user authentication, chat rooms, and messages.
- **Django Channels:** Used for WebSocket communication and real-time messaging.
- **HTML/CSS/JavaScript:** Frontend components for user interface and interactions.
- **SQLite/PostgreSQL:** Database for storing user data, chat rooms, and messages.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/kblandonv/ppi_pl_BLANDONka.git

2. Navigate to the project directory:
   ```sh
   cd simple-chat-app

3. Create a virtual environment:
   ```sh
   python -m venv venv

4. Activate the virtual environment:
   On Windows:
   ```sh
   venv\Scripts\activate
   On macOS/Linux:
   ```sh
   source venv/bin/activate

5. Install dependencies:
   ```sh
   pip install -r requirements.txt

6. Apply migrations:
   ```sh
   python manage.py migrate

7. Run the development server:
   ```sh
   python manage.py runserver

## Usage
Open your web browser and navigate to http://localhost:8000.
Register a new account or log in if you already have one.
Create a new chat room or join an existing one.
Start sending messages in the chat room.
