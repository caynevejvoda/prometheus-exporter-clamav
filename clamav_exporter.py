import dns.resolver
import subprocess


server_answer = dns.resolver.resolve('current.cvd.clamav.net', 'TXT').response.answer[0]

server_answer = str(server_answer)

server_answer = server_answer.replace('"', ':')
server_answer = server_answer.split(':')

server_clamav_version = server_answer[1]
server_daily_database_version = server_answer[3]
server_main_database_version = server_answer[2]
server_bytecode_database_version = server_answer[8]


local_answer = subprocess.check_output('clamscan --version', shell=True)

local_answer = str(local_answer)

local_answer = local_answer.replace(' ', '/')
local_answer = local_answer.split('/')

local_clamav_version = local_answer[1]
local_daily_database_version = local_answer[2]

main_database_file = open('/var/lib/clamav/main.cvd','r')
local_main_database_version = main_database_file.readline()
main_database_file.close()

local_main_database_version = local_main_database_version.split(':')
local_main_database_version = local_main_database_version[2]

bytecode_database_file = open('/var/lib/clamav/bytecode.cvd','r')
local_bytecode_database_version = bytecode_database_file.readline()
bytecode_database_file.close()

local_bytecode_database_version = local_bytecode_database_version.split(':')
local_bytecode_database_version = local_bytecode_database_version[2]


datei = open('clamav_server_database_version.prom','w')
datei.write(
    "# HELP server_clamav_version Version of ClamAV from ClamAV server.\n" + 
    "# TYPE server_clamav_version gauge\n" + 
    "server_clamav_version " + server_clamav_version + "\n" + 

    "# HELP server_daily_database_version Version of daily database from ClamAV server.\n" + 
    "# TYPE server_daily_database_version gauge\n" + 
    "server_daily_database_version " + server_daily_database_version + "\n" + 

    "# HELP server_main_database_version Version of main database from ClamAV server.\n" + 
    "# TYPE server_main_database_version gauge\n" + 
    "server_main_database_version " + server_main_database_version + "\n" + 

    "# HELP server_bytecode_database_version Version of bytecode database from ClamAV server.\n" + 
    "# TYPE server_bytecode_database_version gauge\n" + 
    "server_bytecode_database_version " + server_bytecode_database_version + "\n" +

    "# HELP local_clamav_version Local ClamAV version.\n" + 
    "# TYPE local_clamav_version gauge\n" + 
    "local_clamav_version " + local_clamav_version + "\n" +

    "# HELP local_daily_database_version Local daily database version.\n" + 
    "# TYPE local_daily_database_version gauge\n" + 
    "local_daily_database_version " + local_daily_database_version + "\n" +

    "# HELP local_main_database_version Local main database version.\n" + 
    "# TYPE local_main_database_version gauge\n" + 
    "local_main_database_version " + local_main_database_version + "\n" +

    "# HELP local_bytecode_database_version Local bytecode database version.\n" + 
    "# TYPE local_bytecode_database_version gauge\n" + 
    "local_bytecode_database_version " + local_bytecode_database_version
    )
datei.close()

datei = open('clamav_server_database_version.prom','r+')
print(datei.read())
datei.close()