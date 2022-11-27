import xlrd
from librery.config import Config
class ReadExel:

    # Create function for reading  data from Locators Excel file
    def read_testdata(self, sheetname):
        wb = xlrd.open_workbook(Config.VALUE_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

# Create function for reading  VALES from Excel file
    def read_locater(self, sheetname):
        wb = xlrd.open_workbook(Config.DATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d
