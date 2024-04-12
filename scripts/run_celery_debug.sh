#!/bin/bash

watchmedo auto-restart -d src/worker -p '*.py' --  celery -A src.worker worker --concurrency=4 -l info