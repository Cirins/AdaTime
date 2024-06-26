import subprocess

# Define lists of parameters
datasets = ["CWRU_IR", "CWRU_Ball", "CWRU_OR_centred", "CWRU_OR_orthogonal", "CWRU_OR_opposite"]
da_methods = ["NO_ADAPT"]

# Base command to run the script, adjust the python filename as needed
base_command = "python main.py"

# Loop through each combination of parameters
for dataset in datasets:
    for da_method in da_methods:
            exp_name = f"{dataset}_SYN"
            # Construct the command with all parameters
            command = f"{base_command} --phase=train --exp_name={exp_name} --da_method={da_method} --dataset={dataset}"
            # Print command (for testing purposes) or execute it
            print(command)
            # Uncomment the line below to actually execute the command
            subprocess.run(command, shell=True)

