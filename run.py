import subprocess


save_dir = 'experiments_logs'
exp_name = 'rwma0311'
da_methods = ['NO_ADAPT', 'TARGET_ONLY', 'MMDA', 'DANN', 'CDAN', 'DIRT', 'DSAN', 'HoMM', 'CoDATS', 'AdvSKM', 'SASA', 'CoTMix']
data_path = 'data'
dataset = 'realworld_mobiact'
backbone = 'TSTR'
num_runs = 5
device = 'cuda'


for da_method in da_methods:

    subprocess.run(['python', 'main.py',
                    '--phase', 'train',
                    '--save_dir', save_dir,
                    '--exp_name', exp_name,
                    '--da_method', da_method,
                    '--data_path', data_path,
                    '--dataset', dataset,
                    '--backbone', backbone,
                    '--num_runs', str(num_runs),
                    '--device', device
                    ])

