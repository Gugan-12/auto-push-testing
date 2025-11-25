import azure.functions as func
import logging



# On the top-right, click “Add file” → “Upload files”.

# Open your local backend folder on your computer.

# Select all the files and subfolders inside it (not the folder itself).
# GitHub will show all the files to be uploaded or replaced.

# Existing files (like app.py, requirements.txt, etc.) will be overwritten automatically.

# Scroll down and in the Commit message, type:

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="autopushtesting")
def autopushtesting(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')


    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "Hi bro.",
             status_code=200

        )
