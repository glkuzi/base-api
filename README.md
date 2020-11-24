# base-api
Base api on flask-restful. Could be used to send some files through api in json (e. g. csv files).

## Structure
1. app.py - main app, realize main api functional - get one of two csv files from folder and send it.
2. config.py - config file, contains pathes to files and some api information (api-key). Before using this app, one have to change api-key in config file for security purposes.
3. test_requests.py - simple script to test your api - get file from api and show it. Could be used for debug. For debug one should set api URL (with port), key and endpoint in conifg file. In current version, file configured for testing on localhost with 5045 port.
4. run.sh - bash script for running this api on server.

## How to (use, run, modify)
To run api, just run this command:
```
./run.sh 
```
To run api in background, run this command:
```
nohup ./run.sh &
```
This command move all output to nohup.out file and run app in background, and also print pid of runned process.
To stop app, just kill app process.
