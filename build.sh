#!/usr/bin/env bash
# Build script for Render deployment

echo "Starting build process..."
echo "Current directory: $(pwd)"
echo "Listing files:"
ls -la

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build completed successfully!"
