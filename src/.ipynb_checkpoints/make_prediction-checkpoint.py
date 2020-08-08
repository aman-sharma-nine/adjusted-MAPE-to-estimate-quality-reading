import pandas as pd
import numpy as np


def get_predictions(project_id,model_id,external_set):
    proj=dr.Project.get(project_id)
    model=proj.get_models(search_params={'sample_pct': 100})[0]
    #upload external set
    external= proj.upload_dataset(external_set)
    predict_job=model.request_predictions(external.id)
    predict_job.wait_for_completion()
    #get predictions
    predictions = predict_job.get_result_when_complete()
    predictions['exp_predictions'] = np.exp(predictions['prediction'])
    
    #reset_index 
    #external.reset_index(inplace=True)
    #predictions.reset_index(inplace=True)
    
    #result concat it with actuals
    

if __name__ == '__main__':
    get_predictions()
    