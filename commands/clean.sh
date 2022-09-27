echo "Delete Pycache"
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
echo "House Cleaned"