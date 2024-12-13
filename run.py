import subprocess


# save_dir = 'experiments_logs'
# exp_name = 'rwma'
# da_methods = ['NO_ADAPT', 'SYN', 'Deep_Coral', 'MMDA', 'DANN', 'CDAN', 'DIRT', 'DSAN', 'HoMM', 'CoDATS', 'AdvSKM', 'SASA', 'CoTMix', 'TARGET_ONLY']
# data_path = 'data'
# dataset = 'realworld_mobiact'
# backbone = 'CNN'
# num_runs = 1
# device = 'cuda'

da_methods = ['Deep_Coral', 'DANN']
datasets = ['realworld_mobiact', 'mobiact_realworld', 'realworld_pamap', 'pamap_realworld', 'mobiact_pamap', 'pamap_mobiact']
exp_names = ['rwma', 'marw', 'rwpa', 'parw', 'mapa', 'pama']


for da_method in da_methods:

    num_runs = 10 if da_method in ['NO_ADAPT', 'SYN'] else 1
    
    for i, dataset in enumerate(datasets):

        exp_name = 'ROT_' + exp_names[i]

        subprocess.run(['python', 'main.py',
                        '--phase', 'train',
                        '--save_dir', 'experiments_logs_wal',
                        '--exp_name', exp_name,
                        '--da_method', da_method,
                        '--data_path', 'data_temp',
                        '--dataset', dataset,
                        '--backbone', 'CNN',
                        '--num_runs', str(num_runs),
                        '--device', 'cuda'
                        ])
        

# Run uno così e poi uno senza rotazioni (add rot in exp_name and uncomment), poi syn (change comments in data_model_configs)

