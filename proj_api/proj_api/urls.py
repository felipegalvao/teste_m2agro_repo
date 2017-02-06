"""proj_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from api_produtos_safra import views as safra_produto_views
from api_servicos import views as servicos_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # URLs da API de produtos e safra
    url(r'^produtos/$', safra_produto_views.ProdutoList.as_view(), name='produtos_list'),
    url(r'^produtos/atualizar_preco_medio/$', safra_produto_views.ProdutoUpdatePrecoMedio,
        name='produtos_update_preco_medio'),
    url(r'^produtos/(?P<pk>[0-9]+)/$', safra_produto_views.ProdutoDetail.as_view(),
        name='produtos_detail'),
    url(r'^safras/$', safra_produto_views.SafraList.as_view(), name='safra_list'),
    url(r'^safras/(?P<pk>[0-9]+)/$', safra_produto_views.SafraDetail.as_view(),
        name='safra_detail'),

    # URLs da API de serviços
    url(r'^servicos/$', servicos_views.ServicoList.as_view(), name='servicos_list'),
    url(r'^servicos/(?P<pk>[0-9]+)/$', servicos_views.ServicoDetail.as_view(),
        name='servicos_detail'),
    url(r'^linhas_servicos/$', servicos_views.LinhaServicoList.as_view(),
        name='linhas_servicos_list'),
    url(r'^linhas_servicos/(?P<pk>[0-9]+)/$', servicos_views.LinhaServicoDetail.as_view(),
        name='linhas_servicos_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
