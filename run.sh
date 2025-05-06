#!/bin/bash  

project_dir="/home/keller/Documents/Jobdev/G2A/test2" 
robot_file="$project_dir/Tests/test.robot"  
log_file="$project_dir/logfile.log"

# Vérifier si le fichier Python existe  
if [[ -f "$robot_file" ]]; then  
    echo "Lancement de $robot_file..."
    source "$project_dir/venv/bin/activate"
    echo "$(date '+%Y-%m-%d %H:%M:%S') : process start" | tee -a "$log_file"  
    robot "$robot_file" >> "$log_file" 2>&1 
    deactivate
    echo "$(date '+%Y-%m-%d %H:%M:%S') : process finished." | tee -a "$log_file" 
else  
    echo "Erreur : $robot_file n'existe pas."  
fi  

# */3 * * * * DISPLAY=:0 /home/keller/Documents/Jobdev/G2A/SOC/setup.sh