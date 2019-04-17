# User stories

## Admin
    * I want to audit and verify the integrity of teachers and students (verify @student.uva)


## Users (base model for students and teachers)
    * I want to be able to see the status of all pending and completed transactions
    * I want to enter my temporal and geographical availability
    * I want to message other Users (a)synchronously 
    * I want to configure my profile settings

## Teachers
    * I want to log in and immediately see my profile information and requests from Students
    * I want to enter what I am looking for (OpenRequest)
    * I want to verify that I have accomplished my obligations to a Student
    * I want to enter the subjects that I can teach
    * If a Student does not deliver, I want to settle this
    * I want to have realtime insights into the temporal and geographical availability of a Student
    * I want to rate Students after they have provided a service to me

## Students
    * I want to see Teachers as fast and easy as possible within a certain radius of my location
    * I want to filter/sort Teachers by positive review ratio, service type, subject
    * If a Teacher does not deliver, I want to settle this
    * I want to verify that I have accomplished my obligations to a Teacher
    * I want to have realtime insights into the temporal and geographical availability of a Teacher
    * I want to rate Teachers after they have provided a service to me
    * I want to request meetings with Teachers
    * When I make a meeting request, I want to easily match my schedule with the Students schedule
    * I want to verify the integrity of ratings
    * I want to respond to OpenRequests from Teachers

## General notes

    * messaging system can operate fully independent from RDBMS (maybe use RabbitMQ or similar)
    * sort requirements by implementation phases
    * Best way of leveraging User and hooking profiles into the builtin auth system. Check https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#auth-custom-user

## Flows

Teachers

Login --> ProfilePage --> OpenRequestsPage --> MeetingForm --> MeetingEditForm --> ProfilePage --> Logout
Login --> ProfilePage --> SettingsEditForm --> ProfilePage --> Logout
Login --> ProfilePage --> ProfileEditForm --> ProfilePage --> Logout

Students

Login --> TeacherListing --> MeetingForm --> MeetingEditForm --> Logout
Login --> TeacherListing --> ProfilePage --> SettingsEditForm --> Logout
Login --> TeacherListing --> ProfilePage --> ProfileEditForm --> ProfilePage --> Logout
