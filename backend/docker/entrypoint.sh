#!/bin/sh
exec uvicorn api.main:app --host $HOST --port $PORT
