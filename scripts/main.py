from urllib.error import HTTPError, URLError
from urllib.request import urlopen


SOURCE_URLS = [
    "https://www.openml.org/data/get_csv/3594/dataset_113_primary-tumor.arff",
    "https://archive.ics.uci.edu/ml/machine-learning-databases/primary-tumor/primary-tumor.data",
]


def stream_rows():
    last_error = None
    for source_url in SOURCE_URLS:
        try:
            with urlopen(source_url, timeout=60) as response:
                for line in response:
                    yield line
            return
        except (HTTPError, URLError) as exc:
            last_error = exc
    raise RuntimeError(f"Unable to download primary-tumor source data: {last_error}")


with open("../data/primary-tumor.csv", "w") as bumps_file:
    # bumps_file.write("season,age,childish-disease,trauma,surgical-intervention,fevers,alcoholic,"
    #                  "smoking,sitting,output\n")
    for line in stream_rows():
        decodedLine = line.decode("UTF-8")
        decodedLine = decodedLine.replace("?", "")
        decodedLine = decodedLine.replace('"', "")
        decodedLine = decodedLine.replace("'", "")
        decodedLine = decodedLine.replace("yes", "true")
        decodedLine = decodedLine.replace("no", "false")
        decodedLine = decodedLine.lower()
        bumps_file.write(decodedLine.strip() + "\n")
    bumps_file.close()
