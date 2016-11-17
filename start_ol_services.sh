#!/bin/bash
qjackctl & 
./openlase/build/output/output & 
./openlase/build/tools/simulator &
./lasershark_hostapp/lasershark_jack &
