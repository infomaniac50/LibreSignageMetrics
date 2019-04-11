#!/usr/bin/env bash

python makeDOT.py dist/ 1 libresignageIncludes.dot
gv2gml -o libresignageIncludes.gml libresignageIncludes.dot
sed -i -e 's/name/label/' libresignageIncludes.gml
