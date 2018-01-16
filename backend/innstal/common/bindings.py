from channels_api import detail_action, list_action
from channels_api.bindings import ResourceBinding

from common.models import UserPlans
from common.serializer import UserPlanSerializer


class UserPlanBinding(ResourceBinding):

    model = UserPlans
    stream = "questions"
    serializer_class = UserPlanSerializer
    queryset = UserPlans.objects.all()

    # @detail_action()
    # def publish(self, pk, data=None, **kwargs):
    #     instance = self.get_object(pk)
    #     result = instance.publish()
    #     return result, 200
    #
    # @list_action()
    # def report(self, data=None, **kwargs):
    #     report = self.get_queryset().build_report()
    #     return report, 200