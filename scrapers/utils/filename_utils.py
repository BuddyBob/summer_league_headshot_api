#!/usr/bin/env python3
import re

def clean_filename(name: str) -> str:
    clean_name = name.strip().strip('"')
    clean_name = re.sub(r'[^\w\s\-\']', '', clean_name)
    return re.sub(r'[-\s]+', '_', clean_name)
