setup:
	mkdir database
	python3.12 -m venv .venv;
	. .venv/bin/activate;
	pip3 install -r requirements.txt;
	npm install 
	flask init
	

start_server:
	npm run tailwind & flask run --debug

run:
	@if [ "$(VIRTUAL_ENV)" != "" ]; then\
		. .venv/bin/activate; \
		make start_server; \
	else \
		make start_server; \
	fi;\

clean:
	rm -rf ./.venv ./node_modules ./logs ./database