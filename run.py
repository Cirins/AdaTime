import subprocess


save_dir = 'experiments_logs'
# exp_name = 'rwma'
# da_methods = ['NO_ADAPT', 'SYN', 'Deep_Coral', 'MMDA', 'DANN', 'CDAN', 'DIRT', 'DSAN', 'HoMM', 'CoDATS', 'AdvSKM', 'SASA', 'CoTMix', 'TARGET_ONLY']
da_methods = ['SYN']
data_path = 'data'
# dataset = 'realworld_mobiact'
backbone = 'CNN'
# num_runs = 1
device = 'cuda'


for da_method in da_methods:

    num_runs = 10 if da_method == 'NO_ADAPT' or da_method == 'SYN' else 1

    subprocess.run(['python', 'main.py',
                    '--phase', 'train',
                    '--save_dir', save_dir,
                    '--exp_name', 'mapa',
                    '--da_method', da_method,
                    '--data_path', data_path,
                    '--dataset', 'mobiact_pamap',
                    '--backbone', backbone,
                    '--num_runs', str(num_runs),
                    '--device', device
                    ])

    subprocess.run(['python', 'main.py',
                    '--phase', 'train',
                    '--save_dir', save_dir,
                    '--exp_name', 'pama',
                    '--da_method', da_method,
                    '--data_path', data_path,
                    '--dataset', 'pamap_mobiact',
                    '--backbone', backbone,
                    '--num_runs', str(num_runs),
                    '--device', device
                    ])

