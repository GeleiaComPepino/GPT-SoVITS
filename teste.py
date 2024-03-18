import fairseq
ckpt_path = "D:/Downloads/GPTSoVits/GPT-SoVITS/GPT_SoVITS/pretrained_models/hubert_large_ll60k.pt"
models, cfg, task = fairseq.checkpoint_utils.load_model_ensemble_and_task([ckpt_path])