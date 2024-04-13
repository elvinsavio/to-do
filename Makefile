setup:
	python3.12 -m venv .venv;
	. .venv/bin/activate;
	pip3 install -r requirements.txt;


run:
	npm run tailwind & flask run --debug && fg