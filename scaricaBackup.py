#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Installazione:
# - creazione virtualenv chiamato backupManager
# - pip install paramiko
# - pip install python-dateutil  (per usare relativedelta)
# - copiato scp.py da https://github.com/jbardin/scp.py

## http://stackoverflow.com/questions/250283/how-to-scp-in-python

# visto che chiamo lo script da un file .sh, le istruzioni di tipo
# print ("str") danno un errore perché lo script cerca di eserguire
# la stringa "str"
# Quindi al suo posto va usato  sys.stderr.write("str\n") che funziona
# sia quando si chiama direttamente il file .py che quando lo si chiama
# da un file .sh

from datetime import date, timedelta
# per i mesi timedelta non funziona, bisogna usare relativedelta:
from dateutil.relativedelta import relativedelta
from paramiko import SSHClient
from scp import SCPClient, SCPException
import os.path
import sys

from site_config import * 

DAYS = 1
MONTHS = 2

SQL = "sql"
TARGZ = "tar.gz"

def createSSHClient(server, port, user, password):
    client = SSHClient()
    client.load_system_host_keys()
    #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

class GestoreSito:
    def __init__(self, indirizzo, user, password, cartella_origine):
        self.indirizzo = indirizzo
        self.user = user
        self.password = password
        self.cartella_origine = cartella_origine
        self.client_gia_creato = False

    def scarica_backup(self, numero_ripetizioni, frequenza, estensione_file, radice_file, cartella_destinazione):
        
        today = date.today()

        for i in range(0, numero_ripetizioni):
            if frequenza == DAYS:
                giorno = today - timedelta(days=i)
            elif frequenza == MONTHS:
                primo_giorno_del_mese = today.replace(day=1)
                giorno = primo_giorno_del_mese + relativedelta(months=-i)

            data = giorno.strftime('%Y-%m-%d')
            nome_file = "{}{}.{}".format(radice_file, data, estensione_file)            
            sys.stderr.write("-- Verifico se in locale esiste già il file {}{}\n".format(cartella_destinazione, nome_file))
            if os.path.isfile("{}{}".format(cartella_destinazione, nome_file)):
                sys.stderr.write("File esiste già, non lo scarico di nuovo.\n")
            else:
                if not self.client_gia_creato:
                    self.ssh = createSSHClient(self.indirizzo, 22,
                        self.user, self.password)
                    self.scp = SCPClient(self.ssh.get_transport())            
                    self.client_gia_creato = True
                fileRemoto = "{}/{}".format(self.cartella_origine, nome_file)
                sys.stderr.write("Scarico il file {}\n".format(fileRemoto))
                try:
                    self.scp.get(fileRemoto, cartella_destinazione)
                except SCPException:
                    sys.stderr.write("---- Errore durante il download! il file esiste sul server?\n")
            sys.stderr.write("\n\n")


if __name__ == "__main__":
    sys.stderr.write("\n")

    for site in backups:

        gs = GestoreSito(
            site['remote_url'], site['username'], site['password'],
            site['remote_path'])

        for my_file in site['files']:
            sys.stderr.write("####### {} - {}\n\n".format(site['customer'], my_file['name']))
            gs.scarica_backup(my_file['number_of_files_to_retrieve'], 
                my_file['frequency'], my_file['file_extension'], 
                my_file['filename_prefix'], 
                my_file['destination_path'])
