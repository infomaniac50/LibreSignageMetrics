#!/usr/bin/env bash

python makeDOT.py dist/ 1 builds/includes.dot
gv2gml -o builds/includes.gml builds/includes.dot
sed -i -e 's/name/label/' builds/includes.gml
