"""
代碼生成器 - 藍圖小老鼠
根據用戶回答生成完整的代碼框架
"""

import json
from typing import Dict, List, Any


# 代碼生成提示詞模板
CODE_GENERATION_PROMPT = """基於用戶的回答,生成完整的代碼框架。

模組名稱: {module_name}
模組說明: {module_description}
用戶回答: {user_answers}
框架選擇: {framework}

請生成以下文件的代碼:

1. models.py - 數據模型
2. views.py - API 端點 (或 routes.py)
3. serializers.py - 序列化器 (Django REST) 或 schemas.py (FastAPI)
4. urls.py - 路由配置
5. requirements.txt - 依賴列表

要求:
- 完整可運行的代碼
- 包含詳細註解
- 符合最佳實踐
- 包含錯誤處理
- 包含類型提示 (Python 3.9+)

請用 JSON 格式返回:
{{
  "files": {{
    "models.py": "代碼內容...",
    "views.py": "代碼內容...",
    "serializers.py": "代碼內容...",
    "urls.py": "代碼內容...",
    "requirements.txt": "依賴列表..."
  }},
  "setup_instructions": "安裝和運行說明"
}}

只返回 JSON,不要其他文字。
"""


def generate_code(
    module: Dict[str, Any],
    answers: List[int],
    framework: str = "django"
) -> Dict[str, Any]:
    """
    生成代碼框架
    
    Args:
        module: 模組資訊
        answers: 用戶回答列表
        framework: 框架選擇 (django/flask/fastapi/express/javascript)
        
    Returns:
        生成的代碼文件
    """
    # 根據框架選擇生成器
    if framework == "django":
        return generate_django_code(module, answers)
    elif framework == "flask":
        return generate_flask_code(module, answers)
    elif framework == "fastapi":
        return generate_fastapi_code(module, answers)
    elif framework in ["express", "javascript", "js"]:
        return generate_javascript_code(module, answers)
    elif framework in ["nestjs", "typescript", "ts"]:
        return generate_typescript_code(module, answers)
    elif framework in ["gin", "go", "golang"]:
        return generate_go_code(module, answers)
    else:
        raise ValueError(f"不支持的框架: {framework}")


def generate_django_code(module: Dict[str, Any], answers: List[int]) -> Dict[str, Any]:
    """生成 Django 代碼"""
    try:
        from django_generator import generate_django_code as django_gen
        return django_gen(module, answers)
    except ImportError:
        return generate_mock_code(module.get('name', 'demo'), 'Django')



def generate_flask_code(module: Dict[str, Any], answers: List[int]) -> Dict[str, Any]:
    """生成 Flask 代碼"""
    try:
        from flask_generator import generate_flask_code as flask_gen
        return flask_gen(module, answers)
    except ImportError:
        return {
            "files": {},
            "setup_instructions": "Flask 代碼生成功能開發中...",
            "framework": "Flask"
        }


def generate_fastapi_code(module: Dict[str, Any], answers: List[int]) -> Dict[str, Any]:
    """生成 FastAPI 代碼"""
    try:
        from fastapi_generator import generate_fastapi_code as fastapi_gen
        return fastapi_gen(module, answers)
    except ImportError:
        return {
            "files": {},
            "setup_instructions": "FastAPI 代碼生成功能開發中...",
            "framework": "FastAPI"
        }


def generate_javascript_code(module: Dict[str, Any], answers: List[int]) -> Dict[str, Any]:
    """生成 JavaScript/Express 代碼"""
    try:
        from javascript_generator import generate_javascript_code as js_gen
        return js_gen(module, answers)
    except ImportError:
        return {
            "files": {},
            "setup_instructions": "JavaScript 代碼生成功能開發中...",
            "framework": "Express.js"
        }


def generate_typescript_code(module: Dict[str, Any], answers: List[int]) -> Dict[str, Any]:
    """生成 TypeScript/NestJS 代碼"""
    try:
        from typescript_generator import generate_typescript_code as ts_gen
        return ts_gen(module, answers)
    except ImportError:
        return {
            "files": {},
            "setup_instructions": "TypeScript 代碼生成功能開發中...",
            "framework": "NestJS"
        }


def generate_go_code(module: Dict[str, Any], answers: List[int]) -> Dict[str, Any]:
    """生成 Go/Gin 代碼"""
    try:
        from go_generator import generate_go_code as go_gen
        return go_gen(module, answers)
    except ImportError:
        return {
            "files": {},
            "setup_instructions": "Go 代碼生成功能開發中...",
            "framework": "Gin"
        }


def parse_user_answers(module: Dict[str, Any], answers: List[int]) -> Dict[str, bool]:
    """
    解析用戶回答,提取功能需求
    
    Args:
        module: 模組資訊
        answers: 用戶回答列表
        
    Returns:
        功能需求字典
    """
    features = {
        '需要用戶關聯': True,
        '需要名稱': True,
        '需要狀態': True,
        '需要認證': True,
        '需要資料庫': True,
    }
    return features


def generate_mock_code(module_name: str, framework: str) -> Dict[str, Any]:
    """
    生成高品質的演示代碼 (Demo Mode)
    當用戶沒有 API Key 時使用，讓他們體驗完整流程。
    支持多種場景：部落格、聊天室、待辦事項、電商(默認)
    """
    name_lower = module_name.lower()
    
    # 1. 部落格場景
    if any(k in name_lower for k in ['blog', 'post', 'article', 'news', '部落格', '文章', '新聞']):
        return {
            "files": {
                "models.py": """from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="標題")
    content = models.TextField(verbose_name="內容")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name="是否發布")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="評論內容")
    created_at = models.DateTimeField(auto_now_add=True)
""",
                "views.py": """from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
""",
                "serializers.py": """from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author_name', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_name', 'created_at', 'comments']
""",
                "urls.py": """from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [path('', include(router.urls))]
""",
                "requirements.txt": "Django>=4.2.0\ndjangorestframework>=3.14.0\n"
            },
            "setup_instructions": "### 部落格系統 (Demo Mode)\n\n1. `pip install -r requirements.txt`\n2. `python manage.py migrate`\n3. `python manage.py runserver`"
        }

    # 2. 聊天室場景
    if any(k in name_lower for k in ['chat', 'message', 'im', '聊天', '訊息', '通訊']):
        return {
            "files": {
                "models.py": """from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
""",
                "consumers.py": """import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'chat_message', 'message': message}
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
""",
                "views.py": "# 聊天室使用 WebSocket (Channels)，此處僅為 HTTP API\nfrom django.shortcuts import render\n\ndef index(request):\n    return render(request, 'chat/index.html')\n",
                 "routing.py": r"""from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
""",
                "requirements.txt": "Django>=4.2.0\nchannels>=4.0.0\ndaphne>=4.0.0\n"
            },
            "setup_instructions": "### 即時聊天室 (Demo Mode)\n\n此專案使用 Django Channels 實現 WebSocket。\n\n1. 安裝: `pip install -r requirements.txt`\n2. 運行: `daphne -p 8000 myproject.asgi:application`"
        }

    # 3. 待辦事項場景
    if any(k in name_lower for k in ['todo', 'task', 'list', '待辦', '任務', '清單']):
        return {
            "files": {
                "models.py": """from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TodoItem(models.Model):
    PRIORITY_CHOICES = [
        ('low', '低'), ('medium', '中'), ('high', '高')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
""",
                "views.py": """from rest_framework import viewsets, filters
from .models import TodoItem, Category
from .serializers import TodoSerializer, CategorySerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['due_date', 'priority']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
""",
                "serializers.py": """from rest_framework import serializers
from .models import TodoItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
""",
                "urls.py": """from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'tasks', TodoViewSet, basename='task')

urlpatterns = [path('', include(router.urls))]
""",
                "requirements.txt": "Django>=4.2.0\ndjangorestframework>=3.14.0\n"
            },
            "setup_instructions": "### 待辦事項管理 (Demo Mode)\n\n1. `pip install -r requirements.txt`\n2. `python manage.py migrate`\n3. `python manage.py runserver`"
        }

    # 默認：電商系統
    return {
        "files": {
            "models.py": """from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="商品名稱")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="價格")
    stock = models.IntegerField(default=0, verbose_name="庫存")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
""",
            "views.py": """from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'])
    def purchase(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        
        try:
            with transaction.atomic():
                product = Product.objects.select_for_update().get(id=product_id)
                if product.stock >= quantity:
                    product.stock -= quantity
                    product.save()
                    order = Order.objects.create(
                        user=request.user,
                        product=product,
                        quantity=quantity
                    )
                    return Response(OrderSerializer(order).data)
                else:
                    return Response(
                        {"error": "庫存不足"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except Product.DoesNotExist:
            return Response({"error": "商品不存在"}, status=404)
""",
            "serializers.py": """from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
""",
            "urls.py": """from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))]
""",
            "requirements.txt": """Django>=4.2.0
djangorestframework>=3.14.0
psycopg2-binary>=2.9.0
"""
        },
        "setup_instructions": "### 電商系統 (Demo Mode)\n\n這是一個生成的 Django 電商系統範例。\n\n1. 安裝依賴: pip install -r requirements.txt\n2. 遷移數據庫: python manage.py migrate\n3. 啟動服務器: python manage.py runserver"
    }

