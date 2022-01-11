

class CONFIG:
    def __init__(self):
        self.log_path = "log.txt"
        self.tokenizer_path = "mt5-small"
        self.model_config_path = "config/model_config.json"
        self.device = "gpu"
        self.saved_model_path = "output_mask_r_drop_split_reweight"
        self.pretrained_model_path = "mt5-small"
        self.test = True
        self.train = True
        self.num_workers = 0
        self.train_data_path = 'dataset/mask_train_all_split_dataset.json'
        self.dev_data_path = 'dataset/mask_dev_split_dataset_not_prompt.json'
        self.test_data_path = 'dataset/mask_test_500_split_dataset.json'
        self.test_size = 0.1
        self.batch_size= 2
        self.epochs = 10
        self.epoch2 = "output_mask_r_drop_split_reweight/model_epoch5/Prompt_IsA_Model.pth"
        self.save_model_dic="output_mask_r_drop_split_reweight/model_epoch5/Prompt_IsA_Model.pth"
        self.lr=1.5e-4
        self.warmup_steps=2000
        self.log_step=1
        self.max_grad_norm=1.0
        self.gradient_accumulation=1
        self.topk=8
        self.test_max_len=20
        self.save_mode=True
        self.n_desc=128
        self.n_labels=16
        self.num_classification=19
        self.together=False
        self.result_text = "result_SPL_reweight.txt"

