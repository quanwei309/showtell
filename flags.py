#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import datetime

import pytz


tz = pytz.timezone('Asia/Shanghai')
current_time = datetime.datetime.now(tz)


def parse_args(check=True):
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_train_file_pattern', type=str, default='/output/mscoco_traindata/train-?????-of-00256',
                        help='input_train_file_pattern.')

    parser.add_argument('--inception_checkpoint_file', type=str, default='/data/helloworld309/showandtell-data/inception_v3.ckpt',
                        help='inception_checkpoint_file.')

    parser.add_argument('--train_dir', type=str, default='/data/helloworld309/showandtell-model/train',
                        help='train_dir.')

    parser.add_argument('--train_inception', type=str, default='False',
                        help='train_inception.')

    parser.add_argument('--number_of_steps', type=int, default=4000,
                        help='number_of_steps')

    parser.add_argument('--input_val_file_pattern', type=str, default='/data/helloworld309/showandtell-data/val-?????-of-00004',
                        help='input_val_file_pattern.')

    parser.add_argument('--checkpoint_dir', type=str, default='/data/helloworld309/showandtell-model/train',
                        help='checkpoint_dir.')



    parser.add_argument('--eval_dir', type=str, default='/data/helloworld309/showandtell-model/eval',
                        help='eval_dir')

    parser.add_argument('--checkpoint_path', type=str, default='/data/helloworld309/showandtell-model/train',
                        help='checkpoint_path')

    parser.add_argument('--vocab_file', type=str, default='/data/helloworld309/showandtell-data/word_counts.txt',
                        help='vocab_file')
    parser.add_argument('--input_files', type=str, default='COCO_val2014_000000224477.jpg',
                        help='input_files')

    FLAGS, unparsed = parser.parse_known_args()

    return FLAGS, unparsed


if __name__ == '__main__':
    FLAGS, unparsed = parse_args()

    for x in dir(FLAGS):
        print(getattr(FLAGS, x))
