#!/usr/bin/env bash
port="8000"
uvicorn app.main:app --reload --port $port
