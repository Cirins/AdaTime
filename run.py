import subprocess


save_dir = 'experiments_logs'
exp_name = 'rwma11'
da_method = 'ROT'
data_path = 'data'
dataset = 'realworld_mobiact'
backbone = 'TSTR'
num_runs = 100
device = 'cuda'



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


subprocess.run(['python', 'main.py',
                '--phase', 'test',
                '--save_dir', save_dir,
                '--exp_name', exp_name,
                '--da_method', da_method,
                '--data_path', data_path,
                '--dataset', dataset,
                '--backbone', backbone,
                '--num_runs', str(num_runs),
                '--device', device
                ])

