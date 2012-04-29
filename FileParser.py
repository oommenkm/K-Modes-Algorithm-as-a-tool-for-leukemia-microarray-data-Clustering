#!/usr/bin/env python
"""
This utility module will parse the input data file into a 2D list for the k-modes clustering

Writen on: 25th Feb 2012

Author: Oommen Mathew
"""
import math

class FileParser():
    """
    Parses the csv file and caluculates the sum and count of the
    positive and negative items separately.
    """
    def  __init__(self, data_file=""):
        FH = open(data_file, 'r')
        self.AML_count=0
        self.ALL_count=0
        self.whole_data_list = []
        self.lns = FH.readlines()
        FH.close()

        self.AML_value_sum = []
        self.ALL_value_sum = []
        self.AML_values = []
        self.ALL_values = []
        
        self.AML_mean = []
        self.ALL_mean = []
        self.AML_standard_dev = []
        self.ALL_standard_dev = []

        for i in range(0,7129):
            self.AML_values.append([])
            self.ALL_values.append([])
            self.AML_value_sum.append(0)
            self.ALL_value_sum.append(0)
        
        self.mean_dif_value = []
        self.t_test_value = []
        self.sqrt_std_dev = []
    
    def parse_file(self):
        for ln in self.lns[1:]:
            cur_vals = []
            flds=ln.split(',')
            if(flds[7129].find('AML')>=0):
                self.AML_count=self.AML_count+1
                for i in range(7129):
                    #cur_fld_val = flds[i]
                    self.AML_values[i].append(int(flds[i]))
                    self.AML_value_sum[i] = self.AML_value_sum[i] + int(flds[i])
                    cur_vals.append(int(flds[i]))
            else:
                self.ALL_count=self.ALL_count+1
                for i in range(7129):
                    #cur_fld_val = flds[i]
                    self.ALL_values[i].append(int(flds[i]))
                    self.ALL_value_sum[i] = self.ALL_value_sum[i] + int(flds[i])
                    cur_vals.append(int(flds[i]))
            
            flds[-1] = flds[-1].replace('\n', '')
            cur_vals.append(flds[-1])
            self.whole_data_list.append(cur_vals)
        return self.whole_data_list
    
    
def main():
    kn_in_file_obj = FileParser("luekemia.csv")
    km_in_vals = kn_in_file_obj.parse_file()
    print km_in_vals
    
if __name__ == '__main__':
    main()