# Google Search Stocks API

This folder contains the code for Google Search Stocks' backend API, which is written in Python using FastAPI.

## Running with Docker (Recommended)

Build and run the api with the provided `Dockerfile`.

```
docker build --target bin -t search-stocks-api .
```

```
docker run -p 8000:8000 search-stocks-api
```

The port that the server runs on can be configured with the `$PORT` environment variable (not necessary if running locally, just change the first port for the `-p` flag).

```
docker run -p 5000:5000 -e PORT=5000 search-stocks-api
```

## Running in a Development Environment

The server can be run in a working python environment.

### Installing Dependencies

This project requires Python 3 in order to run. Use pip to install the required packages for a development environment.

```
pip install requirements.txt
```

### Running the Server

Use Uvicorn to start the server in a development environment:

```
uvicorn api.main:app
```

This will start the server running on localhost at port 8000. Tests for this application are all located under the `tests/` folder, and can be run with PyTest. (TESTS ARE FOR AN OLD PROJECT AND WILL CURRENTLY FAIL).

```
python -m pytest tests/
```

## Documentation

You can view documentation for all resources at the `/docs` endpoint. Sending a `GET` request to the root endpoint will return a welcome message.
