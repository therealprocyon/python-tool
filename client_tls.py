#!/usr/bin/env python3
import socket
import ssl
import string
import sys


def start_conn(host,port):


    addr = (host,port)
        
    
    response = input("Enter buffer size: ")
    try:
       response = int(response)
       if response <= 65535 and response >= 0:
           BUFFER_SIZE = response
           print(BUFFER_SIZE)
       else:
            print("The buffersize is invalid: " + \
            str(response))
            exit()
    except ValueError:
        print("The input is invalid: " + \
        response)
        exit()
    except:
        print("Oopsie woopsie, we did a fuckywucky")
        exit()
    

    context = ssl.create_default_context()
    
    print("Enter your request header: ")
    request = sys.stdin.buffer.readline()
#    byte_request = request.encode('utf-8')


    with socket.create_connection(addr) as s:
        with context.wrap_socket(s, server_hostname=host) as ssock:
           # cert = ssock.getpeercert()
            #pprint.pprint(cert)
            #print(ssock.version())
            ssock.send(request)
            
            while True:
                data = ssock.recv(BUFFER_SIZE)
                if ( len(data) < 1 ):
                    break
                sys.stdout.buffer.write(data)

