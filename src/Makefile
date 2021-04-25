.PHONY = all clean test doc run profile
SRCTEST = mathlibtests.py

all: run

#run calculator
run: calculator.py
	python3 calculator.py

#run mathlib tests
test: $(SRCTEST)
	python3 -m unittest -v mathlibtests

#generate doxygen documentation
doc: Doxyfile
	cd .. && rm -r -f ./doc
	doxygen
	mv doc ../
	mv warning_doxygen.txt ../doc

#run profiling program
profile: profiling.py
	python3 profiling.py

installer: calculator.py  calc_ui.py mathlib.py
	bash install.sh

clean: 
	rm -r -f __pycache__ ../doc warning_doxygen.txt
