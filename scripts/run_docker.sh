#!/bin/bash

# Script to run the Spotify Playlist Analysis using Docker

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

# Check if .env file exists
if [ ! -f ".env" ]; then
    print_error ".env file not found!"
    print_warning "Please copy env.example to .env and fill in your credentials:"
    echo "cp env.example .env"
    echo "nano .env"
    exit 1
fi

# Check if PLAYLIST_URL is provided
if [ -z "$1" ]; then
    print_error "Please provide a Spotify playlist URL as an argument"
    echo "Usage: $0 <spotify_playlist_url>"
    echo "Example: $0 https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq"
    exit 1
fi

PLAYLIST_URL="$1"

# Validate URL format
if [[ ! "$PLAYLIST_URL" =~ ^https://open\.spotify\.com/playlist/ ]]; then
    print_error "Invalid Spotify playlist URL format"
    print_warning "URL should be in format: https://open.spotify.com/playlist/<playlist_id>"
    exit 1
fi

print_status "Starting Spotify Playlist Analysis..."
print_status "Playlist URL: $PLAYLIST_URL"

# Create output directory if it doesn't exist
mkdir -p output

# Set environment variable for docker-compose
export PLAYLIST_URL="$PLAYLIST_URL"

# Run the analysis
print_status "Building and running Docker container..."
docker-compose run --rm spotify-analysis

print_status "Analysis complete! Check the output/ directory for results."
