import argparse
from io import StringIO
import re
import requests

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from tqdm import tqdm

import cfg


def is_float(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True


def get_text_from_pdf(pdfname, caption, skip_header, skip_footer):
    # PDF 読み込み
    fp = open(pdfname, 'rb')
    texts = []

    for page in tqdm(PDFPage.get_pages(fp, pagenos=None, maxpages=0, password=None, caching=True, check_extractable=True)):
        rsrcmgr = PDFResourceManager()
        out_fp = StringIO()
        la_params = LAParams()
        la_params.detect_vertical = True
        device = TextConverter(rsrcmgr, out_fp, codec='utf-8', laparams=la_params)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        interpreter.process_page(page)
        texts.append(out_fp.getvalue())
        device.close()
        out_fp.close()
    fp.close()

    output = ""

    # 文章成形
    for text in tqdm(texts):
        lines = text.splitlines()
        replace_strs = [b'\x00']  # 除去するutf8文字
        new_lines = []
        for line in lines:
            line_utf8 = line.encode('utf-8')
            for replace_str in replace_strs:
                line_utf8 = line_utf8.replace(replace_str, b'')
            line = line_utf8.decode()
            line = re.sub("[ ]+", " ", line)  # 連続する空白を一つにする
            line = line.strip()
            if len(line) == 0:
                continue  # 空行は無視
            if is_float(line):
                continue  # 数字だけの行は無視
            new_lines.append(line)

        for index in range(len(new_lines)):
            if index == 0 and skip_header:
                continue
            if index == len(new_lines)-1 and skip_footer:
                continue
            line = new_lines[index]
            # 見出しで改行
            if is_float(line.split(".")[0]) and len(line.split()) < caption and (not line.endswith(".")):
                output += str(line)
                output += "\r\n"
                continue

            if line.endswith("."):
                output += str(line)
                output += "\r\n"
            elif line.endswith("-"):
                # 前の行からの続きの場合
                output += str(line[:-1])
            elif line.endswith(":"):
                # 数式が続く場合
                output += str(line)
                output += "\r\n"
            else:
                # それ以外の場合は、単語の切れ目として半角空白を入れる
                output += str(line)
                output += " "

    return output


def translate(text, api_index):
    url = cfg.api[api_index]
    params = {
        'text': text,
        'source': "en",
        'target': "ja"
    }
    req = requests.get(url, params=params)
    return req.text


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="path to pdf file")
    parser.add_argument("--api", type=int, default=0, help="cfg.py の何番目の API を使用するか")
    parser.add_argument("--skip", type=int, default=0, help="PDFのheader(1行)やfooter(1行)を読み飛ばしたい場合 header: 1, footer: 2, header&footer: 3, no-skip: 0")
    parser.add_argument("--caption", type=int, default=10)
    args = parser.parse_args()

    skip_header = False
    skip_footer = False
    if args.skip == 1 or args.skip == 3:
        skip_header = True
    if args.skip == 2 or args.skip == 3:
        skip_footer = True

    # pdfをテキストに変換
    input = get_text_from_pdf(args.input, caption=args.caption, skip_header=skip_header, skip_footer=skip_footer)

    # 抽出した文章の書き出し
    with open("text.txt", "w", encoding="utf-8") as f_text:
        f_text.write(input)

    # 翻訳
    lines = input.split("\r\n")
    translated_line = ""
    for line in tqdm(lines):
        if line:
            translated_line += (translate(line, api_index=args.api) + "\r\n")
        else:
            translated_line += "\r\n"

    # 翻訳した文章の書き出し
    with open("jpn_text.txt", "w", encoding="utf-8") as f_text:
        f_text.write(translated_line)


if __name__ == "__main__":
    main()
