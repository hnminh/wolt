# Wolt Backend Summer 2021 Engineering Internship

This is my solution for [Wolt's Summer 2021 Internship assignment](https://github.com/woltapp/summer2021-internship)

## Requirements

* Python 3
* Flask

```
    pip install flask
```

## Usage

To start the API, in the terminal, run

```
    python3 main.py
```

From the status message retrieve the "Running on" address (similiar to below):

```
    python3 main.py

        Serving Flask app "main" (lazy loading)
        Environment: production
        WARNING: This is a development server. Do not use it in a production deployment.
        Use a production WSGI server instead.
        Debug mode: off
        Running on http://localhost:50000/ (Press CTRL+C to quit)
```

Access the API, with request parameters. For example

```
    http://localhost:50000/discovery?lat=60.1709&lon=24.941
```

Server will return data in JSON format