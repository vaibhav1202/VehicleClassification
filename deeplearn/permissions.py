from rest_framework import permissions
class MyPers(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser       
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser    

class MyPers2(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "DELETE":
            return request.user.is_superuser
        return request.user.is_superuser or obj.user.id == request.user.id

class MyPers3(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_superuser
 
class MyPers4(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser           
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_superuser    
