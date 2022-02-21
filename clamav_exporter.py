import dns.resolver
import subprocess


server_answer = str(dns.resolver.resolve('current.cvd.clamav.net', 'TXT').response.answer[0]).replace('"', ':').split(':')

server_clamav_version = server_answer[1]
server_daily_database_version = server_answer[3]
server_main_database_version = server_answer[2]
server_bytecode_database_version = server_answer[8]


local_answer = str(subprocess.check_output('clamscan --version', shell=True)).replace(' ', '/').split('/')

local_answer = local_answer.replace(' ', '/').split('/')

local_clamav_version = local_answer[1]
local_daily_database_version = local_answer[2]

main_database_file = open('/var/lib/clamav/main.cvd','r', errors='replace')
local_main_database_version = main_database_file.readline().split(':')[2]
main_database_file.close()

bytecode_database_file = open('/var/lib/clamav/bytecode.cvd','r', errors='replace')
local_bytecode_database_version = bytecode_database_file.readline().split(':')[2]
bytecode_database_file.close()


print(
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