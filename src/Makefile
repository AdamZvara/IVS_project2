.PHONY = all clean test doc run profile pack
SRCTEST = mathlibtests.py
TEAM_PACK = xeichl01_xkorva03_xmatus37_xzvara01

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
	rm -rf ../../doc/
	mv ../doc ../../

#pack project so it can be handed over
pack: clean doc installer
	rm -rf ../../$(TEAM_PACK).zip 
	mkdir -p ../../$(TEAM_PACK)/doc && cp -ar ../../doc/. ../../$(TEAM_PACK)/doc
	mkdir -p ../../$(TEAM_PACK)/repo && cp -r ../../ivs-project2/. ../../$(TEAM_PACK)/repo
	mkdir ../../$(TEAM_PACK)/install && cp -r ../../install/. ../../$(TEAM_PACK)/install
	cd ../.. && zip -qr $(TEAM_PACK).zip $(TEAM_PACK)
	cd ../.. && rm -rf $(TEAM_PACK)
#run profiling program
profile: profiling.py
	python3 profiling.py

#make install folder with .deb package
installer: calculator.py  calc_ui.py mathlib.py
	rm -rf ../../install
	bash install.sh

clean: 
	rm -r -f __pycache__ ../../doc ../../install warning_doxygen.txt ../../$(TEAM_PACK)
