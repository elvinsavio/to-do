setup:
	python3.12 -m venv .venv;
	. .venv/bin/activate;
	pip3 install -r requirements.txt;
	npm install 

run:
	@if [ "$(VIRTUAL_ENV)" != "" ]; then\
		. .venv/bin/activate; \
		npm run dev; \
	else \
		npm run dev; \
	fi;\

clean:
	rm -rf ./.venv ./node_modules ./logs ./database