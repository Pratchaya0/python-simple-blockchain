import hashlib
import datetime

class Transaction:
    def __init__(self, index, title_deed):
        self.index = index
        self.title_deed = title_deed
        self.hash = self.calculate_hash()
        self.datetime = datetime.datetime.now()

    def calculate_hash(self):
        sha = hashlib.sha256()
        details = [self.title_deed.title_deed_number, self.title_deed.data_time, self.title_deed.parcel_number, self.title_deed.near_parcel_number, self.title_deed.owner, self.title_deed.subdistrict_name, self.title_deed.district, self.title_deed.province, self.title_deed.estimated_area_of_land, self.title_deed.drafter, self.title_deed.map_investigator]
        for detail in details:
            sha.update(str(detail).encode('utf-8'))
        sha.update(str(self.index).encode('utf-8'))
        return sha.hexdigest()
