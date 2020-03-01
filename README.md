# Car_emissions
Machine learning models to predict car emissions for new car models

## Multiple linear regressions:
The best independent variables were selected from correlation scores, p-values and multi-collinearity corrections

## Flask app

### Running the project
If running the project for the first time or new data is acquired, generate a serialized version of the model which will be stored as 'model.pkl' file

```
python model.py
```

This would create a 

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Homepage.png)

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
