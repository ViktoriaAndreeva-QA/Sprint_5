class Urls:
    BASE = "https://stellarburgers.education-services.ru"

    @classmethod
    def main_page(cls):
        return cls.BASE
    
    @classmethod
    def register_page(cls):
        return f"{cls.BASE}/register"
    
    @classmethod
    def login_page(cls):
        return f"{cls.BASE}/login"
    
    @classmethod
    def profile_page(cls):
        return f"{cls.BASE}/account/profile"
    
    @classmethod
    def forgot_password_page(cls):
        return f"{cls.BASE}/forgot-password"
