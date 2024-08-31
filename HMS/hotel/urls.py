from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('events/', events, name="events"),
    path('announcements/', announcements, name="announcements"),
    path('event-profile/<str:id>/', event_profile, name="event-profile"),
    path('event-edit/<str:pk>/', event_edit, name="event-edit"),
    path('error/', error, name="error"),
    path('payment/', payment, name="payment"),
    path('verify/', verify, name="verify"),
    path('deleteStorage/<str:pk>/', deleteStorage, name="deleteStorage"),
    path('deleteFoodMenu/<str:pk>/', deleteFoodMenu, name="deleteFoodMenu"),
    path('food-menu/', food_menu, name="food-menu"),
    path('storage/', storage, name="storage"),
    path('food-menu/<str:pk>/', food_menu_edit, name="food-menu-edit"),
    path('createEvent/', createEvent, name="createEvent"),
    path('deleteEvent/<str:pk>/', deleteEvent, name="deleteEvent"),
    path('deleteAnnouncement/<str:pk>/',
         deleteAnnouncement, name="deleteAnnouncement"),
    path('accounts/<str:pk>/', accounts_page, name='accounts'),
    path('dashboard/<str:pk>/', index_page, name='dashboard'),
    path('transactions/<str:pk>/', transaction_page, name="transaction"),
    path('room_booking_list/<str:pk>/', room_booking_list, name="room-booking-list"),
    path('check_in_out/<str:pk>/', checkin_out, name="checkin-out"),
    path('room-status/<str:pk>/', room_status, name="room-status"),
    path('item-unit-list/<str:pk>/', item_unit_list, name="item-unit-list"),
    path('item-list/<str:pk>/', item_list, name="item-list"),
    path('item-destroyed-list/<str:pk>/', item_destroyed_list, name="item-destroyed-list"),
    path('item-category-list/<str:pk>/', item_category_list, name="item-category-list"),
    path('item-suppliers-list/<str:pk>/', item_suppliers_list, name="item-suppliers-list"),
    path('booking-report/<str:pk>/', booking_report, name="booking-report"),
    path('stock-report/<str:pk>/', stuck_report, name="stock-report"),
    path('purchase-report/<str:pk>/', purchase_report, name="purchase-report"),
    path('frontdesk/<str:pk>/', front_desk, name="front-desk"),

]
