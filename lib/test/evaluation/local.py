from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
   
    settings.got10k_path = '/root/siton-data-qiuyueData/wrz/datasets/got-10k'
    settings.lasot_extension_subset_path = '/home/baiyifan/LaSOText/LaSOT_extension_subset'
    settings.lasot_lmdb_path = '/home/baiyifan/code/OSTrack/data/lasot_lmdb'
    settings.lasot_path = '/root/siton-data-qiuyueData/wrz/datasets/Lasot/LaSOTTest'
    settings.network_path =  '/ssddata/baiyifan/artrack_256_full_re/'   # Where tracking networks are stored.
    settings.prj_dir = '/root/siton-data-qiuyueData/zss/code/AIFIARTrack/'
    settings.result_plot_path = '/root/siton-data-qiuyueData/zss/code/AIFIARTrack/output/checkpoints/'
    settings.results_path = '/root/siton-data-qiuyueData/zss/code/AIFIARTrack/output/checkpoints/'    # Where to store tracking results
    settings.save_dir =  '/root/siton-data-qiuyueData/zss/code/AIFIARTrack/output/'


    return settings

