#!/bin/bash

####### Questo è il file .sh che sta nella cartella ~/bin sul server
####### della società ViDissetiamo. Serve a scaricare in automatico i 
####### file del gestionale dal repository git e a lanciare il comando
####### "manage.py collectstatic"

####### Per richiamare il file usare:
####### . set_gestionale




### eval `ssh-agent -s`
### ssh-add /home/mosta/.ssh/id_rsa_da_wf_a_bitbucket

cd ~/webapps/vdgestionale/vdgestionale
git pull

source /home/vidissetiamo/.virtualenvs/VdGestionale/bin/activate

python3.4 manage.py collectstatic --noinput
