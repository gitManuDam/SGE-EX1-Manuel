dbname = 'postgres'
user = 'postgres'
password = 'root'
host = 'localhost'
port = '5432'

INFO="INFO"
ERROR="ERROR"

QUERY_VUELOS_CLIENTE= 'SELECT v.*  FROM scexamen.vuelos v join scexamen.usuariosvuelo uv on uv.id = v.id join scexamen.ciudades c on c.id = v.id where uv.idpasajero = :id'

QUERY_CLIENTE_DIRECCION='select d.calle, d.cp from scexamen.personas p join scexamen.direccion d on d.id = p.id where p.id=:id'

QUERY_VUELO_DATOS='select c1.nombre as c_origen, c2.nombre as c_destino, p.nombre, uv.preciobillete from scexamen.vuelos v join scexamen.ciudades c1 on v.idciudadorigen = c1.id join scexamen.ciudades c2 on v.idciudaddestino = c2.id join scexamen.usuariosvuelo uv on v.id = uv.idvuelo join scexamen.personas p on uv.idpasajero = p.id where v.id = :id'

UPDATE_ESTADO_VUELO="UPDATE scexamen.vuelos SET  estadovuelo='No destion' WHERE id in (5,7);"

UPDATE_FECHA_DEF ='UPDATE scexamen.personas p SET fechadefuncion= :fechadef,  WHERE p.id in(select p.id from scexamen.personas p join scexamen.usuariosvuelo uv on uv.idpasajero = p.id where uv.idvuelo in (5,7)) ;'