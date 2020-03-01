import requests
import pickle as pkl

url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={'ENGINESIZE':3.3, 'Gasoline':0, 'Prem_Gasoline':1})
print('API:',r.json())

# Compare api call results with local model
model = pkl.load(open('mlr_model.pkl','rb'))
print('Local:',model.predict([[3.3, 0, 1]]))