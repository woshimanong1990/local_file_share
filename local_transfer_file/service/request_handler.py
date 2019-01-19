# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import os
import logging
import json
import urllib.parse
import posixpath
import sys
import html
import io

from http.server import SimpleHTTPRequestHandler, HTTPStatus

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
    config_file = os.path.join(bundle_dir, "config.json")
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

    config_file = os.path.join(bundle_dir, "config.json")

logger = logging.getLogger()


class CustomRequestHanlder(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # abandon query parameters
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        # Don't forget explicit trailing slash when normalizing. Issue17324
        trailing_slash = path.rstrip().endswith('/')
        try:
            path = urllib.parse.unquote(path, errors='surrogatepass')
        except UnicodeDecodeError:
            path = urllib.parse.unquote(path)
        path = posixpath.normpath(path)
        if trailing_slash:
            path += '/'
        return path

    def auth_request(self, path, query_data, save_data):
        if path != "/download_file":
            return False
        # print(query_data)
        if "file_path" not in query_data or "code" not in query_data:
            return False
        file_path = query_data.get("file_path", [None])[0]
        code = query_data.get("code", [None])[0]
        if not file_path or not code:
            return False
        saved_file_path = save_data.get("file_path", None)
        if not saved_file_path:
            return False
        saved_code = save_data.get("code", None)
        if saved_code != code:
            return False
        if not os.path.exists(file_path):
            return False
        if os.path.isfile(saved_file_path) and saved_file_path != file_path:
            return False
        if os.path.isdir(saved_file_path) and not file_path.startswith(saved_file_path):
            return False
        return True

    def get_file(self, path):
        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return None
        try:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", ctype)
            fs = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
            return f
        except:
            f.close()
            raise

    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().

        """
        try:
            file_list = os.listdir(path)
        except OSError:
            self.send_error(
                HTTPStatus.NOT_FOUND,
                "No permission to list directory")
            return None
        file_list.sort(key=lambda a: a.lower())
        r = []
        try:
            displaypath = urllib.parse.unquote(self.path,
                                               errors='surrogatepass')
        except UnicodeDecodeError:
            displaypath = urllib.parse.unquote(path)
        displaypath = html.escape(displaypath, quote=False)
        enc = sys.getfilesystemencoding()
        title = 'Directory listing for %s' % displaypath
        r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                 '"http://www.w3.org/TR/html4/strict.dtd">')
        r.append('<html>\n<head>')
        r.append('<meta http-equiv="Content-Type" '
                 'content="text/html; charset=%s">' % enc)
        r.append('<title>%s</title>\n</head>' % title)
        r.append('<body>\n<h1>%s</h1>' % title)
        r.append('<hr>\n<ul>')
        for name in file_list:
            fullname = os.path.join(path, name)
            displayname = name
            linkname = self.get_link_file_name(fullname)
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = self.get_link_file_name(fullname + "/")
            if os.path.islink(fullname):
                displayname = name + "@"
                # Note: a link to a directory displays with @ and links with /
            r.append('<li><a href="%s">%s</a></li>'
                    % (linkname,
                       html.escape(displayname, quote=False)))
        r.append('</ul>\n<hr>\n</body>\n</html>\n')
        encoded = '\n'.join(r).encode(enc, 'surrogateescape')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        return f

    def get_link_file_name(self, file_path):
        url_obj = urllib.parse.urlparse(self.path)
        query_data = urllib.parse.parse_qs(url_obj.query)
        new_data = []
        query_data["file_path"] = [file_path]
        for k, v in query_data.items():
            if len(v) > 1:
                item = "&".join(["{}={}".format(k, _) for _ in v])
            else:
                value = "" if not v else v[0]
                item = "{}={}".format(k, value)
            new_data.append(item)

        link_name = "http://{host}:{port}{path}?{query}".format(host=self.client_address[0],
                                                                 port=self.server.server_port,
                                                                 path=urllib.parse.quote(url_obj.path,
                                                                                         errors='surrogatepass'),
                                                                 query=urllib.parse.quote("&".join(new_data),
                                                                                          errors='surrogatepass')
                                                                 )
        return link_name

    def do_GET(self):
        try:
            # print(self.server.server_port)
            # print(self.client_address)
            url_obj = urllib.parse.urlparse(self.path)
            if url_obj.path == "/favicon.ico":
                return self.send_response(200, "OK")

            query_data = urllib.parse.parse_qs(urllib.parse.unquote(url_obj.query))
            with open(config_file, "r") as f:
                save_data = json.load(f)
            result = self.auth_request(url_obj.path, query_data, save_data)
            if not result:
                return self.send_error(400, "Bad Request")
            saved_file_path = save_data.get("file_path", None)
            file_path = query_data.get("file_path", [None])[0]

            path = self.translate_path(file_path)
            if os.path.isdir(path):
                if not path.endswith("/"):
                    path += "/"
                f = self.list_directory(path)
            else:
                f = self.get_file(path)
            if f:
                try:
                    self.copyfile(f, self.wfile)
                finally:
                    f.close()

        except:
            logger.error("server error", exc_info=True)
            return self.send_error(500, "Sorry, Server Error.")
