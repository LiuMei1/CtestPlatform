-D                  connect to srv directly, smaple: -D 10000. must use root
                        notice: if set -D, "-u -p -cdt -client_version -ip -port" well be ignore!
                        -webdenied: will connect to webdeniedwrk,only valid in set -D,"-ip -port" on work, default: oprtproxy.moa.kdzl.cn:7472!
                        -oprtproxy: will connect to oprtproxywrk,only valid in set -D,"-ip -port" on work, default: webdenied.moa.kdzl.cn:7728!!
                        -sh_did   : set srvhead->from_did, smaple: -sh_did 10000, default: same with -D
                        -sh_pid   : set srvhead->from_pid, smaple: -sh_pid 1783, no default
                        -to_did   : set srvhead->to_did, smaple: -to_did 1000, no default
                        -to_pid   : set srvhead->to_pid, smaple: -to_pid 1783, no default
                        -from_client_version : set srvhead->client->client_version, smaple: -from_client_version 4.1.0, no default
-u                  connect server user
-cdt                : connect to server client type: [{0:android},{1:ios},{2:wp},{3:server},{4:web},{5:ios_beta},{6:android_beta}]. default : 3
-client_version     : connect to server client version, smaple: -client_version 2.5.0 ,default: 9.9.9
-us                 connect server user list,smaple: -us 10000000000-10000001000
-p                  connect server pass, default : 12345
-ip                 connect server ip, default : workip
-port               connect server port, default : 6800
-trace              setlog to trace
-PB_PRINT           print pb with PB_PRINT, default: PB_PRINT_JSON
-srv                print server help, default: list all server
-s                  srvop , smaple: -s 0x301. support: name, hex, int
-j                  input: input data, format json
-f                  input: input file, format xml, user for simc
-cnt                send count: send cnts,smaple: -cnt 1000
-perf               multi time.print times
-h                  or --help, print help
-noauth             without auth
-msrv               connect to go global srv directly


