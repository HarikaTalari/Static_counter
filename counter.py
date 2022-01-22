class Ticket:
    counter=0
    def __init__(self,source,passenger_name,destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None
        Ticket.counter+=1
        

    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def validate_source_destination(self):
        source=self.get_source().upper()
        destination=self.get_destination().upper()
        if ((source=="Delhi".upper()) and (( destination=="Mumbai".upper()) or (destination=="Pune".upper()) or (destination=="chennai".upper()) or (destination=="Kolkata".upper()))):
            return True
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination() is True:
            if Ticket.counter<10:
                self.__ticket_id=self.get_source()[0]+self.get_destination()[0]+str("0")+str(Ticket.counter)
            else:
                self.__ticket_id=self.get_source()[0]+self.get_destination()[0]+str(Ticket.counter)
            return  self.__ticket_id
        else:
            self.__ticket_id=None

ticket=Ticket("Delhi","Hello","Mumbai")
print(ticket.validate_source_destination())
print(ticket.generate_ticket())


