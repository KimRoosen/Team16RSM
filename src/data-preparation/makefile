# Makefile
# requires GNUMake32
# Installation instructions: http://tilburgsciencehub.com/setup

../../data/team16_reactions_quarantaine_policy_nl.zip: download.py
	python download.py
	python unzip.py
	python parse.py

wipe:
	python wipe.py
