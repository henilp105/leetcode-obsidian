Select firstName,lastName,city,state From Person Left Outer Join Address On (Person.personId=Address.personId)