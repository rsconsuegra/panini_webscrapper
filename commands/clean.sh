#!/bin/bash
echo "Deleting Pycache"
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
echo "The House is clean"
