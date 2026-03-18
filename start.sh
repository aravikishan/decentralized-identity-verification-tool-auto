#!/bin/bash
set -e
echo "Starting Decentralized Identity Verification Tool..."
uvicorn app:app --host 0.0.0.0 --port 9119 --workers 1
