#!/bin/bash

mkdir -p ../../notlikecalc-1.0/src
cp ./calculator.py ../../notlikecalc-1.0/src
cp ./calc_ui.py ../../notlikecalc-1.0/src
cp ./mathlib.py ../../notlikecalc-1.0/src
mkdir -p ../../notlikecalc-1.0/install
cp ../install/* ../../notlikecalc-1.0/install
cd ../../notlikecalc-1.0
tar -czvf ../notlikecalc-1.0.tar.gz ../notlikecalc-1.0
dh_make -e xmatus37@vutbr.cz -y -c gpl -n -s -f ../notlikecalc-1.0.tar.gz
mv -f ./install/install ./debian
mv -f ./install/control ./debian
dpkg-buildpackage -rfakeroot -uc -b
cd ..
rm -r notlikecalc-1.0 notlikecalc-1.0.tar.gz notlikecalc_1.0_amd64.buildinfo notlikecalc_1.0_amd64.changes
mkdir install
mv *.deb ./install/notlikecalc-1.0.deb
