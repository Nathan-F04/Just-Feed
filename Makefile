# Minimal Makefile with start/stop
BANK_APP = Src.banking_service.banking:app
LOGIN_APP = Src.banking_service.banking:app
NOTIF_APP = Src.banking_service.banking:app
ORDER_APP = Src.banking_service.banking:app
PROFILE_APP = Src.banking_service.banking:app
PID_FILE = .uvicorn.pid

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run bank:
	python -m uvicorn $(BANK_APP) --host 0.0.0.0 --port 8000 --reload

start bank:
	nohup python -m uvicorn $(BANK_APP) --host 0.0.0.0 --port 8000 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Uvicorn started (PID=$$(cat $(PID_FILE))) on http://localhost:8000"
	
	run bank:
	python -m uvicorn $(BANK_APP) --host 0.0.0.0 --port 8000 --reload

run login:
	python -m uvicorn $(LOGIN_APP) --host 0.0.0.0 --port 8000 --reload

start login:
	nohup python -m uvicorn $(LOGIN_APP) --host 0.0.0.0 --port 8000 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Uvicorn started (PID=$$(cat $(PID_FILE))) on http://localhost:8000"

run notification:
	python -m uvicorn $(NOTIF_APP) --host 0.0.0.0 --port 8000 --reload

start notification:
	nohup python -m uvicorn $(NOTIF_APP) --host 0.0.0.0 --port 8000 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Uvicorn started (PID=$$(cat $(PID_FILE))) on http://localhost:8000"

run order:
	python -m uvicorn $(ORDER_APP) --host 0.0.0.0 --port 8000 --reload

start order:
	nohup python -m uvicorn $(ORDER_APP) --host 0.0.0.0 --port 8000 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Uvicorn started (PID=$$(cat $(PID_FILE))) on http://localhost:8000"

run profile:
	python -m uvicorn $(PROFILE_APP) --host 0.0.0.0 --port 8000 --reload

start profile:
	nohup python -m uvicorn $(PROFILE_APP) --host 0.0.0.0 --port 8000 --reload \
	> .uvicorn.out 2>&1 & echo $$! > $(PID_FILE)
	@echo "Uvicorn started (PID=$$(cat $(PID_FILE))) on http://localhost:8000"

stop:
	@if [ -f $(PID_FILE) ]; then \
 	kill $$(cat $(PID_FILE)) && rm -f $(PID_FILE) && echo "Uvicorn stopped."; \
	else \
 	echo "No PID file found. Did you use 'make start'?"; \
	fi

test:
	python -m pytest -q