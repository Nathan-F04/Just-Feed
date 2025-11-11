# Just-Feed
A microservice application for the CICD2 project

## Project Setup

### Setting up a python virtual environment

````bash
python -m venv venv
````

Activate using:

````bash
source venv/Scripts/activate
````

### Installing dependancies

````bash
make install
````

Run the following commdand when adding new libraries

````bash
make freeze
````

### Starting application

The start/run commands are formatted as "make start/run" followed by the service desired i.e. "bank":

````bash
make run bank
````

````bash
make start bank:
````

````bash
make run login
````

````bash
make start login
````

````bash
make run notification
````

````bash
make start notification
````

````bash
make run order
````

````bash
make start order
````

````bash
make run profile
````

````bash
make start profile
````

````bash
make stop
````
### Running tests

````bash
make test
````