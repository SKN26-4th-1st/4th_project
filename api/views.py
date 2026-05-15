from django.shortcuts import render
from django.http import JsonResponse
from accounts.models import UserFavorite

# Create your views here.
def favorite(request, product_code):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"is_favorite": False})

        userfav = request.user.favorites.filter(product_code=product_code).first()

        if userfav:
            res = False
            userfav.delete()
        else:
            res = True
            _ = UserFavorite.objects.create(
                account=request.user,
                product_code=product_code
            )

        return JsonResponse({"is_favorite":res})
    

# data = json.loads(request.body)
# message = data.get("message")