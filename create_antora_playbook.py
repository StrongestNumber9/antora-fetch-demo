import yaml
import json
import glob
import os
from pathlib import Path

stub = yaml.safe_load(open("antora-playbook-stub.yml").read())

for tagfile in glob.glob(f"{os.getenv("RUNNER_TEMP")}/tags/*.json"):
    tags = json.loads(open(tagfile).read())
    name = Path(tagfile).stem
    source = { "url": f"https://github.com/StrongestNumber9/{name}.git", "tags": tags, "branches": ["!*"] }
    stub["content"]["sources"].append(source)

print(yaml.dump(stub))
