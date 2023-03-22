TASK_NAME=ocnli_public
DATA_DIR=data/${TASK_NAME}

mkdir -p logs/${TASK_NAME}

python3 src/run_cls.py \
    --model_name_or_path xnliang/MigBERT-large \
    --task_name $TASK_NAME \
    --train_file $DATA_DIR/train.json \
    --validation_file $DATA_DIR/dev.json \
    --test_file $DATA_DIR/test.json \
    --cache_dir cached_file/ \
    --do_train \
    --do_eval \
    --do_predict \
    --lr_scheduler_type "linear" \
    --logging_strategy "steps" \
    --evaluation_strategy "steps" \
    --save_strategy "steps" \
    --save_steps 10000 \
    --logging_steps 100 \
    --eval_steps 100 \
    --max_seq_length 150 \
    --warmup_steps 100 \
    --max_steps -1 \
    --per_device_train_batch_size 64 \
    --per_device_eval_batch_size 64 \
    --learning_rate 2e-5 \
    --num_train_epochs 3 \
    --overwrite_output_dir \
    --output_dir tmp/$TASK_NAME/ --seed 42 