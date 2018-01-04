This is a dataset about primary tumors in people. 
Locations of primary tumors are locations in body where the tumor first appeared 
and from there started to metastasize to other parts of the body.

## Data

This dataset was found on [OpenML - primary-tumor](https://www.openml.org/d/171)

This primary tumor domain was obtained from the University Medical Centre, 
Institute of Oncology, Ljubljana, Yugoslavia. Thanks go to 
M. Zwitter and M. Soklic for providing the data.
_Please include this citation if you plan to use this database.

Data is located in directory `data`

`data/primary-tumor.csv`

## Preparation

To get our output data several things are done to input data:
* missing values marked with "?" are replaced with ""(empty space)
* all " are removed
* all ' are removed
* yes and no values are replaced with true and false

Scripts are in directory `scripts`

`scripts/main.py`

## License
Licensed under the [Public Domain Dedication and License][pddl] (assuming
either no rights or public domain license in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/