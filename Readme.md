# FastAPI Log Viewer

This project is a FastAPI application that records incoming GET and POST requests and writes them to a JSON file and presents these logs to the user via a web interface. This application is useful for visualizing and managing logs.

## Features

- Receives and records GET and POST requests.
- Displays the recorded logs via the web interface.
- Can read and write the log file saved in JSON format.

## Requirements

- Python 3.7 or later
- FastAPI
- Uvicorn (ASGI server)
- Jinja2 (for HTML templates)
- `pathlib` and `json` modules for JSON file management

## Getting Started

### 1. Virtual Environment Setup

```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### 2. Running the Application

```bash
uvicorn main:app --reload
```

This command will start the application in development mode and will be accessible at http://127.0.0.1:8000.

### 3. Endpoints

-   GET /test: Makes a GET request and records logs.

    Parameter: q (optional query parameter)

-   POST /test: Makes a POST request and saves the logs.

    Parameter: A payload in JSON format.

-   GET /logs: Returns the saved logs in JSON format.

-   GET /: Returns the web interface and visualizes the logs.

### 4. Viewing Logs

You can visualize the logs by going to http://127.0.0.1:8000 in the browser. The most recently added log is listed first.

Running with Docker

```bash
docker build -t fastapi-log-viewer .

docker run -d -p 8000:8000 fastapi-log-viewer
```