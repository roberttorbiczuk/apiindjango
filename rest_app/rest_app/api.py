from rest_framework import routers

from rest_app.rental.api_views import FriendViewset, BelongingViewset, BorrowedViewset

router = routers.DefaultRouter()
router.register(r'friends', FriendViewset)
router.register(r'belongings', BelongingViewset)
router.register(r'borrowings', BorrowedViewset)
