#!/bin/bash
cd "$(dirname "$0")/.."
source myenv/bin/activate
python chat-scripts/chat_pipeline.py