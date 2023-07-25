# DergDev's Python API Boiler-plate

Based on APIs made in the paste, this boilerplate embark the necessary tools and depedencies to deploy a test ready API right away.
Please duplicate and use at your own convenance, don't forget to edit the following README.

## Dependencies

- [Flask](https://pypi.org/project/Flask/): Flask is a lightweight WSGI web application framework.
- [Flasgger](https://pypi.org/project/flasgger/): Flasgger is a Flask extension to extract OpenAPI-Specification from your API.
- [Apispec](https://pypi.org/project/apispec/): A pluggable API specification generator. (For Marshmallow)
- [Marshmallow](https://pypi.org/project/marshmallow/): Marshmallow is an ORM/ODM/framework-agnostic library.
- [Flask-marshmallow](https://pypi.org/project/flask-marshmallow/): Flask integration of the Marshmallow lib
- [Pathlib](https://pypi.org/project/pathlib/): Pathlib is a smart path handler for easy file access.
- [Python-dotenv](https://pypi.org/project/python-dotenv/): DotEnv is a environment variables setter/ reader.
- [Requests](https://pypi.org/project/requests/): Requests is a simple, HTTP library for Python.
- [Urllib3](https://pypi.org/project/urllib3/): Urllib3 is a powerful, user-friendly HTTP client for Python.
- [Gunicorn](https://pypi.org/project/gunicorn/): Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.
- [Gunicorn_color](https://pypi.org/project/gunicorn_color/): A simple access logger for Gunicorn with termcolor support.

## How to deploy locally
```sh
- make install
- make build_wsgi
- make deploy_serve_wsgi
``` 

## How to undeploy locally
```sh
- make undeploy_wsgi
``` 

[Health](http://127.0.0.1:5000/) for the health endpoint api

[Api Docs](http://127.0.0.1:5000/apidocs) for the swagger documentation

## .env file parameters

This project uses [python-dotenv](https://pypi.org/project/python-dotenv/), the project will need to have the following
parameters set to work.
You may have to create one in your project if the dev team didn't share you one.

```sh
DEFAULT_VALUE_TO_USE='test'
API_KEY='api_key'
```

## Tests

The code is covered by tests, to run the tests please execute

``` sh

```

## Postman Collection

None (yet)

