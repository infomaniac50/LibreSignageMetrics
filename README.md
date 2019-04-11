
## Static Analysis of eerotal/LibreSignage

dependencies2dot.py was derived from http://blog.humaneguitarist.org/2011/07/30/making-a-dot-graph-for-php-include-statements/

## Running the Analysis

- Build the LibreSignage repository.
- Copy dist/ to this directory.
- Create a directory called builds/
- Use ``bash build_gml.sh`` to create a GML file.
- Use yEd to load the GML file
- Group and sort each file according to it's position in the directory hierarchy.
  - If a file is alone in a directory then that file is not grouped.
- Save as a GraphML file and export to SVG.