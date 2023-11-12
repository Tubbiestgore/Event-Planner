# Overview

This project is desgined as a test of cloud database software engineering. In essence it is designed as an application of principles related to the subject in the skein of working within the cloud.

The program itself is a basic Event Planner it utilizes calls to a cloud server in order to store data as inputed by the user. Simply run the program and select the options that you want to work with. The software will take care of the rest. As stated this program is extremly basic. The difficult part of this project was figuring out how to working with a cloud database. 

As stated above the purpose in writing this software is to further my knowledge and skills when working within the cloud and its databases. How to utilizes such resources and integrate them into my own software.

[Software Demo Video](https://youtu.be/Jm4szPOmXZo)

# Cloud Database

The cloud firestore is a NoSQL document database provided by Google Cloud Platform. In essence, it is designed to store and synchronize data accross multiple clients, such as when working with an app, and provides support for large amounts of both users and data. It stores data in JSON like documents instead of the tranditional table based structure. It also has great network security, regular updates, and other such commodities, although many of such services do. 

The structure itself is a collection document model on a NoSQL database. Within we have an event collection and a guest list collection. With some edits you can associate these collections with one another. We can see that this sort of structure allows for relationships ebtween the variables at play. 

# Development Environment

For this projcet I utilized firebase which is a cloud database service, and vscode via the python programming language. I also used import firebase-admin which is the python library provided by firebase for interacting with their servers. 

The language which I used for this project was the python programming language. A good choice for networking and working within the cloud. Lots of documentation is provided to help one get started when working in this manner. 

# Useful Websites

- [Operation of Firebase on VScode](https://www.youtube.com/watch?v=-3GkNz1lfCE)
- [CLoud Databases](https://en.wikipedia.org/wiki/Cloud_database)
- [Working with cloud firestore](https://pypi.org/project/google-cloud-firestore/0.28.0/)
- [Python Firestore Example](https://www.youtube.com/watch?v=gwDXvMqJ2PY)

# Future Work

- Better connections between collections
- More understanidng of Cloud structure - specifically language orientation (which is best for said development etc...)
- More in depth Event Planner