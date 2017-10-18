#!/bin/bash

grep -P '(\d)\s?\1' /dev/stdin
