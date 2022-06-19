import MySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='ArmenG', ssh_password='databasepassword',
    remote_bind_address=('ArmenG.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='ArmenG',
        passwd='databasepassword',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='ArmenG$db',
    )
    # Do stuff
    connection.close()