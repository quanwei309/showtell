#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


from flags import parse_args


if __name__ == '__main__':
    FLAGS, unparsed = parse_args()
    print('current working dir [{0}]'.format(os.getcwd()))
    w_d = os.path.dirname(os.path.abspath(__file__))
    print('change wording dir to [{0}]'.format(w_d))
    os.chdir(w_d)

    cmd = ""

    #train \
    #--input_train_file_pattern="${MSCOCO_DIR}/train-?????-of-00256" \
    #--inception_checkpoint_file="${INCEPTION_CHECKPOINT}" \
    #--train_dir="${MODEL_DIR}/train" \
    #--train_inception=false \
    #--number_of_steps=1000000

    #/ evaluate \
    # --input_val_file_pattern = "${MSCOCO_DIR}/val-?????-of-00004" \
    # --checkpoint_dir = "${MODEL_DIR}/train" \
    # --eval_dir = "${MODEL_DIR}/eval"

    #run_inference \
    #--checkpoint_path =${CHECKPOINT_PATH} \
    #--vocab_file =${VOCAB_FILE} \
    #--input_files =${IMAGE_FILE}
    print('################    configuration    ################')
    p = os.popen('python ./configuration.py')
    for l in p:
        print(l.strip())

    for parm in ["input_train_file_pattern", "inception_checkpoint_file", "train_dir", "train_inception",
                 "input_val_file_pattern" , "checkpoint_dir", "eval_dir",
                 "checkpoint_path", "vocab_file", "input_files"]:
        try:
            cmd += ' --{0}={1}'.format(parm, getattr(FLAGS, parm))
        except:
            pass
    #batch_size =32    40000step 大概一个epoch
    number_of_steps = getattr(FLAGS, "number_of_steps")
    for i in range(10):
       # train 1 epoch
        print('################    train    ################')
        number_of_steps = (i+1)*number_of_steps
        cmd +=' --{0}={1}'.format("number_of_steps", number_of_steps)
        print('################    cmd :   ', cmd)
        p = os.popen('python ./train.py' + cmd)
        for l in p:
            print(l.strip())

        # eval
        print('################    eval    ################')
        print('################    cmd :   ', cmd)
        p = os.popen('python ./evaluate.py' + cmd)
        for l in p:
            print(l.strip())

        print('################    inference    ################')
        print('################    cmd :   ', cmd)
        p = os.popen('python ./run_inference.py' + cmd)
        for l in p:
            print(l.strip())
