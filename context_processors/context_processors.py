from home_app.models import SideBar, Footer
from article_app.models import Article
from product_app.models import Product


def sidebar_footer(request):
    footer = Footer.objects.filter(allowing=True)
    sidebar_services = SideBar.objects.filter(services=True, allowing=True)
    sidebar_questions = SideBar.objects.filter(common_questions=True, allowing=True)

    recent_articles = Article.objects.filter(allowing=True)[:3]
    recent_products = Product.objects.filter(allowing=True)[:3]

    return {
        'footer': footer,
        'service': sidebar_services,
        'question': sidebar_questions,
        'recent_articles': recent_articles,
        'recent_products': recent_products,
    }
