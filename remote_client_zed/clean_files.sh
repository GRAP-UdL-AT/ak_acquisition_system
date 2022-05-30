#/bin/bash!

# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

echo "Cleaning recorded gata and logs!!!"
rm -Rf ./recorded_gnss/*
rm -Rf ./recorded_video/*
rm -Rf ./log/*