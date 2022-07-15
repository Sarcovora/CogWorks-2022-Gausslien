# CogWorks 2022 Gausslien Audio Capstone

## Instructions
1. Install CogZam: cd to the base repo directory and do
```shell
pip install -e .
```
2. Put all the songs you want in the database in the songs folder
3. Run updateDatabaseWithOriginals.py
4. Run song_query.py

## CogZam Function Order
### Adding to a database (updateDatabaseWithOriginals.py)
1. userinput (recordingtoarray.py)
2. peak_extract (peakExtraction.py)
3. getFingerprints (getFingerprints.py)
4. store_fingerprint (store_fingerprints.py)
5. store_song (database_interface.py)

### Searching for a song (song_query.py)
1. load_fp_database (database_interface.py)
2. load_song_database (database_interface.py)
3. (For upload) long_to_short (long_to_short.py)
3. (For record) micRecord (recordingtoarray.py)
4. peak_extract (peakExtraction.py)
5. getFingerprints (getFingerprints.py)
6. query_database (query_database.py)
7. tally_results (tally_results.py)


