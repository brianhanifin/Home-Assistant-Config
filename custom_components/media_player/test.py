    @staticmethod
    def get_last_alexa(url, session):
        """Get the Alexa device that was last used."""
        try:

            response = session.get('https://alexa.' + url +
                                   '/api/activities?startTime=&size=1&offset=1')
            return response.json()
        except Exception as ex:
            template = ("An exception of type {0} occurred."
                        " Arguments:\n{1!r}")
            message = template.format(type(ex).__name__, ex.args)
            _LOGGER.error("An error occured accessing the API: {}".format(
                message))
            return None

    """
    From alexa_remote_control.sh

    last_alexa()
    {
    ${CURL} ${OPTS} -s -b ${COOKIE} -A "Mozilla/5.0" -H "DNT: 1" -H "Connection: keep-alive" -L\
     -H "Content-Type: application/json; charset=UTF-8" -H "Referer: https://alexa.${AMAZON}/spa/index.html" -H "Origin: https://alexa.${AMAZON}"\
     -H "csrf: $(awk "\$0 ~/.${AMAZON}.*csrf[ \\s\\t]+/ {print \$7}" ${COOKIE})" -X GET \
     "https://${ALEXA}/api/activities?startTime=&size=1&offset=1" | jq -r '.activities[0].sourceDeviceIds[0].serialNumber' | xargs -i jq -r --arg device {} '.devices[] | select( .serialNumber == $device) | .accountName' ${DEVLIST}
    }
    """