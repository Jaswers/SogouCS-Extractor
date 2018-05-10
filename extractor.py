#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
#  Version: 1.00 (May 10, 2018)
#  Author: Jaswer Liu (liusiyang@64yang.com)
#
#  Contributors:
#   Jaswer Liu (liusiyang@64yang.com)
#
# =============================================================================
#  Copyright (c) 2011-2018. Jaswer Liu (liusiyang@64yang.com)
# =============================================================================
#  This file is part of Tanl.
#
#  Tanl is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License, version 3,
#  as published by the Free Software Foundation.
#
#  Tanl is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
# =============================================================================
import codecs
import os
from tqdm import tqdm
import argparse

def GetText(frname, cnt=0):
    text = ''
    with codecs.open(frname, 'r', encoding='GB18030') as fr:
        news = dict()
        while 1:
            try:
                lines = fr.readlines(100000)
                if not lines:
                    break
                for line in lines:
                    if line[:14] == '<contenttitle>':
                        cnt += 1
                        s=line[14:-16].strip()
                        text += s
                        text += '\n'
                        # print(s)
                    if line[:9] == '<content>':
                        s=line[9:-11].replace('', '').replace('　', ' ').strip()
                        text += s
                        text += '\n'
                        text += '\n'
                        # print(s)
            except Exception as e:
                print(e)
    return text, cnt


def GetFileNames(filedor):
    filenames=list()
    for root, dirs, files in os.walk(filedor):
        for file in files:
            if file[-3:] == 'txt':
                # print(os.path.join(root,file))
                filenames.append(os.path.join(root, file))
    return filenames


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='extractor', usage='python3 extractor.py -i input_dir -o out_dir',description = 'Sogoucs-Extractor',epilog = 'Jaswer')
    parser.add_argument('-i', '--input_dir', type = str,help='input file dir')
    parser.add_argument('-o', '--out_dir', type = str,help='out file dir')

    args = parser.parse_args()

    print(args.input_dir)
    filedir = args.input_dir
    target = args.out_dir + 'extracted_data.txt'
    finText = ''
    cnt = 0
    names = GetFileNames(filedir)
    for name in tqdm(names):
        text, cnt = GetText(name, cnt)
        finText += text
    print("total", cnt)
    with open(target, 'w') as fw:
        fw.write(finText)
    print("Done")

