import subprocess


save_dir = 'experiments_logs'
# exp_name = 'rwma'
# da_methods = ['NO_ADAPT', 'Deep_Coral', 'MMDA', 'DANN', 'CDAN', 'DIRT', 'DSAN', 'HoMM', 'CoDATS', 'AdvSKM', 'SASA', 'CoTMix', 'TARGET_ONLY']
da_methods = ['Deep_Coral', 'DANN']
data_path = 'data'
# dataset = 'realworld_mobiact'
backbone = 'CNN'
num_runs = 1
device = 'cuda'


for da_method in da_methods:

    # subprocess.run(['python', 'main.py',
    #                 '--phase', 'train',
    #                 '--save_dir', save_dir,
    #                 '--exp_name', 'rwma',
    #                 '--da_method', da_method,
    #                 '--data_path', data_path,
    #                 '--dataset', 'realworld_mobiact',
    #                 '--backbone', backbone,
    #                 '--num_runs', str(num_runs),
    #                 '--device', device
    #                 ])

    subprocess.run(['python', 'main.py',
                    '--phase', 'train',
                    '--save_dir', save_dir,
                    '--exp_name', 'marw',
                    '--da_method', da_method,
                    '--data_path', data_path,
                    '--dataset', 'mobiact_realworld',
                    '--backbone', backbone,
                    '--num_runs', str(num_runs),
                    '--device', device
                    ])

