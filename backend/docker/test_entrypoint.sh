#!/bin/sh
exec python -m pytest tests/ --cov=api/ --cov-fail-under=75
