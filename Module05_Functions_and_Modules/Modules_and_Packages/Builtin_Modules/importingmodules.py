# Syntax:
# from <packagename> import <module_name>
# datetime # (Package)
#     -> datetime (datetime.py) # (Module)
#         -> today() # Definition

from datetime import datetime
# Use asterisk(*) to import all modules and subpackages in a package
# from openpyxl import chart
# from openpyxl import styles
from openpyxl import *

print(datetime.today()) # modulename.definitionname()