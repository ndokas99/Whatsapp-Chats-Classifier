from re import search, sub, split
from emoji import emoji_count, get_emoji_regexp
from multiprocessing import Process
from sys import argv, stdout, stderr
from math import floor


def process(array: list):
    emoji_char = get_emoji_regexp()
    with open("temp/processed.txt", "a", encoding='utf-8') as file_obj:
        for i in range(len(array)):
            sentence = array[i]
            if not search(r".*?:\s", sentence):
                pass
            elif search(r'<Media omitted>', sentence):
                pass
            elif search(r'[.].*? [(]file attached[)]', sentence):
                pass
            elif search(r'This message was deleted', sentence):
                pass
            elif search(r'Waiting for this message', sentence):
                pass
            else:
                try:
                    text = split(r".*?:\s", sentence)[1]
                except IndexError:
                    stderr.write(f"{sentence}")
                if len(text) < 4:
                    pass
                elif emoji_count(sentence) > 0:
                    text = sub(emoji_char, "", text)
                    text = sub(r"<", "&lt;", text)
                    text = sub(r">", "&gt;", text)
                    if len(text) > 2:
                        file_obj.write(text + ":~:")
                elif sentence != "":
                    text = sub(r"<", "&lt;", text)
                    text = sub(r">", "&gt;", text)
                    file_obj.write(text + ":~:")
                else:
                    pass
                stdout.write("_")
                stdout.flush()
            stdout.write("_")
            stdout.flush()


if __name__ == "__main__":
    file = open(argv[1], mode="r", encoding='utf-8')
    lines = split(r"\d{1,2}/\d{1,2}/\d{1,4}, \d{1,2}:\d{1,2} - .*?", file.read())
    lines.pop(0)
    stderr.write(str(len(lines)))
    stderr.flush()

    div5 = floor(len(lines) / 5)
    upper = [div5 * a for a in range(1, 6)]
    lower = [num - div5 for num in upper]
    upper[-1] = len(lines) + 1
    limits = [(x, y) for (x, y) in zip(lower, upper)]

    arrays = [[] for x in range(5)]
    for j in range(5):
        arrays[j] = lines[limits[j][0]:limits[j][1]]

    procs = []

    for group in arrays:
        proc = Process(target=process, args=(group,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
