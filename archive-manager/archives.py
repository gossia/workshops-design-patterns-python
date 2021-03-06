class Archive(object):
    def __init__(self, location_path):
        self.location_path = location_path

    def read(self):
        raise NotImplementedError()


class ZipArchive(Archive):

    def read(self):
        print("Reading files from zip archive")


class TarArchive(Archive):

    def read(self):
        print("Reading files from tar archive")
