#### import csv then clean it and then categorize the column and then plot it
import pandas as pd

from matplotlib import pyplot as plt # importing this module for potting


D = pd.read_csv('fico (1).csv',header=0)
D["FICO"] = pd.to_numeric(D["FICO"],errors="coerce") # using pd.to_numeric to convert not numeric values to nan
Data_fill = D.dropna() # filterdata

# to categorise the fico rate into 5 categories
#Poor (less than 580),Fair (580 to 669),Good (670 to 739),Very Good (740 to 799),Exceptional (800 to 850)
# 300 - 580, 581-669, 670-739, 740- 799, 800 -850
DataCate = pd.cut(Data_fill['FICO'], bins=[300, 581,670 , 740,800,851], include_lowest=True, labels=['Poor','Fair','Good','Very Good'
                                                 ,'Exceptional'])
#print(DataCate.value_counts(),'\n',DataCate.value_counts()/len(DataCate)*100)
DataCate.hist(bins=5) # Creating histogram with 5bars/bins

plt.show()
Region = pd.read_csv("region.csv")
print(Region.head(20))
Merged_data = pd.merge(Data_fill,Region, on="acct_id",how="left")
print(Merged_data.head(),"\n",Merged_data.tail())