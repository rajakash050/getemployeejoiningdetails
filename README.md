# API-Creation-in-Django

Here is the Rest APi application which can fetch all the member details of an office and their respecive start and end date in the organization.

Mainly two tables as follows:
Member
Activity_periods

Database Used:
MySql

Framework used for this backend application is Django and the server side language used is Python.

Packages related to this service are included in the requirement.txt file in the Repository.

Http Method which is used to request this Endpoint is GET

The example of the response is as follows:

{"members": [{"id": 11, "activity_periods": [{"start_date": "06/11/2020", "end_date": "06/11/2020"}, {"start_date": "06/12/2020", "end_date": "06/12/2020"}], "member_name": "jack", "member_desc": "America/Los_Angeles"}, {"id": 12, "activity_periods": [], "member_name": "mack", "member_desc": "Asia/Kolkata"}], "ok": true}

