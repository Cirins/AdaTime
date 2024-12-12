def get_dataset_class(dataset_name):
    """Return the algorithm class with the given name."""
    if dataset_name not in globals():
        raise NotImplementedError("Dataset not found: {}".format(dataset_name))
    return globals()[dataset_name]



class realworld_mobiact():
    def __init__(self):
        super(realworld_mobiact, self).__init__()
        # self.scenarios = [(f'syn_{dom}', f'dp_{dom}') for dom in range(15, 76)]
        # self.scenarios = [(f'df', f'dp_{dom}') for dom in range(15, 76)]
        # self.scenarios = [(f'syn_wal_{dom}', f'dp_wal_{dom}') for dom in range(15, 76)]
        self.scenarios = [(f'df', f'dp_wal_{dom}') for dom in range(15, 76)]
        self.class_names = ['WAL', 'RUN', 'CLD', 'CLU']
        self.sequence_len = 128
        self.shuffle = True
        self.drop_last = True
        self.normalize = False

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = len(self.class_names)

        # CNN and RESNET features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.hidden_dim = 500
        self.DSKN_disc_hid = 128



class mobiact_realworld():
    def __init__(self):
        super(mobiact_realworld, self).__init__()
        # self.scenarios = [(f'syn_{dom}', f'dp_{dom}') for dom in range(61, 76)]
        # self.scenarios = [(f'df', f'dp_{dom}') for dom in range(61, 76)]
        # self.scenarios = [(f'syn_wal_{dom}', f'dp_wal_{dom}') for dom in range(61, 76)]
        self.scenarios = [(f'df', f'dp_wal_{dom}') for dom in range(61, 76)]
        self.class_names = ['WAL', 'RUN', 'CLD', 'CLU']
        self.sequence_len = 128
        self.shuffle = True
        self.drop_last = True
        self.normalize = False

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = len(self.class_names)

        # CNN and RESNET features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.hidden_dim = 500
        self.DSKN_disc_hid = 128



class realworld_pamap():
    def __init__(self):
        super(realworld_pamap, self).__init__()
        # self.scenarios = [(f'syn_{dom}', f'dp_{dom}') for dom in range(15, 21)]
        # self.scenarios = [(f'df', f'dp_{dom}') for dom in range(15, 21)]
        # self.scenarios = [(f'syn_wal_{dom}', f'dp_wal_{dom}') for dom in range(15, 21)]
        self.scenarios = [(f'df', f'dp_wal_{dom}') for dom in range(15, 21)]
        self.class_names = ['WAL', 'RUN', 'CLD', 'CLU']
        self.sequence_len = 128
        self.shuffle = True
        self.drop_last = True
        self.normalize = False

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = len(self.class_names)

        # CNN and RESNET features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.hidden_dim = 500
        self.DSKN_disc_hid = 128



class pamap_realworld():
    def __init__(self):
        super(pamap_realworld, self).__init__()
        # self.scenarios = [(f'syn_{dom}', f'dp_{dom}') for dom in range(6, 21)]
        # self.scenarios = [(f'df', f'dp_{dom}') for dom in range(6, 21)]
        # self.scenarios = [(f'syn_wal_{dom}', f'dp_wal_{dom}') for dom in range(6, 21)]
        self.scenarios = [(f'df', f'dp_wal_{dom}') for dom in range(6, 21)]
        self.class_names = ['WAL', 'RUN', 'CLD', 'CLU']
        self.sequence_len = 128
        self.shuffle = True
        self.drop_last = True
        self.normalize = False

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = len(self.class_names)

        # CNN and RESNET features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.hidden_dim = 500
        self.DSKN_disc_hid = 128



class mobiact_pamap():
    def __init__(self):
        super(mobiact_pamap, self).__init__()
        # self.scenarios = [(f'syn_{dom}', f'dp_{dom}') for dom in range(61, 67)]
        # self.scenarios = [(f'df', f'dp_{dom}') for dom in range(61, 67)]
        # self.scenarios = [(f'syn_wal_{dom}', f'dp_wal_{dom}') for dom in range(61, 67)]
        self.scenarios = [(f'df', f'dp_wal_{dom}') for dom in range(61, 67)]
        self.class_names = ['WAL', 'RUN', 'CLD', 'CLU']
        self.sequence_len = 128
        self.shuffle = True
        self.drop_last = True
        self.normalize = False

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = len(self.class_names)

        # CNN and RESNET features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.hidden_dim = 500
        self.DSKN_disc_hid = 128



class pamap_mobiact():
    def __init__(self):
        super(pamap_mobiact, self).__init__()
        # self.scenarios = [(f'syn_{dom}', f'dp_{dom}') for dom in range(6, 67)]
        # self.scenarios = [(f'df', f'dp_{dom}') for dom in range(6, 67)]
        # self.scenarios = [(f'syn_wal_{dom}', f'dp_wal_{dom}') for dom in range(6, 67)]
        self.scenarios = [(f'df', f'dp_wal_{dom}') for dom in range(6, 67)]
        self.class_names = ['WAL', 'RUN', 'CLD', 'CLU']
        self.sequence_len = 128
        self.shuffle = True
        self.drop_last = True
        self.normalize = False

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = len(self.class_names)

        # CNN and RESNET features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.hidden_dim = 500
        self.DSKN_disc_hid = 128



class HAR():
    def __init__(self):
        super(HAR, self).__init__()
        self.scenarios = [("2", "11"), ("6", "23"), ("7", "13"), ("9", "18"), ("12", "16"), ("18", "27"), ("20", "5"), ("24", "8"), ("28", "27"), ("30", "20")]
        self.class_names = ['walk', 'upstairs', 'downstairs', 'sit', 'stand', 'lie']
        self.sequence_len = 128
        self.shuffle = True
        self.drop_last = True
        self.normalize = True

        # model configs
        self.input_channels = 9
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = 6

        # CNN and RESNET features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.hidden_dim = 500
        self.DSKN_disc_hid = 128
        
        
class EEG():
    def __init__(self):
        super(EEG, self).__init__()
        # data parameters
        self.num_classes = 5
        self.class_names = ['W', 'N1', 'N2', 'N3', 'REM']
        self.sequence_len = 3000
        self.scenarios = [("0", "11"), ("7", "18"), ("9", "14"), ("12", "5"), ("16", "1"),
                          ("3", "19"), ("18", "12"), ("13", "17"), ("5", "15"), ("6", "2")]
        self.shuffle = True
        self.drop_last = True
        self.normalize = True

        # model configs
        self.input_channels = 1
        self.kernel_size = 25
        self.stride = 6
        self.dropout = 0.2

        # features
        self.mid_channels = 32
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [32,64]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 15# 25
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.DSKN_disc_hid = 128
        self.hidden_dim = 500
        self.disc_hid_dim = 100


class WISDM(object):
    def __init__(self):
        super(WISDM, self).__init__()
        self.class_names = ['walk', 'jog', 'sit', 'stand', 'upstairs', 'downstairs']
        self.sequence_len = 128
        self.scenarios = [("7", "18"), ("20", "30"), ("35", "31"), ("17", "23"), ("6", "19"),
                          ("2", "11"), ("33", "12"), ("5", "26"), ("28", "4"), ("23", "32")]
        self.num_classes = 6
        self.shuffle = True
        self.drop_last = False
        self.normalize = True

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5
        self.num_classes = 6

        # features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75,150,300]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.DSKN_disc_hid = 128
        self.hidden_dim = 500


class HHAR(object):  ## HHAR dataset, SAMSUNG device.
    def __init__(self):
        super(HHAR, self).__init__()
        self.sequence_len = 128
        self.scenarios = [("0", "6"), ("1", "6"), ("2", "7"), ("3", "8"), ("4", "5"),
                          ("5", "0"), ("6", "1"), ("7", "4"), ("8", "3"), ("0", "2")]
        self.class_names = ['bike', 'sit', 'stand', 'walk', 'stairs_up', 'stairs_down']
        self.num_classes = 6
        self.shuffle = True
        self.drop_last = True
        self.normalize = True

        # model configs
        self.input_channels = 3
        self.kernel_size = 5
        self.stride = 1
        self.dropout = 0.5

        # features
        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75,150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.DSKN_disc_hid = 128
        self.hidden_dim = 500

        
        
class FD(object):
    def __init__(self):
        super(FD, self).__init__()
        self.sequence_len = 5120
        self.scenarios = [("0", "1"), ("0", "3"), ("1", "0"), ("1", "2"),("1", "3"),
                          ("2", "1"),("2", "3"),  ("3", "0"), ("3", "1"), ("3", "2")]
        self.class_names = ['Healthy', 'D1', 'D2']
        self.num_classes = 3
        self.shuffle = True
        self.drop_last = True
        self.normalize = True

        # Model configs
        self.input_channels = 1
        self.kernel_size = 32
        self.stride = 6
        self.dropout = 0.5

        self.mid_channels = 64
        self.final_out_channels = 128
        self.features_len = 1

        # TCN features
        self.tcn_layers = [75, 150]
        self.tcn_final_out_channles = self.tcn_layers[-1]
        self.tcn_kernel_size = 17
        self.tcn_dropout = 0.0

        # lstm features
        self.lstm_hid = 128
        self.lstm_n_layers = 1
        self.lstm_bid = False

        # discriminator
        self.disc_hid_dim = 64
        self.DSKN_disc_hid = 128
        self.hidden_dim = 500
