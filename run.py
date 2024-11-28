import subprocess


save_dir = 'experiments_logs'
exp_name = 'rwma0311'
da_method = 'NO_ADAPT'
data_path = 'data'
dataset = 'realworld_mobiact'
backbone = 'TSTR'
num_runs = 1
device = 'cpu'



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


# subprocess.run(['python', 'main.py',
#                 '--phase', 'test',
#                 '--save_dir', save_dir,
#                 '--exp_name', exp_name,
#                 '--da_method', da_method,
#                 '--data_path', data_path,
#                 '--dataset', dataset,
#                 '--backbone', backbone,
#                 '--num_runs', str(num_runs),
#                 '--device', device
#                 ])

