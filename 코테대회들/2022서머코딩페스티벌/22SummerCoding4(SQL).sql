-- 코드를 입력하세요
SELECT fi.NAME as NAME_X, se.NAME as NAME_Y, COUNT(*) AS "장바구니 수"
from(
   SELECT distinct(NAME), cart_id
   FROM CART_PRODUCTS
   ) fi
   inner JOIN
   (
   SELECT distinct(NAME), cart_id
   FROM CART_PRODUCTS
   ) se
   ON fi.cart_id = se.cart_id
where fi.name!=se.name
group by name_X, name_y
order by NAME_x, name_y
