# Development Notes 

username: karl
password: password

Django djoser 
pip install -U djoser
Django rest api Framework


--------
Dashboard needed
Log in -> Dashboard -> view projects -> tickets -> comments
--------
Models

# Comment Model:

class Comment(models.Model):
    ticketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.TextField()
    dateCreated =
    createdBy = models.CharField(max_length=100)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

# Project Model:

Id = primary_key
title
detail
TotalNumberOfTickets
TicketsComplete
TicketsToDO
TicketsInProgress
TicketsOverDue