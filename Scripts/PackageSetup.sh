#!/bin/bash
# Checks and installs all packages needed for UpdatePlots.py to run

pip3 install selenium
pip3 install beautifulsoup4
pip3 install Plotly
pip3 install pandas
pip3 install psutil
pip3 install requests
conda install -c plotly plotly-orca
/Applications/Python\ 3.7/Install\ Certificates.command
