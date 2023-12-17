#!/usr/bin/env bash
port="8000"
kill $(lsof -t -i:$port)
