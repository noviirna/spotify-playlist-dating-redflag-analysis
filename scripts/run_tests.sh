#!/bin/bash

# Script to run tests for the Spotify Playlist Analysis project

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_status "Running tests for Spotify Playlist Analysis..."

# Check if we're in the right directory
if [ ! -f "requirements.txt" ]; then
    print_error "Please run this script from the project root directory"
    exit 1
fi

# Install test dependencies if needed
if ! python -c "import pytest" 2>/dev/null; then
    print_status "Installing test dependencies..."
    pip install pytest pytest-cov
fi

# Run tests
print_status "Running unit tests..."
python -m pytest tests/ -v --cov=noviirnawati --cov-report=html --cov-report=term

# Run the test runner script
print_status "Running test runner script..."
python tests/run_tests.py

print_status "All tests completed!"
