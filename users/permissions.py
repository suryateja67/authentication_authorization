from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self,request,view):
        print(request.user)
        if request.user.is_authenticated:
            if request.user.role=="Admin":
                return True
        return False
    
class ClientPermission(permissions.BasePermission):
    
    def has_permission(self,request,view):
        print(request.user)
        if request.user.is_authenticated:
            return request.user.role =='Client' and view.action !='create'
        return False
    