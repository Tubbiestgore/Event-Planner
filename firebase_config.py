import firebase_admin
from firebase_admin import credentials, firestore

# Dictionary to store initialized apps
initialized_apps = {}

def initialize_firebase():
    # Check if Firebase has already been initialized
    if not initialized_apps:
        cred = credentials.Certificate("event-planner-v2-firebase-adminsdk-vhc2l-830ab8ee40.json")
        app = firebase_admin.initialize_app(cred, name='event-planner-app')

        # Access Firestore database
        db = firestore.client(app=app)

        # Store the initialized app in the dictionary
        initialized_apps['event-planner-app'] = app

        return db

    # Return the existing database if Firebase has already been initialized
    return firestore.client(app=initialized_apps['event-planner-app'])