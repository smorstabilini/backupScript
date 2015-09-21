# backupScript
Python scripts created to easily download files from remote servers.
It's possible to configure remote urls, username, password, frequency of download, etc.
This script is meant to be run daily. It checks if desired backups have already been downloaded 
and if not it downloads them.

Remote files are created with cronjobs.

Based on scp.py (https://github.com/jbardin/scp.py).

Installation
-----
Following packages are required:
- paramiko
- python-dateutil

Usage of VirtualEnv is highly recommended.

Configuration
-------------
Rename site_config_example.py into site_config.py and change it as per your requirements.
Remember to create remote and local directories accordingly.

Usage
-----
  python scaricaBackup.py

