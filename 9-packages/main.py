import sys
from analytics import calculator

from analytics.calculator import add
from analytics.formatter.nbf import bold_text

result_sum = add(10,5)

format_it = bold_text("my text 223")

# cwd, pythonpath, site-package (pi)

for pathh in sys.path:
    print(pathh)