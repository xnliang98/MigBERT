# MigBERT | 中文混合粒度BERT
This is the code for preprint paper [Character, Word, or Both? Revisiting the Segmentation Granularity for Chinese Pre-trained Language Models](https://arxiv.org/abs/2303.10893).

> TODO1: upload MigBERT-base, MigBERT-JP-base/large
> TODO2: upload all fine-tune scripts.
> TODO3: Finish the readme.md.

## Model Download
https://huggingface.co/xnliang/MigBERT-large



## Fine-tune on OCNLI
Install required python packages.

安装Python的依赖库。
```
pip install -r requirements.txt
```
你可以在单卡V100-32G上训练该模型。

You can train the model on one V100-32G.
```shell
bash run_ocnli.sh
```

ACC: ~82.00. 

## Citation
如果你觉得我们的工作对你有用，请在您的工作中引用我们的文章。
If you find our resource or paper is useful, please consider including the following citation in your paper.

```
@misc{liang2023character,
      title={Character, Word, or Both? Revisiting the Segmentation Granularity for Chinese Pre-trained Language Models}, 
      author={Xinnian Liang and Zefan Zhou and Hui Huang and Shuangzhi Wu and Tong Xiao and Muyun Yang and Zhoujun Li and Chao Bian},
      year={2023},
      eprint={2303.10893},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```