Cricbuzz Clone - Python Web Application
Welcome to the Cricbuzz Clone project! This is a simple Python web application built using the Flask framework, designed to display live cricket scores in a user-friendly interface. The project is set up to be flexible, allowing easy deployment on a Virtual Machine (VM) or through Docker. This application uses an in-memory database (SQLite) and is structured to support future microservices.

Table of Contents
Project Structure
Getting Started
Prerequisites
Installation
Running the Application
On a Virtual Machine (VM)
Using Docker
Testing
Future Enhancements
Contributing
License

Explanation
app/: Contains the core application code.

__init__.py: Initializes the Flask app and configures the in-memory database.
routes.py: Defines the routes (URLs) and the corresponding views (what the user sees).
templates/: Contains HTML files for the user interface.
static/: Contains static files like CSS for styling.
tests/: Contains unit tests to ensure the application works as expected.

Dockerfile: Instructions to build a Docker image for the application.

requirements.txt: Lists all the Python dependencies needed to run the application.

run.py: The main file to start the Flask application.


Getting Started
Prerequisites
To run this application, you need to have the following installed on your system:

Python 3.7+
pip (Python package installer)
Docker (optional, if you plan to run the application using Docker)



Installation
Clone the Repository:

git clone https://github.com/yourusername/cricbuzz_clone.git
cd cricbuzz_clone
Install Python Dependencies:

pip install -r requirements.txt

## Running the Application
        On a Virtual Machine (VM)
        python run.py
## Access the Application:
    Open your web browser and go to http://localhost:5000

## Using Docker

        Using Docker
        Build the Docker Image:

        docker build -t cricbuzz-clone .
        Run the Docker Container:


        docker run -d -p 5000:5000 cricbuzz-clone
        Access the Application:

        Open your web browser and go to http://localhost:5000

## Testing
Unit tests are provided to ensure the application works correctly.

## Run the Tests:


python -m unittest discover tests


Check the Test Output:

All tests should pass successfully, confirming that the routes and views are working as expected.