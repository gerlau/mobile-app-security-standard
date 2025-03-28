## Overview 
This document outlines the key functions within the compliance-trestle/trestle library that enable the translation of catalog models in JSON format into Markdown format. Below is the sequence of the key functions:

1. CatalogAPI.write_catalog_as_markdown()
2. CatalogWriter.write_catalog_as_catalog()
3. CatalogWriter.write_control_into_dir()
4. ControlWriter.write_control_for_editing()
    - self._add_control_statement()
    - self._add_control_objective()
    - self._add_sections()

## Breakdown of function calls

### Control Statement - self._add_control_statement()
- title = f'{control_id} -{group_name} {control_title}'
- header_title = 'Control Statement'
- add_part_and_its_items(), for each control.parts
    - if part.name=statement && if part.prose, add part.prose
    - if part.name/=statement like part.name=item, it will be added on as a list item (remember to add lables like a., 1.)

### Control Objective - self._add_control_objective()
- heading_title = 'Control Assessment Objective'
- add_part_and_its_items(), for each control.parts
    - if part.name=assessment-objective && if part.prose, add part.prose
    - if part.name/=assessment-objective like part.name=item, it will be added on as a list item (remember to add lables like a., 1.)

### Control Section - self._add_sections()
- add_sections(), for each control.parts
    - if part.prose && part.name not in ['statement', 'item', 'objective', 'assessment-objective']
    - title = 'Control {title}'
    - add part.prose