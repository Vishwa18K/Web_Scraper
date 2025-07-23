This Music RAG Data Scraper collects guitar tabs, music theory content, and educational materials for AI training. It processes both local files and web content, then stores everything in a searchable ChromaDB vector database.
# How It Works
Phase 1: Local File Processing

Parses TuxGuitar files (.gp3/.gp4/.gp5) for guitar tablature
Processes MIDI files to extract musical notes and timing
Reads ASCII tab files and chord charts
Converts everything into structured JSON chunks

Phase 2: Web Scraping

Scrapes educational music websites (Wikipedia, music theory sites, etc.)
Attempts to get Ultimate Guitar tabs
Processes GitHub awesome-guitar resources
Extracts and chunks text content for AI training

Data Storage

Saves all content as JSON files
Stores in ChromaDB vector database for semantic search
Creates searchable chunks with metadata (source, difficulty, topic, etc.)

# Installation (prereqs, and file structure, and changing file paths)
<img width="418" height="332" alt="image" src="https://github.com/user-attachments/assets/ff38cc75-63dd-433a-8a53-08e8d592ebb4" />

<img width="412" height="271" alt="image" src="https://github.com/user-attachments/assets/d02e38d8-be7d-4d2c-aa86-4537b01b94f0" />

# known problems 
1. TuxGuitar Library Issue
Problem: module 'guitarpro' has no attribute 'open'
Fix: Install the correct library:
bashpip install guitar-pro  # or try: pip install PyGuitarPro

2. Missing XML Parser
Problem: Couldn't find a tree builder with the features you requested: xml
Fix: Install lxml:
bashpip install lxml

3. Ultimate Guitar URLs Are Dead
The hardcoded Ultimate Guitar URLs return 404 errors. You'll need to find fresh, valid URLs or comment out that section.
4. Duplicate ID Errors in ChromaDB
The script may generate duplicate chunk IDs, causing database errors. This is handled gracefully but may reduce total chunks stored.
5. Website Access Issues
Some sites block the scraper (403 Forbidden) or have connection timeouts. This is expected behavior for some protected sites.


# Output Files
The scraper creates several JSON files in the music_rag_data/ directory:

phase1_local_file_chunks.json - Local file processing results
educational_websites.json - Web scraped educational content
ultimate_guitar_tabs.json - Guitar tabs (if successful)
awesome_guitar_resources.json - GitHub resources
complete_music_dataset.json - Combined dataset
chroma_db/ - ChromaDB vector database




