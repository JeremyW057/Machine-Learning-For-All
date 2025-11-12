import pandas as pd
import numpy as np
import pickle
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

##Build Model from provided csv file
def build_model(csv,iv,dv):
    df = pd.read_csv(csv)
    df.columns = df.columns.str.strip()
    X = df[iv]
    Y = df[dv]
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.4)
    model = LinearRegression()
    model.fit(x_train,y_train)
    
    ##Get some predicted values to plot
    y_pred = model.predict(x_test)
    
    ##Convert to 1D float array for plotting
    y_test_arr = np.asarray(y_test, dtype=float).flatten()
    y_pred_arr = np.asarray(y_pred, dtype=float).flatten()
    
    ##Plot actual vs predicted vaules 
    plt.figure()
    if len(iv) == 1:
        # One IV: plot actual vs predicted along that IV
        x_axis = x_test[iv[0]]
        plt.scatter(x_axis, y_test_arr, color='red', label='Actual Values')
        plt.scatter(x_axis, y_pred_arr, color='blue', alpha=0.6, label='Predicted Values')

        plt.xlabel(iv[0])
        plt.ylabel(', '.join(dv))
        plt.title('Actual vs Predicted Values (Single IV)')
    else:
        # Multiple IVs: X-axis = sample index, show actual vs predicted with residual lines
        plt.scatter(range(len(y_test_arr)), y_test_arr, color='red', alpha=0.7, label='Actual Values')
        plt.scatter(range(len(y_test_arr)), y_pred_arr, color='blue', alpha=0.6, label='Predicted Values')

        # Residual lines
        for i in range(len(y_test_arr)):
            plt.plot([i, i], [y_test_arr[i], y_pred_arr[i]], color='gray', alpha=0.3)

        plt.xlabel('Test Sample Index')
        plt.ylabel(', '.join(dv))
        plt.title('Actual vs Predicted Values (Multiple IVs)')

        
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./static/model_tests.png')
    plt.close()
    
    ##Generate model score
    score = f'{100*model.score(x_test,y_test): 0.2f}'
    
    ## Create downloadable file
    with open('./static/model_pickle', 'wb') as model_file:
        pickle.dump(model,model_file)
    
    ##Model data (Coeffecients, Intercepts, and model score)
    coef = model.coef_.tolist()
    intercept = model.intercept_.tolist() if hasattr(model.intercept_, '__iter__') else model.intercept_
    
    tup = (coef,intercept,score)
    return tup 
##Clean up data?