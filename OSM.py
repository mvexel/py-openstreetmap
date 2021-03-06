from datetime import datetime
import dateutil
import requests


class OSMFeature(object):

    def __init__(self, *args, **kwargs):
        self.osmid = kwargs.get("osmid", 0)
        self.visible = kwargs.get("visible", "True")
        self.version = kwargs.get("version", 1)
        self.changeset = kwargs.get("changeset", None)
        if "timestamp" in kwargs:
            self.timestamp = dateutil.parser.parse(kwargs["timestamp"])  # FIXME catch parsing errors
        else:
            self.timestamp = datetime.now()
        self.user = kwargs.get("user", None)
        self.uid = kwargs.get("uid", None)
        super(OSMFeature, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "OSM {type} with id {osmid}".format(type=self.__class__.__name__, osmid=self.osmid)


class Node(OSMFeature):

    def __init__(self, *args, **kwargs):
        self.lat = kwargs.get("lat", 0.0)
        self.lon = kwargs.get("lon", 0.0)
        self.tags = []
        super(Node, self).__init__(*args, **kwargs)


class Way(OSMFeature):

    def __init__(self, *args, **kwargs):
        self.tags = []
        self.nodes = []
        super(Way, self).__init__(*args, **kwargs)


class Relation(OSMFeature):

    def __init__(self, *args, **kwargs):
        self.tags = []
        self.members = []
        super(Relation, self).__init__(*args, **kwargs)


class Changeset(object):

    def __init__(self, *args, **kwargs):
        pass


class OSMException(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


class APIServer(object):
    def __init__(self, *args, **kwargs):
        super(APIServer, self).__init__(*args, **kwargs)

    def Get(self, osmtype, osmid):
        pass
