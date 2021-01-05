--CREACIÓN TABLAS
--create table cliente (id_cliente serial PRIMARY KEY not null, nombre VARCHAR(50), calle VARCHAR(200), ciudad VARCHAR(50));
--create table empleado (id_empleado serial PRIMARY KEY not null, nombre VARCHAR(50), calle VARCHAR(200), ciudad VARCHAR(50));
--create table pedidos (id_pedido serial PRIMARY KEY not null, id_cliente int references cliente(id_cliente), id_empleado int references empleado(id_empleado), fecha date default current_timestamp);
--create table producto (id_producto serial PRIMARY KEY not null, nombre VARCHAR(50), precio decimal(8,2), existencias int);
--create table detalles_pedido (id_pedido int references pedidos(id_pedido), id_producto int references producto(id_producto), cantidad int, primary key(id_pedido, id_producto));

SELECT pedidos.id_pedido, fecha, sum(detalles_pedido.cantidad) as total_productos, 
	(SELECT round(avg(cantidad),2) from DETALLES_PEDIDO WHERE id_producto=1 AND pedidos.id_pedido=detalles_pedido.id_pedido) as media_peraExtra1kg,
	(SELECT round(avg(cantidad),2) from DETALLES_PEDIDO WHERE id_producto=2 AND pedidos.id_pedido=detalles_pedido.id_pedido) as media_manzanaGolden1kg,
	(SELECT round(avg(cantidad),2) from DETALLES_PEDIDO WHERE id_producto=3 AND pedidos.id_pedido=detalles_pedido.id_pedido) as media_kiwiZespi1kg,
	(SELECT round(avg(cantidad),2) from DETALLES_PEDIDO WHERE id_producto=4 AND pedidos.id_pedido=detalles_pedido.id_pedido) as media_platanoCanarias1kg,
	(SELECT round(avg(cantidad),2) from DETALLES_PEDIDO WHERE id_producto=5 AND pedidos.id_pedido=detalles_pedido.id_pedido) as media_naranjaPremium1kg
	FROM pedidos, detalles_pedido
	GROUP BY pedidos.id_pedido, detalles_pedido.id_pedido HAVING pedidos.id_pedido=detalles_pedido.id_pedido;
