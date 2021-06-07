from svgtrace import trace


class SVGConverter:
    def __init__(self, filepath, directory, filename):
        self.filepath = filepath
        self.directory = directory
        self.filename = filename

    def convertToSVG(self):
        bw = open(self.directory + "/" + self.filename + ".svg", "w")
        bw.write(trace(self.filepath))
        bw.close()
