from pythonosc import udp_client

ip, port = 'ipaddress', 5000

client = upd_client.SimpleUDPClient(ip, port)

msg = input ()
client.send_message("/position", msg)
print ('sent {} to {}'.format(msg, ip))
