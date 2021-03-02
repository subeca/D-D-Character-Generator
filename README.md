# D-D-Character-Generator
## Introduction
The aim of this second project is to create a very simple web application consisting of four services. The first service is the front-end which interacts with the back-end service- in this case is the fourth service. The result of these services is allowing the user to view the page while the back-end service is required to interact with the two remaining services to generate a random object. The requirements for this project are as follows:

*	Using a Kanban board
*	An app fully integrated using the feature-branch model into a version control system
*	Built through a CI server and being deployed to a cloud-based virtual machine
*	Have two different versions of the application that can be interchangeable
*	Using webhooks allowing Jenkins to automatically deploy application with the changes
*	Must be deployed using containerization and an orchestration tool
*	Using Ansible Playbook which provides an environment for the app to run
*	Use of reverse proxy to allow accessibility to the user

My project looks at creating Dungeons and Dragons characters where service 2 creates random class while the service 3 creates a random race from a list correspondingly. Service-1 allows the user to view the page with a click of a button and service-4 interacts with service-2 and service-3 to generate a random trait whether this is physical or personality.

## ER Diagram
The following diagram summarises the table used for this project where the database stores the data inputted and ID is the primary key.

![erd (2)](https://user-images.githubusercontent.com/77278616/109594861-638d6680-7b0b-11eb-840b-f96ecf31af5d.jpg)

## Services
The following diagram demonstrates how each of the services outlined earlier interacts with each other. Service 2 creates random classes while service 3 creates random races where the output from both services gets pulled to service 1 through a GET request while getting also ‘POSTED’ to service 4. The arrow going from service 4 to service 1 shows the traits being generated using data from service 2 and service 3 which is displayed in the front-end, service-1.

![SERVICE DIAGRAM (3)](https://user-images.githubusercontent.com/77278616/109595103-c7179400-7b0b-11eb-8c66-f6a9b04a90ad.jpg)

## CI Pipeline

