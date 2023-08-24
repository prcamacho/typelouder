class UserController:
    @classmethod
    def create_user():
        try:
            usuario.cerate()
        except:
            return {'message':'todo mal'}    
        return {'message':'ok'}