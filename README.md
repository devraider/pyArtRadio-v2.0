# pyArtRadio 2.0 - Python automation script

This is the automation script for a newer version of ArtRadio (for first version you can check [djangoArtRadio V1](https://github.com/devraider/djangoArtRadio-v1.0.0)).

ArtRadio it's an ad-free online radio player.


> [!note]
> This project using:
> - JavaScript, Angular framework as frontend – code could be found: [ngArtRadio - Angular](https://github.com/devraider/ngArtRadio-v2.0)
> - Java, Spring boot framework as backend – code could be found: [javaArtRadio - Springboot](https://github.com/devraider/javaArtRadio-v2.0)


## Features

- **Automated Song Scraping**: Uses Selenium to access radio websites and capture currently playing song details.
- **Database Storage**: Saves song information in a database for easy tracking and future analysis.
- **Request Management**: Manages requests efficiently by patiently waiting on the website for updates without overloading the radio station.
- **Clever Auto-Refresh**: Refreshes the browser tab intelligently with Selenium to handle situations where the station stops updating songs.
- **Data Validation**: Utilizes Pydantic to ensure accurate and consistent data handling before adding entries to the database.

## Technologies Used

- **MySQL**: Relational database for storing ecommerce data.
- **Selenium**: Web scraping, with `Chromium Driver` for browser automation.
- **SQLAlchemy**: ORM for managing MySQL database interactions.
- **Pydantic**: For data validation and management within Python models.

## Getting Started

### Prerequisites

- **Python 3.11**
- **MySQL**: Installed and running for database management.


### Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/devraider/pyArtRadio-v2.0.git
   cd pyArtRadio-v2.0.git
   ```

2. **Prepare Environment**
    ```bash
   python -m venv .venv
   source .venv/bin/activation
   python install -r requirements.txt
   ```

3. **Configure Database:**
    - Ensure your MySQL server is running.
    - `.env` file with your MySQL credentials.

4. **Run the Application:**
   ```bash
    python main.py
   ```
