start-ts:
	cd node-app && npx tsx watch src/index.ts

start-py:
	cd python-app && pymon src/main.py

start:
	make start-ts &
	make start-py
