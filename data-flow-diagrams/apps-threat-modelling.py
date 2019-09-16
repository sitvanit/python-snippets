#!/usr/bin/env python3
from pytm import TM, Server, Datastore, Dataflow, Boundary, Actor, Element

tm = TM("Apps")
tm.description = "Apps threat modeling"

internet = Boundary("Internet")
machine = Boundary("User's machine")
apps_vpc = Boundary("Apps VPC")
rds_boundary = Boundary("RDS security group")
cache_boundary = Boundary("ElastiCache security group")

user = Actor("User/Browser")
user.inBoundary = machine

apigee = Element("Apigee")
apigee.inBoundary = internet
apigee.isHardened = True

apigee = Element("Apigee")
apigee.inBoundary = internet
apigee.isHardened = True

server = Server("Apps Server")
server.inBoundary = apps_vpc
server.isHardened = True
server.hasAccessControl = True
server.encodesOutput = True

db = Datastore("MySQL DB")
db.isHardened = True
db.hasAccessControl = True
db.inBoundary = apps_vpc
db.inBoundary = rds_boundary
db.isSQL = True
db.inScope = True
db.onAWS = True
db.isShared = True
db.storesSensitiveData = False

redis = Datastore("Redis")
redis.isHardened = True
redis.inBoundary = apps_vpc
redis.inBoundary = cache_boundary
redis.isSQL = False
redis.inScope = True
db.onAWS = True
db.isShared = False
db.storesSensitiveData = False

third_party = Element("3rd party services")
third_party.inBoundary = internet

third_party_bim = Element("3rd party BIM360 services")
third_party_bim.inBoundary = internet

user_to_apigee = Dataflow(user, apigee, "User sends API request to Apps service")
user_to_apigee.protocol = "HTTPS"
user_to_apigee.isEncrypted = True
user_to_apigee.authenticatedWith = True
user_to_apigee.dstPort = 443
user_to_apigee.data = 'JSON'
user_to_apigee.order = 1

apigee_to_server = Dataflow(apigee, server, "Apigee forwards API request to Apps server")
apigee_to_server.protocol = "HTTPS"
apigee_to_server.isEncrypted = True
apigee_to_server.authenticatedWith = True
apigee_to_server.dstPort = 443
apigee_to_server.data = 'JSON'
apigee_to_server.order = 2

server_to_third_party = Dataflow(server, third_party, "Apps server communicates with 3rd party services")
server_to_third_party.authenticatedWith = True
server_to_third_party.isEncrypted = True
server_to_third_party.dstPort = 0
server_to_third_party.order = 3

server_to_third_party_bim = Dataflow(server, third_party_bim, "Apps server communicates with 3rd party BIM360 services")
server_to_third_party_bim.authenticatedWith = True
server_to_third_party_bim.isEncrypted = True
server_to_third_party_bim.dstPort = 0
server_to_third_party_bim.order = 3

server_to_redis = Dataflow(server, redis, "Apps server inquires data from Redis")
server_to_redis.dstPort = 6379
server_to_redis.order = 4

server_to_db = Dataflow(server, db, "Apps server inquires data from DB")
server_to_db.isEncrypted = True
server_to_db.authenticatedWith = True
server_to_db.dstPort = 3306
server_to_db.order = 4

db_to_server = Dataflow(db, server, "Apps server gets data from DB")
db_to_server.isEncrypted = True
db_to_server.authenticatedWith = True
db_to_server.dstPort = 0
db_to_server.order = 5

redis_to_server = Dataflow(redis, server, "Apps server gets data from Redis")
redis_to_server.isEncrypted = True
redis_to_server.dstPort = 0
redis_to_server.order = 5

third_to_server = Dataflow(third_party, server, "Apps server gets data from 3rd-party services")
third_to_server.authenticatedWith = True
third_to_server.isEncrypted = True
third_to_server.dstPort = 0
third_to_server.order = 5

third_bim_to_server = Dataflow(third_party_bim, server, "Apps server gets data from 3rd-party BIM360 services")
third_bim_to_server.authenticatedWith = True
third_bim_to_server.isEncrypted = True
third_bim_to_server.dstPort = 0
third_bim_to_server.order = 5

server_to_apigee = Dataflow(server, apigee, "Apps Server returns an answer to Apigee")
server_to_apigee.protocol = "HTTPS"
server_to_apigee.isEncrypted = True
server_to_apigee.authenticatedWith = True
server_to_apigee.dstPort = 0
server_to_apigee.data = 'JSON'
server_to_apigee.order = 6

apigee_to_user = Dataflow(apigee, user, "Apigee forwards response to user")
apigee_to_user.protocol = "HTTPS"
apigee_to_user.isEncrypted = True
apigee_to_user.authenticatedWith = True
apigee_to_user.dstPort = 0
apigee_to_user.data = 'JSON'
apigee_to_user.order = 7


tm.process()
