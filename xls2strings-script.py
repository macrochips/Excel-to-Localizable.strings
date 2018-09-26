from xlrd import open_workbook

class Arm(object):
    def __init__(self, source_str, destination_str):
        self.source_str = source_str
        self.destination_str = destination_str

    def __str__(self):
        return("Arm object:\n"
               "  BaseLanguage = {0}\n"
               "  LocalisedLanguage = {1}"
               .format(self.source_str.encode('utf-8'), self.destination_str.encode('utf-8')))

wb = open_workbook('Input-Excel-File.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value)).encode('utf-8')
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Arm(*values)
        items.append(item)

with open('Localizable.strings', 'w') as f:
    for item in items:
        print >> f ,"\"{0}\" = \"{1}\";".format(item.source_str.encode('utf-8'), item.destination_str.encode('utf-8')) # Python 2.x
        # print("\"{0}\" = \"{1}\";".format(item.source_str.encode('utf-8'), item.destination_str.encode('utf-8')), file=f)  # Python 3.x