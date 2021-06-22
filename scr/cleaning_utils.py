import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#  2. Eliminación de columnas que no son necesarias.

def columnas_innecesarias(data, list_columns):
    columnas_innecesarias = data.drop([list_columns], axis=1)
    return columnas_innecesarias

