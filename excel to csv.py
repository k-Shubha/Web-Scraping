# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:45:35 2019

@author: SiriRamana
"""

import pandas as pd
data_xls = pd.read_excel(r'C:\Users\SiriRamana\Documents\Book1.xlsx', index_col=None)
data_xls.to_csv(r'C:\Users\SiriRamana\Documents\Book1.csv', encoding='utf-8')