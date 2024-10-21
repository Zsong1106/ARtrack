class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/root/siton-data-qiuyueData/zss/code/AIFIARTrack/'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/root/siton-data-qiuyueData/zss/code/AIFIARTrack//tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/root/siton-data-qiuyueData/zss/code/AIFIARTrack//pretrained_networks'
        self.got10k_dir = '/root/siton-data-qiuyueData/wrz/datasets/got-10k/train'
        self.got10k_val_dir = '/root/siton-data-qiuyueData/wrz/datasets/got-10k/val'
        self.save_every_epoch = True
       
