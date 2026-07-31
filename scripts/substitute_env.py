import os
import sys
from pathlib import Path
from string import Template

template_path, output_path = sys.argv[1], sys.argv[2]
text = Path(template_path).read_text()
Path(output_path).write_text(Template(text).substitute(os.environ))
