from sys import stdout
from pickle import load
from os import remove


def process(input_data):
    with open("models/AppModel.bin", "rb") as model:
        classifier, pipeline = load(model)
    for info in input_data:
        processed = pipeline.transform([info])
        prediction = classifier.predict(processed)
        if prediction[0] != 7:
            stdout.write(f"{prediction[0]}")
            stdout.flush()
        else:
            continue


if __name__ == "__main__":
    data = open("temp/processed.txt", "r", encoding="utf-8").read().split(":~:")
    remove("temp/processed.txt")
    process(data)
