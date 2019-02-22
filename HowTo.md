## How to deploy this sample app

### Prerequisites:

1. Install the Azure CLI
2. Install Docker
3. Install the Azure Functions Core Tools

### Instructions:

4. Create a Python 3.6 VirtualEnv and activate it (I recommend using pyenv virtualenv).
5. From `AzTFServerless` folder, run `pip -r requirements.txt --ignore-installed`
6. Run the severless function locally by running `func host start`. This spins up a server. You can use the convenient `upload.html` file to upload an image to the API and see the results from our ML model.


7. Follow the instructions for functions deployment here: https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python . You'll be create a resource group, storage account and a linux function app (on the consumption plan). (Note: my app is called `tfserverless` which is used the following instructions).

8. Deploy the Function App.

Depending on your system version of Python you might not be able to use both the VirtualEnv and the Azure CLI at the same time. Deploy instead by executing a build in a Docker container:

```
func azure functionapp publish tfserverless --build-native-deps
```

If your system Python is Python 3.6 you may deploy via `func azure functionapp publish tfserverless`.

9. To test our deployed API, update the HTML form action in the handy form upload page `upload.html` provided so that it points to the new functions app URL, including the function key param.
