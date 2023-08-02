from blog.models import Category, Article

def get_Categories(request):


    categories_in_use= Article.objects.filter(public=True).values_list('Categories', flat=True)
    Categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')
    

    return {
        'Categories': Categories,
        'ids' : categories_in_use
    }