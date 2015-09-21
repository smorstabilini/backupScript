#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Rename this file site_config.py and change it at your convenienve

from scaricaBackup import DAYS, MONTHS, SQL, TARGZ

backups = [
    {
        'customer': 'Custome 1',
        'remote_url': 'customer1.webfactional.com',
        'username': [insert-username-here],
        'password': [insert-password-here],
        'remote_path': '/home/aaaa/db_backups/project1',
        'files': [
            {
                'name': 'Dump db project 1',
                'filename_prefix': 'project1_',
                'destination_path': '/home/yourname/PROJECTS/backup/customer1_project1/',
                'number_of_files_to_retrieve': 5,
                'frequency': DAYS,
                'file_extension': SQL
            }
        ]
    },
    {
        'customer': 'Customer 2',
        'remote_url': 'customer2.webfactional.com',
        'username': '',
        'password': '',
        'remote_path': '/home/bbbb/db_backups/project 2',
        'files': [
            {
                'name': 'Dump db Wordpress',
                'filename_prefix': 'Project2_dump_',
                'destination_path': '/media/Volume/PROJECTS/backup/customer2_project2/',
                'number_of_files_to_retrieve': 1,
                'frequency': MONTHS,
                'file_extension': SQL
            },
            {
                'name': 'Files Wordpress',
                'filename_prefix': 'Project2_files_',
                'destination_path': '/media/Volume/PROJECTS/backup/customer2_project2/',
                'number_of_files_to_retrieve': 1,
                'frequency': MONTHS,
                'file_extension': TARGZ
            }
        ]
    },
]