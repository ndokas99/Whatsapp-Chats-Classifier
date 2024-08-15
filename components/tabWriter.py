from multiprocessing import Process
from re import findall, split, escape, sub
from sys import stdout, stderr, exc_info
from emoji import get_emoji_regexp


def process(index, text, msg, _start, _end):
    try:
        count = 1
        emoji_re = get_emoji_regexp()
        for sent in msg:
            sent = sub(emoji_re, "", sent)
            try:
                line = findall(r"\d{1,2}/\d{1,2}/\d{1,4}, \d{1,2}:\d{1,2} - .*?: " + escape(sent), text)[0]
            except IndexError:
                continue
            date = findall(r"\d{1,2}/\d{1,2}/\d{1,4}, \d{1,2}:\d{1,2}", line)[0]
            name = split(r"- |:", line)[2]
            _start += f"<div><p><span class=\"span1\">{name}</span><span class=\"span2\">{date}</span></p>" \
                      f"<p>{sent}</p></div>\n"
            count += 1
            stdout.write(f"{index} {count}")
            stdout.flush()
        result = _start + _end
        with open(f"temp/{index}", "w", encoding="utf-8") as f:
            f.write(result)
    except IndexError:
        error = exc_info()
        error = f"{error[2].tb_frame} : lineno {error[2].tb_lineno}"
        stderr.write(error)
        stderr.flush()


if __name__ == "__main__":
    args = open("temp/state", "r", encoding="utf-8").read()
    start, end, txt, msgs = args.split(":<arg>:")
    emoji_char = get_emoji_regexp()
    txt = sub(emoji_char, "", open(txt, "r", encoding="utf-8").read())
    msgArray = eval(msgs)

    for i in range(7):
        proc = Process(target=process, args=(i, txt, msgArray[i], start, end))
        proc.start()
