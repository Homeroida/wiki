# Wiki

Wiki is a simple web application built with Django that allows users to create and edit encyclopedia entries using Markdown.



## Video Demo: https://youtu.be/sywQE4BoXpE


## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Project Description

Wiki is a Django-based web application that provides a platform for creating and editing encyclopedia entries. It utilizes Markdown for formatting the content of entries. Users can search for entries, view entry details, create new entries, and edit existing entries. The application follows a simple and user-friendly interface.

## Installation

To run the Wiki application locally, follow these steps: 

1. Clone the repository: `git clone https://github.com/Homeroida/wiki_n.git`
2. Navigate to the project directory: `cd wiki_n`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`
8. Access the application in your web browser at: `http://localhost:8000`

## Usage

Once the application is installed and running, you can perform the following actions:

- View the list of all encyclopedia entries on the home page.
- Click on an entry to view its contents in Markdown format.
- Use the search functionality to find specific entries.
- Create a new entry by clicking on "Create New Page" and providing a title and content.
- Edit an existing entry by clicking on the "Edit" link on the entry page and modifying the content.
- Click on "Random Page" in the sidebar to be taken to a random encyclopedia entry.

## Contact

For any inquiries or questions, you can reach me at chanishvili@gmail.com.

GitHub: [https://github.com/Homeroida/](https://github.com/Homeroida/)
