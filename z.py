from kazoo.client import KazooClient
from kazoo.handlers.threading import SequentialThreadingHandler
zk = KazooClient(hosts="localhost:2181",handler=SequentialThreadingHandler())
zk.start()
children = zk.get_children('/')
zk.stop()
