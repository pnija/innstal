from channels import route_class
from channels.generic.websockets import WebsocketDemultiplexer

from common.bindings import UserPlanBinding


class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'questions': UserPlanBinding.consumer
    }

channel_routing = [
    route_class(APIDemultiplexer)
]