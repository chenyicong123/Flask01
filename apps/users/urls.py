from apps.users.login import VerificationCodeHandler, LoginHandler, UserInfoHandler, LogoutHandler

urls = [
    ('code/', VerificationCodeHandler.as_view('login_code')),
    ('login/', LoginHandler.as_view('login')),
    ('logout/', LogoutHandler.as_view('user_logout')),
    ('info/', UserInfoHandler.as_view('user_info')),

]
