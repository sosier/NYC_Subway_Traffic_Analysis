import re


def GetDataURLs(inputFile):
    with open(inputFile) as f:
        HTMLstrings = [line.strip() for line in f]

    HTMLstring = "".join(HTMLstrings)

    return re.findall(r"data[a-zA-Z0-9_\/]*\.txt", HTMLstring)

# print(GetDataURLs("data/rawHTMLdataURLs.txt"))
