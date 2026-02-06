#!/usr/bin/env python3
"""Simple repository SRS validation checks.

This script implements lightweight checks from the SRS verification checklist.
It does not prove runtime behaviors (e.g., re-planning) but verifies repository
artifacts and obvious references that help automation and reviewers.
"""
import os
import sys
import re
import json


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def find_files(name):
    matches = []
    for dirpath, _, filenames in os.walk(ROOT):
        if name in filenames:
            matches.append(os.path.join(dirpath, name))
    return matches

def grep_keyword(keyword):
    found = []
    pat = re.compile(re.escape(keyword), re.IGNORECASE)
    for dirpath, _, filenames in os.walk(ROOT):
        for fn in filenames:
            if fn.endswith(('.py', '.md', '.yaml', '.yml', '.json', '.ts', '.js')):
                path = os.path.join(dirpath, fn)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        txt = f.read()
                    if pat.search(txt):
                        found.append(path)
                except Exception:
                    pass
    return found

def extract_json_codeblocks():
    """Extract JSON code-blocks from markdown files and return parsed JSON objects."""
    objs = []
    codeblock_re = re.compile(r'```json\s*(\{.*?\})\s*```', re.DOTALL | re.IGNORECASE)
    for dirpath, _, filenames in os.walk(ROOT):
        for fn in filenames:
            if fn.endswith('.md'):
                path = os.path.join(dirpath, fn)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        txt = f.read()
                    for m in codeblock_re.finditer(txt):
                        blob = m.group(1)
                        try:
                            parsed = json.loads(blob)
                            objs.append((path, parsed))
                        except Exception:
                            # skip invalid JSON blocks
                            pass
                except Exception:
                    pass
    return objs

def check_task_schema_object(obj):
    required_keys = {'task_id', 'task_type', 'priority', 'context', 'assigned_worker_id', 'created_at', 'status'}
    return required_keys.issubset(set(obj.keys()))

def check_task_schema_present():
    # First try to find well-formed JSON code blocks that match the task schema
    objs = extract_json_codeblocks()
    for path, obj in objs:
        if isinstance(obj, dict) and check_task_schema_object(obj):
            return True
    # Fallback: look for the task_id string anywhere
    hits = grep_keyword('"task_id"')
    return len(hits) > 0

def main():
    ok = True
    failures = []

    # Required files
    required = [
        os.path.join(ROOT, 'specs', 'technical.md'),
        os.path.join(ROOT, 'specs', 'functional.md'),
        os.path.join(ROOT, 'specs', 'openclaw_integration.md'),
        os.path.join(ROOT, '.cursor', 'srs_alignment_prompt.md'),
    ]
    for r in required:
        if not os.path.isfile(r):
            ok = False
            failures.append(f'Missing required file: {r}')

    # SOUL.md presence somewhere in repo
    soul_files = find_files('SOUL.md')
    if not soul_files:
        ok = False
        failures.append('No SOUL.md files found (agents must have SOUL.md)')

    # Skills directory exists
    skills_dir = os.path.join(ROOT, 'skills')
    if not os.path.isdir(skills_dir):
        ok = False
        failures.append(f'Missing skills directory: {skills_dir}')

    # Memory infra mentions
    redis_hits = grep_keyword('redis')
    weaviate_hits = grep_keyword('weaviate')
    if not redis_hits:
        failures.append('No references to Redis found (short-term memory)')
    if not weaviate_hits:
        failures.append('No references to Weaviate found (long-term memory)')

    # Policy and keyword checks (HITL, CFO, Coinbase, AgentKit, native_transfer)
    keywords = ['HITL', 'human-in-the-loop', 'CFO', 'budget', 'coinbase', 'agentkit', 'native_transfer', 'deploy_token', 'get_balance']
    keyword_hits = {}
    for kw in keywords:
        hits = grep_keyword(kw)
        if hits:
            keyword_hits[kw] = hits

    # Warn (but don't fail) if critical keywords are missing
    missing_critical = []
    for critical in ['HITL', 'CFO', 'coinbase', 'agentkit']:
        if critical.lower() not in [k.lower() for k in keyword_hits.keys()]:
            missing_critical.append(critical)
    if missing_critical:
        failures.append('Missing references for critical keywords: ' + ', '.join(missing_critical))

    # Check task schema snippet
    if not check_task_schema_present():
        ok = False
        failures.append('Task schema JSON snippet not found (search for "task_id")')

    # OpenClaw integration file
    openclaw = os.path.join(ROOT, 'specs', 'openclaw_integration.md')
    if not os.path.isfile(openclaw):
        ok = False
        failures.append('Missing OpenClaw integration spec')

    # Print results
    if ok and not failures:
        print('SRS validation: OK')
        return 0
    else:
        print('SRS validation: FAIL')
        for f in failures:
            print('- ' + f)
        # Also print hints where we found related references (non-failing)
        if redis_hits:
            print('\nFound Redis references in:')
            for p in redis_hits[:10]:
                print('  - ' + p)
        if weaviate_hits:
            print('\nFound Weaviate references in:')
            for p in weaviate_hits[:10]:
                print('  - ' + p)
        if keyword_hits:
            print('\nFound keyword occurrences:')
            for k, paths in keyword_hits.items():
                print(f'  - {k}: {len(paths)} files (examples: {paths[:3]})')
        return 1

if __name__ == '__main__':
    sys.exit(main())
