import numpy as np
def amape(actual,pred):
    #actual, pred = np.array(actual), np.array(pred)
    for a in actual:
        if a < 2000000:
            actual[a] = 2000000
            #mape =np.round(np.mean(np.abs((actual - pred) / actual)),4)
        else:
            None
            mape =np.round(np.mean(np.abs((actual - pred) / actual)),4)
            return mape

#def mape(actual, pred): 
 #   actual, pred = np.array(actual), np.array(pred)
  #  return np.mean(np.abs((actual - pred) / actual)) * 100