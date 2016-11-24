#!/usr/bin/env bash

rm -f submission.zip
cp HAL.py MyBot.py
zip -rX submission.zip MyBot.py hal
