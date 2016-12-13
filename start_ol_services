#!/bin/bash
qjackctl & 
echo "-----------Plug in the first lasershark (usb portXXX)-------------"
read -p "Press 'Enter' when ready..." temp
./openlase/build/output/output & 
./openlase/build/tools/simulator &
./lasershark_hostapp/lasershark_jack &
sleep 1 
echo "-----------Plug in the second lasershark (usb portXXX)------------"
read -p "Press 'Enter' when ready..." temp
./openlase/build/output/output & 
./openlase/build/tools/simulator &
./lasershark_hostapp/lasershark_jack &
