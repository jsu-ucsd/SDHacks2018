from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='9f4c8fdd79b24c4aa14ed9f3fec060e2')
model = app.public_models.general_model

def picPredict( imageLink ): #url should be a string
    response = model.predict_by_url(url= imageLink)
    concepts = response['outputs'][0]['data']['concepts']

    for concept in concepts:
        results = (concept['name'], concept['value'])

    return results


