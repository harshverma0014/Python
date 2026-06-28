# import pandas as pd
# s=pd.Series([23,34,54,64,37])
# print(s)




# import pandas as pd
# s=pd.Series(["harry","peter","thomas","vickey"],index=[100,200,300,400])
# print(s)



import numpy as np
import pandas as pd

a=np.array(["harry","peter","thomas","vickey"])
s=pd.Series(a,index=[100,200,300,400])
print(s[200])