import argparse
import logging
import os
import gzip


class OptionPerLineParser(argparse.ArgumentParser):
    def convert_arg_line_to_args(self, arg_line):
        if arg_line.startswith("#"):
            return []
        return arg_line.split()


def smart_open(path):
    if path.endswith('.gz'):
        return gzip.open(path)
    else:
        return open(path)


def ensure_dir(p):
    parent = os.path.dirname(p)
    if not os.path.exists(parent):
        os.makedirs(parent)


def tokens_to_sent(tokens, sent_start):
    sent = ""

    for token, span in tokens:
        if span[0] > len(sent) + sent_start:
            padding = ' ' * (span[0] - len(sent) - sent_start)
            sent += padding
        sent += token
    return sent


def find_by_id(folder, docid):
    for filename in os.listdir(folder):
        if filename.startswith(docid):
            return os.path.join(folder, filename)


def set_basic_log(log_level=logging.INFO):
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)
