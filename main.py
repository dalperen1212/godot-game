class merhaba:
    def __init__(self,name,yaş):
        self.name = name
        self.yaş = yaş
    def __str__(self):
        return f"{self.isim} kişisi {self.yaş} yaşında"
        
alperen = merhaba('alperen',15)
print(alperen.yaş)