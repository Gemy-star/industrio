from .models import WebsiteInfo


def web_info(request):
        return {
            'web_data':WebsiteInfo.get_solo(),
        }