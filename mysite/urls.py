"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# When a user makes a request for a page on your web app, 
# Django controller takes over to look for the corresponding view via the url.py file, 
# and then return the HTML response or a 404 not found error, if not found. 
# In url.py, the most important thing is the "urlpatterns" tuple. It’s where you define the mapping between URLs and views


urlpatterns = [
    path('polls/', include('polls.urls'), name = 'polls'),
    path('admin/', admin.site.urls),  # Syncdb sẽ tạo các bảng hoặc bộ sưu tập cần thiết tùy thuộc vào loại DB của bạn, cần thiết cho giao diện quản trị để chạy
    # using this command: python manage.py createsuperuser để tạo username and password for admin interface
]


# Sau khi đăng nhập vào giao diện admin:
# Giao diện sau đó sẽ cho phép bạn quản lý các nhóm Django và người dùng và tất cả các mô hình đã đăng ký trong ứng dụng của bạn. 
# Giao diện cung cấp cho bạn khả năng thực hiện ít nhất các hoạt động "CRUD" (tạo, đọc, cập nhật, xóa) trên các mô hình của bạn.