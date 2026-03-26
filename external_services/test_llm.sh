#!/bin/bash

curl -X POST http://127.0.0.1:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"messages":[{"role":"user","content":"How much can a woodchuck chuck if a wood chuck could chuck wood?"}]}'