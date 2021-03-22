from django.conf import settings

from edc_model_wrapper import ModelWrapper


class PerformanceImpModelWrapper(ModelWrapper):

    model = 'contract.performanceimpplan'
    querystring_attrs = ['contract', 'performance_assessment']
    next_url_attrs = ['contract', 'performance_assessment']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('appraisal_listboard_url')

    @property
    def performance_assessment(self):
        return self.object.performance_assessment