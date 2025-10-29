# Car Charging Reservation System


## Running Locally (with Python)

1. **Install Python 3.13 and pip**
2. Install dependencies (choose one):
	```bash
	cd monolith
	python -m venv .venv
	source .venv/bin/activate
	pip install .
	# OR, with uv (faster alternative to pip):
	uv sync
	```
3. Run the application (choose one):
	- **With Python:**
		```bash
		python src/main.py
		```
    
4. Visit [http://localhost:8080](http://localhost:8080) in your browser.

## Running with Docker

1. **Build the Docker image:**
	```bash
	docker build -t car-charging-monolith ./monolith
	```
2. **Run the container:**
	```bash
	docker run -p 8080:8080 car-charging-monolith
	```
3. Visit [http://localhost:8080](http://localhost:8080) in your browser.

## Running with Docker Compose (if available)

1. From the project root, run:
	```bash
	docker compose up
	```
2. Visit [http://localhost:8080](http://localhost:8080) in your browser.

---
For development, make sure to restart the server after code changes if not using `--reload`.
