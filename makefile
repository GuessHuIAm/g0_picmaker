make:
	python3 picmaker.py

openpic:
	export DISPLAY=:0.0
	eog picture.ppm
