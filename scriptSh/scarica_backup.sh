# Questo è il file sh che va messo nella cartella ~/bin del proprio pc
# La versione in uso non ha questi commenti in cima...

echo "Script in ~/bin che richiama lo script python che effettivamente scarica i db"


source /home/mosta/VirtualEnv/backupManager/bin/activate

cd /home/mosta/work/backupManager
`/home/mosta/work/backupManager/scaricaBackup.py`



