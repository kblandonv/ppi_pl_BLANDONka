SELECT pap.name, o.quantity, COUNT(o.PRODUCT_ID_ID) AS number_orderquantity
FROM product_api_orderdetail o
INNER JOIN product_api_product pap
ON o.product_id_id = pap.id 
GROUP BY o.PRODUCT_ID_ID
HAVING COUNT(o.PRODUCT_ID_ID) >=2
ORDER BY o.PRODUCT_ID_ID
