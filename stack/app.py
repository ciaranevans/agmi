#!/usr/bin/env python3
import os

from aws_cdk import core

from stack import AgmiStack

tags = {
    "APPLICATION": "agmi",
    "ENV": os.environ.get("ENV", "dev"),
    "SOURCE": "https://github.com/ciaranevans/agmi",
    "ORG": "Development Seed",
}

app = core.App()
AgmiStack(app, f"agmi-{os.environ.get('ENV', 'dev')}")
_ = [core.Tag.add(app, key, val) for key, val in tags.items()]
app.synth()
