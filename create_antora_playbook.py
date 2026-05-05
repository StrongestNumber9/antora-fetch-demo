import yaml
import json
import glob
import os
from pathlib import Path

stub = yaml.safe_load(open("antora-playbook-stub.yml").read())
runner_temp=os.getenv("RUNNER_TEMP")

for tagfile in glob.glob(f"{runner_temp}/tags/*.json"):
    tags = json.loads(open(tagfile).read())
    name = Path(tagfile).stem
    source = { "url": f"{runner_temp}/repos/{name}", "tags": tags, "branches": ["!*"] }
    stub["content"]["sources"].append(source)
print(yaml.dump(stub))
