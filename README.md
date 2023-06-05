# H3-Scenario-Tag-Tree-Exporter
This script exports the tag tree for .scenario tag files for the H3EK into a new folder. This is helpful for sharing all the relevant scenario tag files. When copying shared tags to your main tags folder, always be mindful of duplicate tags. It is always recommended to keep a backup of your main tags folder.

Note: You need to have Python installed on your computer to run this script.

1. After compiling the relevant scenario using the H3EK tools, locate the `scenario_tags.txt` saved in `H3EK\reports\<scenario_name>`
2. Place `scenario_tags.txt` in the same folder as the `export_h3_tag_tree.py` script, along with the included `common_tags.txt` and `tags folder location.txt`.
3. Open the `tags folder location.txt` file inluded in the same folder as the script, and make sure it contains the correct path to your H3EK tags folder, as a single line of text. For example, if your files are located in `C:\Program Files (x86)\Steam\steamapps\common\H3EK\tags`, then `tags folder location.txt` should contain this line:
```
C:\Program Files (x86)\Steam\steamapps\common\H3EK\tags
```
3. Run the script using Python.
4. When prompted, enter the name of the custom directory where you want to save the exported tag tree. This folder will be created in the same folder as the script.
6. The script will save all of the relevant tags from 'the scenario_tags.txt' file inside of the new directory. It will also save a list of exported tags to a file called `tags_to_be_exported.txt` and log any missing tags to a file called `debug_missing tags.txt`.
7. When the script has finished running, it will wait for you to press Enter before exiting.

This script might be functional for other Halo mod tools, but has not been tested for them.
