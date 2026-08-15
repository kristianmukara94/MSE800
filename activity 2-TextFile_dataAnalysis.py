class DataAnalysisJunkFile:

    def __init__(self, filename="junk.txt"):
        self.filename = filename

    def count_lines(self):
        with open(self.filename, "r") as data:
            content = data.readlines()

        total_lines = len(content)
        print("Total number of lines:", total_lines)

    def write_data(self):
        with open(self.filename, "a") as data:
            data.write("\ntext file analysis\n")

    def convert_to_lowercase(self):
        with open(self.filename, "r") as data:
            content = data.read()

        with open(self.filename, "w") as data:
            data.write(content.lower())


# Create object
data_analysis = DataAnalysisJunkFile()

# Call methods
data_analysis.count_lines()
data_analysis.write_data()
data_analysis.convert_to_lowercase()