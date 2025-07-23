How It Works
Phase 1: Local File Processing

Parses TuxGuitar files (.gp3/.gp4/.gp5) for guitar tablature
Processes MIDI files to extract musical notes and timing
Reads ASCII tab files and chord charts
Converts everything into structured JSON chunks

Phase 2: Web Scraping

Scrapes educational music websites (Wikipedia, music theory sites, etc.)
Attempts to get Ultimate Guitar tabs (currently failing due to 404s)
Processes GitHub awesome-guitar resources
Extracts and chunks text content for AI training

Data Storage

Saves all content as JSON files
Stores in ChromaDB vector database for semantic search
Creates searchable chunks with metadata (source, difficulty, topic, etc.)

Current Issues That Need Fixing
1. TuxGuitar Library Issue
python# PROBLEM: guitarpro.open() doesn't exist
song = guitarpro.open(filepath)

# FIX: Install correct library or use different method
pip install guitar-pro  # or try: pip install PyGuitarPro
2. Missing XML Parser
bash# PROBLEM: "Couldn't find a tree builder with the features you requested: xml"
# FIX: Install lxml
pip install lxml
3. Ultimate Guitar URLs Are Dead
The hardcoded Ultimate Guitar URLs return 404 errors. Need fresh, valid URLs or different approach.
4. Duplicate ID Errors in ChromaDB
The script generates duplicate chunk IDs, causing database errors.
5. Website Access Issues
Some sites block the scraper (403 Forbidden) or have connection timeouts.
How Someone Else Can Run This
Prerequisites Installation
bash# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install required packages
pip install requests beautifulsoup4 tiktoken chromadb pandas
pip install music21 guitarpro pretty-midi pdfplumber playwright
pip install lxml  # For XML parsing
File Structure Setup
project_directory/
├── web_scraper.py
├── samples/              # CREATE THIS DIRECTORY
│   ├── sample.gp3       # Add your .gp files here
│   ├── sample.mid       # Add MIDI files here  
│   ├── tab1.txt         # Add ASCII tab files here
│   └── sample_chords.txt # Add chord charts here
└── music_rag_data/      # Will be created automatically
Configuration Changes Needed
1. Update File Paths (Line ~1050)
python# CHANGE THESE PATHS TO YOUR ACTUAL FILES
tuxguitar_files = [
    "samples/your_actual_file.gp3",  # Replace with real files
    "samples/another_song.gp5",
]

freetar_tabs = [
    "samples/your_tab_file.txt",     # Replace with real tab files
]

guitar_trainer_midi_files = [
    "samples/your_midi_file.mid",    # Replace with real MIDI files
]
2. Fix Ultimate Guitar URLs (Line ~885)
python# REPLACE THESE DEAD URLS WITH WORKING ONES
sample_ug_urls = [
    # Find working Ultimate Guitar URLs or comment out this section
    # "https://tabs.ultimate-guitar.com/tab/artist/song-chords-xxxxx",
]
3. Optional: Add HookTheory Token
python# Set environment variable for HookTheory API access
import os
os.environ['HOOKTHEORY_TOKEN'] = 'your_token_here'  # Optional
Running the Script
bash# Navigate to project directory
cd your_project_directory

# Run the scraper
python web_scraper.py
Expected Output

Phase 1: Processes local files (MIDI worked: 620 chunks)
Phase 2: Scrapes websites (786 chunks collected)
Creates JSON files in music_rag_data/ folder
Builds ChromaDB database for semantic search
Total: ~1400+ chunks of music education content

Quick Start for Testing

Create samples/ directory
Add at least one MIDI file to test
Comment out TuxGuitar section if you don't have .gp files
Run with minimal file set to verify it works
Gradually add more file types and sources

The script is functional but needs the above fixes for optimal performance. The ChromaDB integration works well for creating a searchable music education database.
