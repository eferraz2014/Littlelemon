user 	/ password 		/ role 		/ 	token 
root 	/ root			/ admin		/	db6538a023647ee975f83ee8e7799fa75662db56
garcon	/ garcon1234$#	/ -			/	-

---------------------------------------------------------------------------------

urls
for user root use
use token:db6538a023647ee975f83ee8e7799fa75662db56
prefix: Token


for booking listing
http://127.0.0.1:8000/restaurant/booking/tables/

for individual booking operation (CRUD)
http://127.0.0.1:8000/restaurant/booking/tables/<int:pk>/

filtering datetime booking_date
http://127.0.0.1:8000/restaurant/booking/tables?booking_date=YYYY-MM-DD HH:MI:SS
---------------------------------------------------------------------------------
for menu listing
http://127.0.0.1:8000/restaurant/menu

for individual booking operation (CRUD)
http://127.0.0.1:8000/restaurant/menu/1/

for filtering menu by price or (lo_price and/or up_price) or title
http://127.0.0.1:8000/restaurant/menu?lo_price=1000&up_price=2500&title=Brusc
http://127.0.0.1:8000/restaurant/menu?price=2000&title=lemon

--------------------------------------------------------------------------------
test http://127.0.0.1:8000/api/api-token-auth with 
username:root / password:root
