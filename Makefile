# Microservice Makefile
BANK_APP = Src.banking_service.banking:app
LOGIN_APP = Src.login_service.login:app
NOTIF_APP = Src.notification_service.notification:app
ORDER_APP = Src.order_service.orders:app
PID_FILE = .uvicorn.pid

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run-bank:
	python -m uvicorn $(BANK_APP) --host 0.0.0.0 --port 8000 --reload

start-bank:
	nohup python -m uvicorn $(BANK_APP) --host 0.0.0.0 --port 8000 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Banking service started (PID=$$(cat $(PID_FILE))) on http://localhost:8000"

run-login:
	python -m uvicorn $(LOGIN_APP) --host 0.0.0.0 --port 8001 --reload

start-login:
	nohup python -m uvicorn $(LOGIN_APP) --host 0.0.0.0 --port 8001 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Login service started (PID=$$(cat $(PID_FILE))) on http://localhost:8001"

run-notification:
	python -m uvicorn $(NOTIF_APP) --host 0.0.0.0 --port 8002 --reload

start-notification:
	nohup python -m uvicorn $(NOTIF_APP) --host 0.0.0.0 --port 8002 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Notification service started (PID=$$(cat $(PID_FILE))) on http://localhost:8002"

run-order:
	python -m uvicorn $(ORDER_APP) --host 0.0.0.0 --port 8003 --reload

start-order:
	nohup python -m uvicorn $(ORDER_APP) --host 0.0.0.0 --port 8003 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Order service started (PID=$$(cat $(PID_FILE))) on http://localhost:8003"

# Legacy compatibility (will show usage message)
run:
	@echo "Usage: make run-[service] where service is: bank, login, notification, order"

start:
	@echo "Usage: make start-[service] where service is: bank, login, notification, order"

stop:
	@if [ -f $(PID_FILE) ]; then \
	kill $$(cat $(PID_FILE)) && rm -f $(PID_FILE) && echo "Service stopped."; \
	else \
	echo "No PID file found. Did you use 'make start-[service]'?"; \
	fi

test:
	python -m pytest -q