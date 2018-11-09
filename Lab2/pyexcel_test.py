import pyexcel
from collections import OrderedDict
#2 Prepare data
data = [
    OrderedDict({
        "Name": 'Cong',
        "Age": 21,
    }),
    OrderedDict({
        "Name": 'Mymy',
        "Age":21,
    }),
]
#3 Save file using save_as()
pyexcel.save_as(records= data, dest_file_name="sampl.xlsx")