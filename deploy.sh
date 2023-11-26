#!/bin/bash -ex

# Check if npm is installed
if ! hash npm 2>/dev/null; then
    echo "Error: npm is not installed."
    exit 1
fi

# Check if zip is installed
if ! hash zip 2>/dev/null; then
    echo "Error: zip is not installed."
    exit 1
fi

# Remove 'dist' and 'node_modules' directories if they exist
echo "Cleaning up old 'dist' and 'node_modules' directories..."
rm -rf dist node_modules

# Run npm install
echo "Running npm install..."
npm ci

# Run npm build
echo "Running npm run build..."
npm run build

# Check if the build was successful and 'dist' directory exists
if [ ! -d "dist" ]; then
    echo "Error: 'dist' directory not found. Build may have failed."
    exit 1
fi

# Check if 'requirements.txt' exists
if [ ! -f "requirements.txt" ]; then
    echo "Error: 'requirements.txt' file not found."
    exit 1
fi

# Check if 'app.py' exists
if [ ! -f "app.py" ]; then
    echo "Error: 'app.py' file not found."
    exit 1
fi

# Create a zip file
zip -r demo.zip requirements.txt app.py dist

echo "Archive 'demo.zip' created successfully."
