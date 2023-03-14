from .models import WebsiteInfo, Project
from datetime import datetime


def web_info(request):
    current_year = datetime.now().year - 2013
    return {
        'web_data': WebsiteInfo.get_solo(),
        "years": current_year,
        "projects": Project.objects.count()
    }
