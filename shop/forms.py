from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['content', 'price', 'product_detail', 'stock', 'imgfile']
        labels = {
            'content': '제 품 명',
            'price': '가 격',
            'product_detail':'상세설명',
            'stock': '재고수량',
            'imgfile': '이 미 지'
        }