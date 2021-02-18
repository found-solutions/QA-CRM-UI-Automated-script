import xlrd
import os


def find_file_abspath(start_dir, file_name):
    """
        start_dir: 开始查找文件的路径的目录名称 --> 'data'
        file_name: 需要查找的文件名称
        return： 查找到的文件的绝对路径
    """
    file_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), start_dir)
    for root, dirs, files in os.walk(file_path):
        if len(files) != 0:
            for f in files:
                if file_name == f:
                    p = os.path.join(root, f)
                    return p


class ExcelUtil:
    def __init__(self, excel_name, sheet_ame="Sheet1"):
        excel_path = find_file_abspath('data', excel_name)
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_ame)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for _ in range(1, self.rowNum):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    filepath = "member_login.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())
    i = find_file_abspath('data', 'address_proof.jpg')
    print(i)
