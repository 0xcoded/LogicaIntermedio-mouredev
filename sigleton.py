#Ejercicio

class Sigleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Sigleton, cls).__new__(cls)
        return cls._instance
    

    #Extra

class UserSession:
    id:int = None
    username:str = None
    name:str = None
    email:str = None
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    
    def setUser(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def getUser(self):
        return f"id: {self.id}, username: {self.username}, name: {self.name}, email: {self.email}"
    
    def clearUser(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None
        print("Sesión cerrada por el usuario.")

sesion = UserSession()
sesion.setUser(1,"0xcoded","david","test@test.com")
print(sesion.getUser())

#sesion.setUser...
sesion2 = UserSession()
#estamos accediendo a sesion, por lo que también varia sesión2
#sesion.setUser(1,"test","noelia","test@test.com")
print(sesion2.getUser())
sesion.clearUser()