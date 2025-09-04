# WeatherNow- Flask Web App

A simple Python web application that allows users to check the current weather of any city. It pulls live data from the OpenWeatherMap API to show the temperature, weather conditions, and a corresponding weather icon.

This project was initially built as a desktop application with Tkinter and has been refactored into a web application using the Flask framework for server deployment.

## Features

*   **Real-time Weather:** Get live weather data for any city by entering its name.
*   **Weather Details:** Displays the current temperature in Celsius, a weather description, and a visual icon.
*   **Web-based Interface:** The application runs on a web server, allowing access through a browser.
*   **Error Handling:** Provides user-friendly error messages for invalid city names or failed API requests.

## Technologies Used

*   **Python:** The core programming language for the application logic.
*   **Flask:** A lightweight web framework used to build the web application.
*   **OpenWeatherMap API:** Used to fetch real-time weather data.
*   **Requests:** A Python library for making HTTP API calls.
*   **Pillow:** Used for handling and displaying weather icons.
*   **Gunicorn:** A production web server used by Render.

## Installation and Local Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/SanKrishnan/WeatherNow.git
    cd weather-dashboard
    ```

2.  **Set up a virtual environment** (recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Run the application locally:**
    ```sh
    flask run
    ```
    The application will be running at `http://127.0.0.1:5000/`.

## Deployment on Render


## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/SanKrishnan/WeatherNow/issues).

## License

This project is licensed under the [MIT License](https://github.com/SanKrishnan/WeatherNow/LICENSE).
