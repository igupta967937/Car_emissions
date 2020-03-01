# Car_emissions
Machine learning models to predict car emissions for new car models

## Multiple linear regressions:
The best independent variables were selected from correlation scores, p-values and multi-collinearity corrections

## Flask app

### To run project
- If running the project for the first time or new data is acquired, generate a serialized version of the model which will be stored as 'model.pkl' file

```
python mlr_model.py
```
- Check that the model is setup properly by running:
```
python predict.py
```
This script can also be used to send direct POST requests to FLask API

- Fire up the API to run the GUI on port 5000:
```
python api_app.py
```
- In the browser, the app should be running on http://localhost:5000 and should display as follows:

![GUI sample](https://github.com/wgova/Car_emissions/blob/master/API_app/img/app_GUI.png)

After entering the required values, press "Calculate prediction" and something similar to the below should be displayed:

![Results sample](https://github.com/wgova/Car_emissions/blob/master/app/img/APi_app/app_GUI.png)
