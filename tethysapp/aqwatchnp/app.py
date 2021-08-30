from tethys_sdk.base import TethysAppBase, url_map_maker


class Aqwatchnp(TethysAppBase):
    """
    Tethys app class for Aqwatchnp.
    """

    name = 'Air Quality Watch - Nepal'
    index = 'aqwatchnp:recent'
    icon = 'aqwatchnp/images/icon.gif'
    package = 'aqwatchnp'
    root_url = 'aqwatchnp'
    color = '#2c3e50'
    description = ''
    tags = 'Air Quality Watch'
    enable_feedback = False
    feedback_emails = []


    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='recent',
                url='aqwatchnp/recent',
                controller='aqwatchnp.controllers.home.Recent'
            ), UrlMap(
                name='archive',
                url='aqwatchnp/archive',
                controller='aqwatchnp.controllers.home.Archive'
            ), UrlMap(
                name='forecast',
                url='aqwatchnp/forecast',
                controller='aqwatchnp.controllers.home.Forecast'
            ),
        )
        return url_maps
