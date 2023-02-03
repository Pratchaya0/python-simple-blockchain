class Title_Deed:
    def __init__(self, title_deed_number, data_time, parcel_number, near_parcel_number, owner, subdistrict_name, district, province, estimated_area_of_land, drafter,  map_investigator):
        self.title_deed_number = title_deed_number              # โฉนดที่ดินเลขที่
        self.data_time = data_time                              # วัน-เวลาที่ออก
        self.parcel_number = parcel_number                      # เลขที่ดิน
        self.near_parcel_number = near_parcel_number            # เลขที่ดินใกล้เคียง
        self.owner = owner                                      # เจ้าของ
        self.subdistrict_name = subdistrict_name                # ตำบล
        self.district = district                                # อำเภอ
        self.province = province                                # จังหวัด
        self.estimated_area_of_land = estimated_area_of_land    # ที่ดินแปลงนี้มีเนื้อที่ประมาณ
        self.drafter = drafter                                  # ผู้เขียนแผนที่
        self.map_investigator = map_investigator                # ผู้ตรวจแผนที่
